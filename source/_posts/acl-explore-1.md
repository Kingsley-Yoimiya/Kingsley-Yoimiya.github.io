---
title:  Arm Compute Library 结构初探 1
date: '2024-11-11 19:43:00'
updated: '2024-11-11 19:43:00'
excerpt: >-
  主要是要求看 kernel，但是整个仓库代码实在是太大了，于是先理清结构来着。
  - GPU
  - ARM
categories: [技术向]
permalink: /post/acl-explore-1.html
comments: true
---
# Arm Compute Library 结构初探 1

## 前言

主要是要求看 kernel，但是整个仓库代码实在是太大了，于是先理清结构来着。

## 基本结构——以 conv 为例子

先让 ChatGPT 开路，我们知道可以这样写一个 Conv 代码：

```cpp
#include "arm_compute/runtime/CL/CLScheduler.h"
#include "arm_compute/runtime/CL/CLTensor.h"
#include "arm_compute/runtime/CL/functions/CLConvolutionLayer.h"
#include "arm_compute/core/Types.h"

// Initialize the ARM Compute Library and OpenCL
void initialize_acl_opencl() {
    // Set up OpenCL scheduler (initializes OpenCL context and queue)
    arm_compute::CLScheduler::get().default_init();
}

// Perform a convolution operation using OpenCL
void perform_convolution() {
    // Define and allocate input/output tensors
    arm_compute::CLTensor input, output, weights;
    input.allocator()->init(arm_compute::TensorInfo(...)); // Specify tensor shape & format
    output.allocator()->init(arm_compute::TensorInfo(...));
    weights.allocator()->init(arm_compute::TensorInfo(...));

    // Configure convolution layer
    arm_compute::CLConvolutionLayer conv;
    conv.configure(&input, &weights, nullptr, &output, ...); // Configure with your parameters

    // Allocate memory for tensors
    input.allocator()->allocate();
    output.allocator()->allocate();
    weights.allocator()->allocate();

    // Run the convolution
    conv.run();
}
```

我们可以明白基本的使用 ACL 的方式：

1. 所有操作前面都需要 `arm_compute::CLScheduler::get().default_init();`​
2. 一种很重要的操作可以通过 `CLTensor`​ 进行。

    1. `CLTensor`​需要进行 allocator()->init() 以及 allocator()->allocate() 才能操作
3. 如果要进行运算，可以先定义一个 `function`​，比如 `arm_compute::CLConvolutionLayer`​，对于 `conv `​我们需要进行 `configure()`​，确定基本信息，最后 `run()。`​

因此确定重点内容：

1. **​`conv`​**​ **如何进行** **​`run()`​** ​ **的（最重要）** ，以及 `configure()`​ 时候干了什么预处理操作？
2. 接着是 `allocator()`​, `CLSceduler()`​ 等等的逻辑。

## Convolutionlayer

### 背景知识补充

通过 GPT 提示，找到了 `src/runtime/CL/functions/CLConvolutionLayer.cpp`​这个是实现，对照 `arm_compute/runtime/CL/functions/CLConvolutionLayer.h`​一起看。

首先我们可以看到注释，告诉我们实际上 `CLConvolution.h`​ 是在进行算法选择：

```cpp
 * -# opencl::ClGemmConv2d
 * -# opencl::ClWinogradConv2d
 * -# opencl::ClDirectConv2d
 * -# @ref CLFFTConvolutionLayer
 *
 * The function selects one of the algorithms mentioned above based on:
 *      - The size of the kernel
 *      - Number of input/output feature maps
 *      - Amount of memory needed
 *
 * Generally GEMM-based convolution is executed when neither Winograd nor FFT nor Direct convolution can be performed.
 *
 * FP32 Algorithm| Filter Size                                                 |   Input/Output feature maps               |
 * --------------|-------------------------------------------------------------|-------------------------------------------|
 * Winograd      | 3x3 1x3 3x1 5x1 1x5 5x5(fast maths) 7x1 1x7                 |  Input channels is greater than 3         |
 * FFT           | Squared kernels and greater than 9x9                        |  Input feature maps > Output feature maps |
 * DirectConv    | 9x9                                                         |                                           |
 * GEMM          | Any size                                                    |                                           |
 *
 * Winograd 5x5 requires fast maths enabled.
```

告诉我们：

The `CLConvolutionLayer`​ class can use several different algorithms, each optimized for specific conditions:

* **GEMM-Based Convolution**: General matrix multiplication, a common fallback when other algorithms aren’t suitable.
* **Winograd Convolution**: Fast for small kernel sizes (like 3x3), especially when using fast math.
* **Direct Convolution**: A straightforward convolution, effective for certain kernel sizes (e.g., 9x9).
* **FFT Convolution**: Suited for very large kernel sizes (e.g., \> 9x9) and input/output feature maps where FFT-based convolutions are efficient.

接着跳过一段构造、销毁、禁止 conv 复制的代码，新的注释：

```cpp
/** Set the input and output tensors.
     *
     * Valid data layouts:
     * - NHWC
     * - NCHW
     *
     * Valid data type configurations:
     * |src0           |src1               |src2   |dst            |
     * |:--------------|:------------------|:------|:--------------|
     * |F16            |F16                |F16    |F16            |
     * |F32            |F32                |F32    |F32            |
     * |QASYMM8        |QASYMM8            |S32    |QASYMM8        |
     * |QASYMM8        |QSYMM8_PER_CHANNEL |S32    |QASYMM8        |
     * |QASYMM8_SIGNED |QASYMM8_SIGNED     |S32    |QASYMM8_SIGNED |
     * |QASYMM8_SIGNED |QSYMM8_PER_CHANNEL |S32    |QASYMM8_SIGNED |
```

补充知识：`NHWC`​中的含义

* N：Batchsize
* H：height
* W：width
* C：color channels

### configure() 函数

接着看到 configure 函数了，这是一个主要部分。

```cpp
     * @param[in]  input            Source tensor. 3 lower dimensions represent a single input [width, height, IFM],
     *                              while every optional dimension from 4 and above represent a batch of inputs.
     *                              Data types supported: QASYMM8/QASYMM8_SIGNED/F16/F32.
     * @param[in]  weights          Weights tensor. Weights are 4D tensor with dimensions [kernel_x, kernel_y, IFM, OFM].
     *                              Data type supported: Same as @p input, also could be QSYMM8_PER_CHANNEL if input is QASYMM8/QASYMM8_SIGNED.
     * @param[in]  biases           Biases tensor. Shared biases supported. Biases are 1D tensor with dimensions [OFM].
     *                              Data type supported: Same as @p input, except for input of QASYMM8/QASYMM8_SIGNED type where biases should be of S32 type.
     * @param[out] output           Destination tensor. 3 lower dimensions represent a single output [width, height, OFM], while the rest represent batch of outputs.
     *                              Data types supported: Same as @p input.
     * @param[in]  conv_info        Contains padding and stride information described in @ref PadStrideInfo.
     * @param[in]  weights_info     Specifies if the weights tensor has been reshaped with CLWeightsReshapeKernel. Data type supported: Same as @p input.
     * @param[in]  dilation         (Optional) Dilation, in elements, across x and y. Defaults to (1, 1).
     * @param[in]  act_info         (Optional) Activation layer information in case of a fused activation.
     * @param[in]  enable_fast_math (Optional) Enable fast math computation. In case this flag were set, the function could dispatch the fastest implementation
     *                              available which may introduce a drop of accuracy as well. Default is false
     * @param[in]  num_groups       (Optional) Number of groups when performing a grouped convolution. num_groups != 1 is only supported for NCHW data layout
     */
    void configure(ICLTensor                 *input,
                   const ICLTensor           *weights,
                   const ICLTensor           *biases,
                   ICLTensor                 *output,
                   const PadStrideInfo       &conv_info,
                   const WeightsInfo         &weights_info     = WeightsInfo(),
                   const Size2D              &dilation         = Size2D(1U, 1U),
                   const ActivationLayerInfo &act_info         = ActivationLayerInfo(),
                   bool                       enable_fast_math = false,
                   unsigned int               num_groups       = 1);
```

接下来可以确定一种常见的数据形式就是 `ICLTensor`​，conv 配置需要看 `PadStrideInfo`​，weights 有 `WeightsInfo`​，剩下的可以不管。

#### PadStrideInfo

```cpp
/** Constructor
     *
     * @param[in] stride_x (Optional) Stride, in elements, across x. Defaults to 1.
     * @param[in] stride_y (Optional) Stride, in elements, across y. Defaults to 1.
     * @param[in] pad_x    (Optional) Padding, in elements, across x. Defaults to 0.
     * @param[in] pad_y    (Optional) Padding, in elements, across y. Defaults to 0.
     * @param[in] round    (Optional) Dimensions rounding. Defaults to @ref DimensionRoundingType::FLOOR.
     */
```

可以看到对于卷积层，我们有 stride，表示每隔多少元素进行一次卷积，有 pad 表示图像的边缘补上 0。

#### WeightsInfo

```cpp
/** Constructor
     *
     * @param[in] are_reshaped            True if the weights have been reshaped
     * @param[in] kernel_width            Kernel width.
     * @param[in] kernel_height           Kernel height.
     * @param[in] num_kernels             Number of convolution kernels.
     * @param[in] retain_internal_weights (Optional) True if internal reshaped weights must be retained. Used for reconfiguration purposes. Default is false.
     * @param[in] weight_format           (Optional) arm_gemm:WeightFormat enumeration requested by the user. Default is arm_compute::WeightFormat::UNSPECIFIED.
     */
```

可以看到有 基础的 kernel 信息，kernel 个数（获取最后的输出深度）等等。

#### Size2D

就是基础的 WH：

```cpp
/** Constructor. Initializes "width" and "height" respectively with "w" and "h"
     *
     * @param[in] w Width of the image or rectangle
     * @param[in] h Height of the image or rectangle
     */
```

#### ActivationLayerInfo

可以主要是 activation func：

```cpp
/** Default Constructor
     *
     * @param[in] f The activation function to use.
     * @param[in] a (Optional) The alpha parameter used by some activation functions
     *              (@ref ActivationFunction::BOUNDED_RELU, @ref ActivationFunction::LU_BOUNDED_RELU, @ref ActivationFunction::LINEAR, @ref ActivationFunction::TANH).
     * @param[in] b (Optional) The beta parameter used by some activation functions (@ref ActivationFunction::LINEAR, @ref ActivationFunction::LU_BOUNDED_RELU, @ref ActivationFunction::TANH).
     */
```

### 函数部分

```cpp
const Conv2dInfo conv2d_info = Conv2dInfo(conv_info, dilation, act_info, enable_fast_math, num_groups);
switch (opencl::ClConv2d::get_convolution_method(input->info(), weights->info(), output->info(), conv2d_info,
                                                     weights_info, CLScheduler::get().target()))
```

这个就是开头提到的进行 conv 实现方式选择的代码。

接下来就是根据 `get_convolution_method`​ 进行选择的结果：

```cpp
case ConvolutionMethod::WINOGRAD:
case ConvolutionMethod::DIRECT:
case ConvolutionMethod::INDIRECT:
case ConvolutionMethod::GEMM:
{
    auto f = std::make_unique<opencl::ClConv2d>();
    f->configure(compile_context, input->info(), weights->info(),
                    ((biases != nullptr) ? biases->info() : nullptr), output->info(), conv2d_info, weights_info);
    _impl->op = std::move(f);
    break;
}
case ConvolutionMethod::FFT:
{
    auto f = std::make_unique<CLFFTConvolutionLayer>(_impl->memory_manager);
    f->configure(compile_context, input, weights, biases, output, conv_info, act_info, enable_fast_math);
    _impl->func = std::move(f);
    break;
}
default:
    ARM_COMPUTE_ERROR("Not supported.");
    break;
```

也就是除了 FFT，其他都可以用 OpenCL 的实现。

不过还是要看 `get_convolution_method`​，`CLFFTConvolutionLayer`​。

#### get_convolution_method

首先是对于特殊的神经网络选取预设的最好的参数：

```cpp
const std::vector<ConfigurationMethod> known_configs = {
	// Alexnet
   	ConfigurationMethod(ConvolutionConfiguration(Size2D(27U, 27U), Size2D(5U, 5U), Size2D(48U, 128U),
                                                PadStrideInfo(1U, 1U, 2U, 2U), DataLayout::NCHW),
                       ConvolutionMethod::DIRECT),
```

再接着是一堆特判，根据前面的注释判断是否选择特定的实现方法。

#### CLFFTConvolutionLayer

几乎都是大部分的处理，通过观察 `src/runtime/CL/functions/CLFFTConvolutionLayer.cpp`​ 和 `src/runtime/CL/functions/CLFFT1D.cpp`​可以找到真正的 kernel 了：`src/core/CL/kernels/CLFFTRadixStageKernel.cpp`​ 中提到了：

```cpp
std::string kernel_name = "fft";
kernel_name += "_radix_" + support::cpp11::to_string(config.radix);
kernel_name += (config.is_first_stage) ? "_first_stage" : "";
kernel_name += "_axis_" + support::cpp11::to_string(config.axis);
_kernel = create_kernel(compile_context, kernel_name, build_opts.options());
```

因此可以找到一系列 kernel，比如名字是 `fft_radix_2_first_stage_axis_0`​的 kernel，放在`src/core/CL/cl_kernels/common/fft.cl`​ 中。

后续就是看具体的 kernel 实现了，只要找 `src/core/CL/cl_kernels/common/`​就行了！

