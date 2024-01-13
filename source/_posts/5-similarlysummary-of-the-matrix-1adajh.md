---
title: 5 矩阵的相抵与相似-总结
updated: '2024-01-13 18:04:38'
excerpt: >-
  矩阵的相抵与相似总结矩阵的相抵设a_{stimesn}证明_a的秩为r的充要条件是存在数域k上stimesr列满秩矩阵和rtimesn行满秩矩阵c使得a=bc。证明rightarrow考虑可逆pq有a=pbegin{pmatrix}i_rend{pmatrix}begin{pmatrix}q_q_end{pmatrix}其中p_r列q_r行。于是a=p_q_。证明leftarrow有r(a)leqslantr(b)因此r(a)leqslantr。而同时r(a)geqslantr(b)r(c)r（练习题目直
tags:
  - 高等代数
  - 数学
categories: []
permalink: /post/5-similarlysummary-of-the-matrix-1adajh.html
comments: true
---

# 5 矩阵的相抵与相似-总结

## 矩阵的相抵

> 设 $A_{s \times n}$，证明：$A$ 的秩为 $r$ 的充要条件是存在数域 $K$ 上 $s\times r$ 列满秩矩阵和 $r\times n$ 行满秩矩阵 $C$，使得 $A=BC$。

证明 $\Rightarrow$，考虑可逆 $P,Q$，有 $A=P\begin{pmatrix} I_r &0 \\ 0 & 0\end{pmatrix} Q$，进而表示 $A=\begin{pmatrix}P_1,P_2\end{pmatrix}\begin{pmatrix} I_r &0 \\ 0 & 0\end{pmatrix}\begin{pmatrix} Q_1\\ Q_2\end{pmatrix}$，其中 $P_1$ $r$列，$Q_1$ $r$ 行。

于是 $A=P_1Q_1$。

证明 $\Leftarrow$，有 $r(A)\leqslant r(B)$，因此 $r(A)\leqslant r$。

而同时 $r(A)\geqslant r(B)+r(C)-r$（练习题目，直接构造分块矩阵即可），因此 $r(A)\geqslant r$。于是 $r(A)=r$。

> 设 $A$ 为实数域上 $n$ 级对称矩阵，且 $A$ 的秩为 $r>0$，证明 $A$ 的所有非 0 主子式同号。

存在可逆 $P,Q$ 满足 $A=P\begin{pmatrix}I_{r} & 0\\0 & 0\end{pmatrix} Q$，同时

$$
A^{T} =Q^{T}\begin{pmatrix}I_{r} & 0\\0 & 0\end{pmatrix} P^{T} =T=P\begin{pmatrix}I_{r} & 0\\0 & 0\end{pmatrix} Q\Rightarrow P^{-1} Q^{T}\begin{pmatrix}I_{r} & 0\\0 & 0\end{pmatrix} =\begin{pmatrix}I_{r} & 0\\0 & 0\end{pmatrix} Q\left( P^{T}\right)^{-1}
$$

令 

$$
\displaystyle P^{-1} Q^{T} =\begin{pmatrix}
H_{1} & H_{2}\\
H_{3} & H_{4}
\end{pmatrix}
$$

其中 $H_1$ 是 $r\times r$ 的。

于是有 $\begin{pmatrix}H_{1} & 0\\H_{3} & 0\end{pmatrix} =\begin{pmatrix}H_{1}^{T} & H_{3}^{T}\\0 & 0\end{pmatrix}$，进而 $H_1=H_1^T$，且 $H_3=0$。

于是 $Q^{T} =P\begin{pmatrix}H_{1} & H_{2}\\0 & H_{4}\end{pmatrix} ,A=P\begin{pmatrix}H_{1}^{T} & 0\\0 & 0\end{pmatrix} P^{T}$。

由比内-柯西公式，

$$
\begin{aligned}
A\begin{pmatrix}
i_{1} ,i_{2} ,\cdots ,i_{r}\\
i_{1} ,i_{2} ,\cdots ,i_{r}
\end{pmatrix} = & \sum _{u_{1} < u_{2} < \cdots < u_{r}} P\begin{pmatrix}
i_{1} ,i_{2} ,\cdots ,i_{r}\\
u_{1} ,u_{2} ,\cdots ,u_{r}
\end{pmatrix}\left(\begin{pmatrix}
H_{1}^{T} & 0\\
0 & 0
\end{pmatrix} P^{T}\right)\begin{pmatrix}
u_{1} ,u_{2} ,\cdots ,u_{r}\\
i_{1} ,i_{2} ,\cdots ,i_{r}
\end{pmatrix}\\
= & \sum _{u_{1} < u_{2} < \cdots < u_{r}} P\begin{pmatrix}
i_{1} ,i_{2} ,\cdots ,i_{r}\\
u_{1} ,u_{2} ,\cdots ,u_{r}
\end{pmatrix}\sum _{v_{1} < v_{2} < \cdots < v_{r}}\begin{pmatrix}
H_{1}^{T} & 0\\
0 & 0
\end{pmatrix}\begin{pmatrix}
u_{1} ,u_{2} ,\cdots ,u_{r}\\
v_{1} ,v_{2} ,\cdots ,v_{r}
\end{pmatrix} P^{T}\begin{pmatrix}
v_{1} ,v_{2} ,\cdots ,v_{r}\\
i_{1} ,i_{2} ,\cdots ,i_{r}
\end{pmatrix}\\
= & \sum _{u_{1} < u_{2} < \cdots < u_{r}} P\begin{pmatrix}
i_{1} ,i_{2} ,\cdots ,i_{r}\\
u_{1} ,u_{2} ,\cdots ,u_{r}
\end{pmatrix}\begin{pmatrix}
H_{1}^{T} & 0\\
0 & 0
\end{pmatrix}\begin{pmatrix}
u_{1} ,u_{2} ,\cdots ,u_{r}\\
1,2,\cdots ,r
\end{pmatrix} P^{T}\begin{pmatrix}
1,2,\cdots ,r\\
i_{1} ,i_{2} ,\cdots ,i_{r}
\end{pmatrix}\\
= & P\begin{pmatrix}
i_{1} ,i_{2} ,\cdots ,i_{r}\\
1,2,\cdots ,r
\end{pmatrix}\begin{pmatrix}
H_{1}^{T} & 0\\
0 & 0
\end{pmatrix}\begin{pmatrix}
1,2,\cdots ,r\\
1,2,\cdots ,r
\end{pmatrix} P^{T}\begin{pmatrix}
1,2,\cdots ,r\\
i_{1} ,i_{2} ,\cdots ,i_{r}
\end{pmatrix}\\
= & P\begin{pmatrix}
i_{1} ,i_{2} ,\cdots ,i_{r}\\
1,2,\cdots ,r
\end{pmatrix} |H_1|P^{T}\begin{pmatrix}
1,2,\cdots ,r\\
i_{1} ,i_{2} ,\cdots ,i_{r}
\end{pmatrix}\\
= & \left| P\begin{pmatrix}
i_{1} ,i_{2} ,\cdots ,i_{r}\\
1,2,\cdots ,r
\end{pmatrix}\right| ^{2} |H_1|
\end{aligned}
$$

因此，$A$ 的所有 $r$ 阶主子式都和 $|H_1|$ 同号。

> 设 $A,B,C$分别是数域 $K$ 上的 $s\times n,p\times m,s\times m$矩阵，证明：
>
> $AX-YB=C$ 有解 $\Leftrightarrow$ $\mathrm{rank}\begin{pmatrix}A & 0 \\ 0 & B\end{pmatrix}=\mathrm{rank}\begin{pmatrix}A & C \\ 0 & B\end{pmatrix}$。

证明 $\Rightarrow$ 是可以直接代入得出。

证明 $\Leftarrow$则需要考虑找到一个初等变换的方式使得两个矩阵相同，而相抵可以提供一种思路，就是将左右都化成一个形式，

因此可以找到 $P_1AQ_1=\begin{pmatrix}I_r & 0 \\ 0 & 0\end{pmatrix},P_2BQ_2=\begin{pmatrix}I_t & 0 \\ 0 & 0\end{pmatrix}$，进而可以找到 $\begin{pmatrix}P_1 & 0 \\ 0 & P_2\end{pmatrix}\begin{pmatrix}A & 0 \\ 0 & B\end{pmatrix}\begin{pmatrix}Q_1 & 0 \\ 0 & Q_2\end{pmatrix} = \begin{pmatrix}I_r & 0 & 0 &  0 \\0 & 0 & 0 & 0 \\0 & 0 & I_t & 0 \\0 & 0 & 0 & 0\\\end{pmatrix}$。

因此对于右边，也只要找到类似的方式变成这个玩意儿即可。

……

> 设 $A,B$ 都是 $n$ 级矩阵，证明：如果 $AB=BA=0$，且 $\mathrm{rank}(A^2)=\mathrm{rank}(A)$，那么
>
> $$
> \mathrm{rank}(A+B)=\mathrm{rank}(A)+\mathrm{rank}(B)
> $$

题目中，$\mathrm{rank}(A^2)=\mathrm{rank}(A)$的运用非常棘手，之后要形成条件反射：

对于 $\mathrm{rank}(X)=\mathrm{rank}(Y)$，实际上是存在一个 $C$，满足 $XC=Y$，在本题中，就像是 $A$的一个*勉强的逆*。

因此本题存在 $C$ 满足，$A^2C=A$，同时，因为 $\mathrm{rank}(A+B)\leqslant\mathrm{rank}(A)+\mathrm{rank}(B)$，故我们只要证明 $\mathrm{rank}(A+B)\geqslant\mathrm{rank}(A)+\mathrm{rank}(B)$。

因此

$$
\begin{pmatrix}
A+B & 0\\
0 & 0
\end{pmatrix}\rightarrow \begin{pmatrix}
A+B & A+B\\
A^{2} & A^{2}
\end{pmatrix}\xrightarrow{\cdot \begin{pmatrix}
I_{n} & -AC\\
 & I_{n}
\end{pmatrix}}\begin{pmatrix}
A+B & B\\
A^{2} & 0
\end{pmatrix}
$$

$\mathrm{rank}(A+B)=\mathrm{rank}(A)+\mathrm{rank}(B)$

故有 $\mathrm{rank}( A+B) =\mathrm{rank}\begin{pmatrix}A+B & B\\A^{2} & 0\end{pmatrix} =\mathrm{rank}\begin{pmatrix}B & A+B\\0 & A^{2}\end{pmatrix} \geqslant \mathrm{rank}( B) +\mathrm{rank}\left( A^{2}\right) =\mathrm{rank}( A) +\mathrm{rank}( B)$。

因此

$$
\mathrm{rank}(A+B)=\mathrm{rank}(A)+\mathrm{rank}(B)
$$

## 矩阵的相似

> 证明：幂等矩阵的秩等于幂等矩阵的迹。

对于 $A^2=A$，令 $A=P\begin{pmatrix}I_{r} & 0\\0 & 0\end{pmatrix} Q$，其中 $P,Q$可逆且 $r$ 为 $A$ 的秩，有

$$
\begin{array}{l}
A^{2} =P\begin{pmatrix}
I_{r} & 0\\
0 & 0
\end{pmatrix} QP\begin{pmatrix}
I_{r} & 0\\
0 & 0
\end{pmatrix} Q=P\begin{pmatrix}
I_{r} & 0\\
0 & 0
\end{pmatrix} Q\Rightarrow 
\begin{pmatrix}
I_{r} & 0\\
0 & 0
\end{pmatrix} QP\begin{pmatrix}
I_{r} & 0\\
0 & 0
\end{pmatrix} =\begin{pmatrix}
I_{r} & 0\\
0 & 0
\end{pmatrix}
\end{array}
$$

令$QP=\begin{pmatrix}
H_{1} & H_{2}\\
H_{3} & H_{4}
\end{pmatrix}$，有 $H_1=I_r$，进而 $Q=\begin{pmatrix}
I_{r} & H_{2}\\
H_{3} & H_{4}
\end{pmatrix} P^{-1}$，得到

$$
A=P\begin{pmatrix}
I_{r} & 0\\
0 & 0
\end{pmatrix}\begin{pmatrix}
I_{r} & H_{2}\\
H_{3} & H_{4}
\end{pmatrix} P^{-1} =P\begin{pmatrix}
I_{r} & H_{2}\\
0 & 0
\end{pmatrix} P^{-1}
$$

可以发现 $A\sim \begin{pmatrix}I_{r} & H_{2}\\0 & 0\end{pmatrix}$，因此 $\mathrm{tr}(A)=\mathrm{tr}\begin{pmatrix}
I_{r} & H_{2}\\
0 & 0
\end{pmatrix}=r$。

实际上可以进一步证明 $A\sim \begin{pmatrix}
I_{r} & 0\\
0 & 0
\end{pmatrix}$，只是我比较懒。

> 证明：如果数域 $K$ 上 2 级矩阵 $A$ 满足 $AB-BA=A$，那么 $A^2=0$。

如果 $A$ 的秩为 $0$，那么 $A=0$ 成立。

如果 $A$ 的秩为 $2$，那么 $A$ 可逆，因此 $B-A^{-1}BA=I$，而相似的矩阵有相同的迹，矛盾。

如果 $A$ 的秩为 $1$，那么令 $A=\begin{pmatrix}x & a\\b & -x\\\end{pmatrix}$，写 $-x$ 是因为 $A$ 的迹为 0，于是可以得到 $x^2+ab=0$，进而 $A^2$ 通过计算得到 0。

> 证明：如果 $A,B,C$ 都是 $n$ 级矩阵，且满足 $AB-BA=C,AC=CA$，那么 $\mathrm{tr}(C^k)=0,\forall k \in \mathbb{Z}\cap(0,+\infty)$。

对于 $\mathrm{tr}(C^1)=\mathrm{tr}(AB)-\mathrm{tr}(BA)=0$。

对于 $k>1$，有 $\mathrm{tr}(C^k)=\mathrm{tr}(C^{k-1}(AB-BA))=\mathrm{tr}(C^{k-1}AB)-\mathrm{tr}(C^{k-1}BA)=\mathrm{tr}(C^{k-1}AB)-\mathrm{tr}(AC^{k-1}B)=\mathrm{tr}(C^{k-1}AB)-\mathrm{tr}(CAC^{k-2}B)=\cdots=\mathrm{tr}(C^{k-1}AB)-\mathrm{tr}(C^{k-1}AB)=0$。

**注意：**$\mathrm{tr}$ 的法则中只写了 $\mathrm{tr}(AB)=\mathrm{tr}(BA)$，也就是只能进行乘法的类似于置换的交换，而不能任意交换！

> 设 $b_1,b_2,\cdots,b_n$ 都是正实数，且 $\sum\limits_{i=1}^n b_i=1$。设 $A=(a_{ij})$ 其中
>
> $$
> a_{ij}=\begin{cases} 1 - b_i, &i=j\\-\sqrt{b_ib_j}, &i\neq j\end{cases}
> $$
>
> 求矩阵 $A$ 的秩；$A$ 能否对角化？若 $A$ 能对角化，写出和 $A$ 相似的对角矩阵。

**方法一（再做的时候想出来的）**：

设矩阵 $B=\begin{pmatrix}\sqrt{b_1} \\ \sqrt{b_2} \\ \vdots \\ \sqrt{b_n}\end{pmatrix}$，则 $A=I-BB^T$，对于 $BB^T$ 通过降幂公式可以求出其特征值为 $-1,0(n-1)$（当然特征向量也可以出来，但是不必要），$A$ 是 $BB^T$ 的一个多项式，于是其特征值为 $0,1(n-1)$，进而其对角矩阵就是 $\mathrm{diag}\{I_{n-1},0\}$，秩为 $n-1$。

**方法二（书上的方法，注意力惊人）**：

可以证明 $A$ 是幂等矩阵，然后幂等矩阵的秩就是迹，于是 $A$ 的秩为 $n-1$，对角矩阵 $\mathrm{diag}\{I_{n-1},0\}$。

## 矩阵的特征值和特征向量

### 注意事项

* 小心计算！
* 注意，对于证明<某种矩阵一定有特征值，并且特征值为……>一定要证明<有特征值>，而不是光说明特征值是什么，因此需要从 $|\lambda I-A|=0$入手。

### 结论

* 设 $A$是数域 $K$上的 $n$级矩阵，证明：若 $A$的秩为 $r$，则 $A$的特征多项式

  $$
  |\lambda I-A|=\lambda^n+b_{n-1}\lambda^{n-1}+\dots + b_{n-r}\lambda^{n-r}
  $$

  其中 $b_{n-k}$等于 $(-1)^k$乘以 $A$ 的所有 $k$ 阶主子式的和$\forall k=1,2,\dots,r$。
* $A$ 的 $n$ 个复根之和为 $A$ 的迹，之积为 $|A|$。
* 如果 $A$ 是一个 $n$ 阶正交矩阵，如果 $|A|=1$ 且 $n$ 为奇数，那么 $1$ 是 $A$ 的一个特征值；如果 $|A|=-1$，那么 $-1$ 是 $A$ 的一个特征值。

### 典型题目

✅TODO✅

* [X] 【几何重数 $\leqslant$ 代数重数】证明
* [X] 例题 7（关于开始犯了的代数重数和几何重数的问题）
* [X] 例题 14
* [X] 练习 8
* [X] 练习 13
* [X] 练习 16
* [X] 练习 18（-> 13）

> 设 $\lambda_1$ 是数域 $K$ 上 $n$ 级矩阵 $A$ 的一个特征值，则 $\lambda_1$ 的几何重数不超过它的代数重数。

思路：相似的矩阵有相似的特征多项式，考虑将矩阵进行转化变成一个和几何重数有关的量，然后比较。

对于 $A$的特征多项式在复数域下进行分解，有 $|\lambda I-A|=(\lambda-\lambda_1)^{l_1}\dots (\lambda-\lambda_k)^{l_k}$。

对于 $\lambda_1$ 的特征向量空间 $U$，取一个基向量，$\alpha_1,\alpha_2,\dots,\alpha_t$，将其扩充成 $K^n$ 上的一个基向量 $\alpha_1,\dots,\alpha_t, \beta_1,\dots, \beta_{n-t}$，令 $P=(\alpha_1,\dots,\alpha_t, \beta_1,\dots, \beta_{n-t})$，有 $P$ 可逆，进而

$$
\begin{aligned}
P^{-1}AP=&P^{-1}A(\alpha_1,\dots,\alpha_t, \beta_1,\dots, \beta_{n-t})\\
=&P^{-1}(\lambda_1\alpha_1,\dots,\lambda_1\alpha_t, A\beta_1,\dots, A\beta_{n-t})\\
=&(\lambda_1\varepsilon_1,\dots,\lambda_t\varepsilon_t,P^{-1}A\beta_1,\cdots, P^{-1}A\beta_{n-t})\\
=&\begin{pmatrix}
\lambda_1I_t & B\\
0 & C\\
\end{pmatrix}
\end{aligned}
$$

而因为相似的矩阵有相似的特征多项式，于是

$$
\begin{aligned}
|\lambda I-A|=&\begin{vmatrix}
(\lambda-\lambda_1)I_t & -B\\
0 & \lambda I_{n-t}-C\\
\end{vmatrix}\\
=&|(\lambda-\lambda_1)I_t||\lambda I_{n-t}-C|\\
=&(\lambda-\lambda_1)^t |\lambda I_{n-t}-C|\\
\end{aligned}
$$

因此，代数重数至少为 $t$，于是$\lambda_1$ 的几何重数不超过它的代数重数。

> 设 $A$ 是数域 $K$ 上的 $n$ 级矩阵，证明：如果 $\lambda_0$ 是 $A$ 的 $l$ 重特征值，那么 $\lambda_0^2$ 是 $A^2$的至少 $l$ 重特征值。

**注意区分代数重数和几何重数！**

在复数域上分解 $A$ 的特征多项式，有 $f(\lambda)=|\lambda I-A|=(\lambda-\lambda_0)^l(\lambda-\lambda_1)^{l_1}\dotsb(\lambda-\lambda_k)^{l_k}$。

考虑 $f(-\lambda)=|-\lambda I-A|=(-1)^n|+\lambda I+A|=(-1)^n(\lambda-\lambda_0)^l(\lambda-\lambda_1)^{l_1}\dotsb(\lambda-\lambda_k)^{l_k}$，

因此 $|\lambda I+A|=(\lambda-\lambda_0)^l(\lambda-\lambda_1)^{l_1}\dotsb(\lambda-\lambda_k)^{l_k}$，有

$$
|\lambda I-A^2|=|\lambda I-A||\lambda I+A|=(\lambda - \lambda_0^2)^l(\lambda - \lambda_1^2)^{l_1}\dotsb(\lambda - \lambda_k^2)^{l_k}
$$

> 复数域上的 $n$ 级矩阵
>
> $$
> A=\begin{pmatrix}
>  & 1 &  &  & \\
>  &  & 1 &  & \\
>  &  &  & \ddots  & \\
>  &  &  &  & 1\\
> -a_{0} & -a_{1} & -a_{2} & \cdots  & -a_{n-1}
> \end{pmatrix}
> $$
>
> 称为 **Frobenius 矩阵**，$n\geqslant 2$。求 $A$的特征多项式和全部特征向量。

$$
f( \lambda ) =|\lambda I-A|=\begin{vmatrix}
\lambda  & -1 &  &  & \\
 & \lambda  & -1 &  & \\
 &  & \lambda  & \ddots  & \\
 &  &  & \ddots  & -1\\
+a_{0} & +a_{1} & +a_{2} & \cdots  & \lambda +a_{n-1}
\end{vmatrix} =\lambda ^{n} +a_{n-1} \lambda ^{n-1} +\cdots +a_{0}
$$

因为在复数域上，所以特征多项式必有 $n$ 个根，设为 $\lambda_1,\dots,\lambda_n$。

对于 $\lambda_i$，有

$$
f(\lambda_i)=\begin{vmatrix}
\lambda_i  & -1 &  &  & \\
 & \lambda_i  & -1 &  & \\
 &  & \lambda_i  & \ddots  & \\
 &  &  & \ddots  & -1\\
+a_{0} & +a_{1} & +a_{2} & \cdots  & \lambda_i +a_{n-1}
\end{vmatrix}
$$

记这个矩阵为 $B$，有 $B\begin{pmatrix}1 & 2 & \cdots  & n-1\\2 & 3 & \cdots  & n\end{pmatrix}\neq0$，存在一个 $n-1$ 阶子式不等于 0，因此，特征向量为：

$$
\eta _{i} =\begin{pmatrix}
B( n,1)\\
B( n,2)\\
\vdots \\
B( n,n)
\end{pmatrix} =\begin{pmatrix}
1\\
\lambda _{i}\\
\vdots \\
\lambda _{i}^{n-1}
\end{pmatrix}
$$

于是 $A$ 的属于 $\lambda_i$的全部特征向量的集合是 $\{k\eta_i|k\in \mathbb{C},k\neq 0\}$。

> 设 $A$是数域 $K$ 上的 $n$级矩阵，$m$ 是任一正整数。证明：如果 $\lambda_0$ 是 $A$的 $l$ 重特征值，那么 $\lambda_0^m$ 是 $A^m$ 的 $l$ 重特征值。

将 $A$ 的特征多项式在复数域上进行分解，有

$$
|\lambda I-A|=(\lambda - \lambda_0)^{l}(\lambda - \lambda_1)^{l_1}\cdots (\lambda - \lambda_k)^{l_k}
$$

令 $\omega=e^{i\frac{2\pi}{m}}$，也就是 $m$ 次单位根，计算 $|\lambda I-\omega^i A|$并将结果相乘，因为 $a^m-b^m=(a-b)(a-\omega b)(a-\omega^2b)\cdots (a-\omega^{m-1} b)$，于是

$$
|\lambda^mI-A|=(\lambda^m - \lambda_0^m)^{l}(\lambda^m - \lambda_1^m)^{l_1}\cdots (\lambda^m - \lambda_k^m)^{l_k}
$$

将 $\lambda^m$ 换成 $\lambda$，有

$$
|\lambda I-A^m|=(\lambda - \lambda_0^m)^{l}(\lambda - \lambda_1^m)^{l_1}\cdots (\lambda - \lambda_k^m)^{l_k}
$$

于是$\lambda_0^m$ 是 $A^m$ 的 $l$ 重特征值。

> 设 $A$ 是数域 $K$ 上的 $n$ 级矩阵，$\lambda_1,\lambda_2,\cdots,\lambda_n$ 是 $A$ 的特征多项式 $|\lambda I-A|$ 在复数域中的全部根（可能相同）。证明：
>
> （1）对于复数域上的任一多项式 $g(x)$ 有
>
> $$
> |g(A)|=g(\lambda_1)g(\lambda_2)\cdots g(\lambda_n)
> $$
>
> （2）对于数域 $K$上任一多项式，有 $f(\lambda_1),f(\lambda_2),\cdots,f(\lambda_n)$ 是矩阵 $f(A)$的特征多项式 $|\lambda I-f(A)|$ 在复数域中的全部根，从而如果 $\lambda_1$ 是 $A$ 的 $l_1$ 重特征值，那么 $f(\lambda_1)$是 $f(A)$ 的至少 $l_1$ 重特征值。

（1）将 $g(x)$ 分解，$g(x)=(x-\mu_1)(x-\mu_2)\cdots(x-\mu_k)$，

则 $|g(A)|=\prod_{i=1}^k |A-\mu_iI|=\prod_{i=1}^k (-1)^n\prod_{j=1}^n (\mu_i-\lambda_j)=\prod_{i=1}^k\prod_{j=1}^n(\lambda_j-\mu_i)$

而 $\prod_{j=1}^n g(\lambda_j)=\prod_{j=1}^n\prod_{i=1}^k (\lambda_j-\mu_i)$。证明完毕。

（2）令 $g(x)=\lambda x^0-f(x)$，则 $|\lambda I - A|=|g(A)|=g(\lambda_1)\cdots g(\lambda_n)=(\lambda-f(\lambda_1))\cdots (\lambda-f(\lambda_n))$，因此有 $f(\lambda_1),f(\lambda_2),\cdots,f(\lambda_n)$ 是矩阵 $f(A)$的特征多项式 $|\lambda I-f(A)|$ 在复数域中的全部根。

> 设 $A$ 是复数域上的 $n$ 级矩阵，$\lambda_1,\lambda_2,\cdots,\lambda_n$ 是 $A$ 的全部特征值，求 $A$ 的伴随矩阵 $A^*$ 的全部特征值。

因为 $AA^*=|A|I$，假设 $\lambda \neq 0$，

$$
\begin{aligned}
|\lambda I-A|&=\left| \frac{\lambda}{|A|}A^*A -A\right|\\
&=(-1)^n|A|\left|\frac{\lambda}{|A|}\left(\frac{|A|}{\lambda}I-A^*\right)\right|

\end{aligned}
$$

因此，如果 $\lambda_i\neq0$，则 $\frac{|A|}{\lambda_i}$ 是 $A^*$ 的特征值。

如果 $\lambda_i=0$，则 $|A|=0$，$0$ 也是 $A^*$ 特征值。

更加具体，不依赖 $|A|$：

如果 $A$ 可逆，那么 $|A|=\lambda_1\cdots\lambda_n$，因此 $\lambda_2\cdots\lambda_n,\lambda_1\lambda_3\cdots\lambda_n,\lambda_1\cdots\lambda_{n-1}$ 是 $A^*$ 全部特征值。

如果 $A$ 不可逆，假设 $\lambda_{n}=0$，而如果 $\mathrm{rank}(A) < n-2$，$A^*=0$，只有 $0$ 是 $n$ 重特征值。如果 $\mathrm{rank}(A)=n-1$，那么 $\mathrm{rank}(A^*)=1$，因此 $0$ 至少是 $n-1$ 重特征值，#TODO#​ 则令 $\mu=\lambda_1\cdots\lambda_{n-1}$ 是 $A^*$ 特征值。

> 设 $A$ 是数域 $K$ 上的 $n$ 级矩阵，$\lambda_1,\lambda_2,\cdots,\lambda_n$ 是 $A$ 的特征多项式的全部复根。令
>
> $$
> G=\begin{pmatrix}A & A^m\\ A^m & A\\\end{pmatrix}
> $$
>
> 求 $G$ 的特征多项式的全部复根。

$$
|\lambda I - G|=|(\lambda I_n - A)^2 - A^{2m}| = |\lambda - A - A^m| |\lambda - A + A^m|
$$

两个都是关于 $A$ 的多项式，根据[前面结论](/post/5-similarlysummary-of-the-matrix-1adajh.html)， $\lambda_i+\lambda_i^m$ 和 $\lambda_i - \lambda_i^m$ 都是这个特征多项式的解，因此全部复根就是 $\lambda_i+\lambda_i^m$ 和 $\lambda_i - \lambda_i^m$。

>  下列矩阵是否可对角化？如果可对角化，求出一个可逆矩阵 $\displaystyle P$ 使得 $\displaystyle P^{-1} AP$ 为对角矩阵。
>
> （1）元素全为 $\displaystyle 1$ 的矩阵 $\displaystyle J$；
>
> （2）$\displaystyle A=aI+bJ,a\neq 0,b\neq 0$。

（1）

$$
\begin{array}{l}
|\lambda I-J|=\begin{vmatrix}
\lambda -1 & -1 & \cdots  & -1\\
-1 & \lambda -1 & \cdots  & -1\\
\vdots  & \vdots  &  & \vdots \\
-1 & -1 & \cdots  & \lambda -1
\end{vmatrix} =\begin{vmatrix}
\lambda -1 & -1 & \cdots  & -1\\
\lambda  & \lambda  & \cdots  & 0\\
\vdots  & \vdots  &  & \vdots \\
\lambda  & 0 & \cdots  & \lambda 
\end{vmatrix} =\begin{vmatrix}
\lambda -n & -1 & \cdots  & -1\\
0 & \lambda  & \cdots  & 0\\
\vdots  & \vdots  &  & \vdots \\
0 & 0 & \cdots  & \lambda 
\end{vmatrix}\\
=\lambda ^{n-1}( \lambda -n)
\end{array}
$$

因此 $\displaystyle J$ 有特征值 $\displaystyle n,1$（$\displaystyle n-1$ 重）。

可以求出其一组线性无关的特征向量为

$$
\begin{pmatrix}
1\\
-1\\
0\\
\vdots \\
0
\end{pmatrix} ,\begin{pmatrix}
1\\
0\\
-1\\
\vdots \\
0
\end{pmatrix} ,\begin{pmatrix}
1\\
0\\
0\\
\vdots \\
-1
\end{pmatrix} ,\begin{pmatrix}
1\\
1\\
1\\
\vdots \\
1
\end{pmatrix}
$$

因此 $P=\begin{pmatrix}1 & 1 & 1 & \cdots  & 1\\1 & -1 & 0 & \cdots  & 0\\1 & 0 & -1 & \cdots  & 0\\\vdots  & \vdots  & \vdots  &  & \vdots \\1 & 0 & 0 & \cdots  & -1\end{pmatrix}$。

（2）

可以发现，$\displaystyle P^{-1} AP=\mathrm{diag}\{a+bn,a,\cdots ,a\}$，因此可以，本小问和上一小问的 $\displaystyle P$ 相同。

## 矩阵可对角化的条件

### 三个考虑方向

* $|\lambda I-A|=0$
* $A\alpha=\lambda_0\alpha$
* $(\lambda I-A)X=0$的解空间

### 常见结论

* 对于复数域上的循环位移矩阵 $C=(\varepsilon_n,\varepsilon_1,\cdots,\varepsilon_{n-1})$ 可以通过

  $$
  P=\begin{pmatrix}
  1 & 1 & 1 & \cdots & 1 \\
  1 & \omega_n^1 & \omega_n^2 &\cdots  & \omega_n^{n-1}\\
  1 & \omega_n^2 & \omega_n^4 &\cdots  & \omega_n^{2(n-1)}\\
  \vdots & \vdots & \vdots & & \vdots \\
  1 & \omega_n^{n-1} & \omega_n^{2(n-1)} &\cdots  & \omega_n^{(n-1)(n-1)}\\
  \end{pmatrix}
  $$

  进行对角化，同时特征值为 $\omega_n^k$。

### 典型题目

> 设 $A$ 是数域 $K$ 上的 $n$ 级矩阵。证明：如果 $K^n$ 中任意非零列向量都是 $A$ 的特征向量，那么 $A$ 一定是数量矩阵。

首先，证明一个结论，如果 $\alpha,\beta$ 是属于 $A$ 的不同特征值的两个特征向量，那么 $\alpha+\beta$ 一定不是 $A$ 的特征向量。……（omission）

然后 $A$ 只有一个特征值，同时 $A$ 有 $n$ 个线性无关的特征向量，取 $\varepsilon_1,\cdots,\varepsilon_n$，有 $(\varepsilon_1,\cdots,\varepsilon_n)^{-1}A(\varepsilon_1,\cdots,\varepsilon_n)=\mathrm{diag}(\lambda,\cdots,\lambda)$，因此 $A$ 是数量矩阵。

> 设 $A,B$ 分别是数域 $K$ 上的 $n$ 级、$m$ 级矩阵，它们分别有 $n$ 个、$m$ 个不同的特征值，设 $f(\lambda)$ 是 $A$ 的特征多项式，且 $f(B)$ 是可逆矩阵。证明：对于任意 $n\times m$ 矩阵 $C$，有 $G=\begin{pmatrix}
> A & C \\ 0 & B\\
> \end{pmatrix}$可对角化。

考虑 $|\lambda I - G| = |\lambda I - A||\lambda I - B|=(\lambda - \lambda_1)\cdots (\lambda - \lambda_n)(\lambda - \mu_1)\cdots (\lambda - \mu_m)$，其中 $\lambda_1,\cdots,\lambda_n$ 互不相同，$\mu_1,\cdots,\mu_m$ 互不相同。

而 $f(\mu_i)$ 也是 $f(B)$ 的特征值，又 $f(B)$ 可逆，因此 $f(\mu_i)\neq 0$，于是 $\mu_i\neq \lambda_j$，于是 $G$ 有 $n+m$ 个互不相同特征值，$G$ 可逆。

> 证明：数域 $\displaystyle K$ 上的对合矩阵一定可以对角化；写出它的相似标准型．

注意：在这里发现了之前学习漏洞！

对于 $\displaystyle A^{2} =I$，如果存在特征值 $\displaystyle \lambda$ 和特征向量 $\displaystyle \alpha$ 使得 $\displaystyle A\alpha =\lambda \alpha$，有

$$
\displaystyle  \begin{array}{c}
		A\alpha &=\lambda \alpha \\
		A^{2} \alpha &=\lambda A\alpha \\
		\alpha &=\lambda ^{2} \alpha \\
		\lambda &=\pm 1
	\end{array}
$$

对于 $\displaystyle \lambda =1$，考虑 $\displaystyle ( I-A) X=0$ 的解空间维数为 $n-\displaystyle \mathrm{rank}( I-A)$．

对于 $\displaystyle \lambda =-1$，考虑 $\displaystyle ( -I-A) X=0$ 的解空间维数为 $n-\displaystyle \mathrm{rank}( I+A)$．

而 ​$(I-A)(I+A)=0\Rightarrow \displaystyle \mathrm{rank}( I-A) +\mathrm{rank}( I+A) \leqslant \mathrm{rank}( 2I) =n\Rightarrow 2n-\displaystyle \mathrm{rank}( I+A)\geqslant n$，因此一定可以将 ​$\displaystyle A$​ 对角化．

**（注意证明！）**

且 $\displaystyle A$ 的相似标准型为 $\displaystyle \mathrm{diag}\{1,\cdots ,1,-1,\cdots ,-1\}$，其中 $\displaystyle 1$ 有 $\displaystyle n - \mathrm{rank}( I-A)$ 个，$\displaystyle -1$ 有 $\displaystyle \mathrm{rank}( I-A)$ 个．

> 求数域 $K$ 上 2 级可逆矩阵 $P$ 组成的集合 $\Omega_1$，$P$ 使得对于数域 $K$ 上任何一个可逆对角矩阵 $\mathrm{diag}\{d_1,d_2\}$ 都有 $P^{-1}\mathrm{diag}\{d_1,d_2\}P$ 为对角矩阵。

$\mathrm{diag}\{d_1,d_2\} \sim P^{-1}\mathrm{diag}\{d_1,d_2\}P$，相似的矩阵有相同的特征值，因此 $P^{-1}\mathrm{diag}\{d_1,d_2\}P=\mathrm{diag}\{d_1,d_2\}$ 或 $\mathrm{diag}\{d_2,d_1\}$，因此

$$
P=\begin{pmatrix}a_1 & 0\\ 0 & a_2\\\end{pmatrix}
$$

或者

$$
P=\begin{pmatrix}0 & a_1\\ a_2 & 0\\\end{pmatrix}
$$

综上，$\Omega_1=\left\{\begin{pmatrix}a_1 & 0\\ 0 & a_2\\\end{pmatrix},\begin{pmatrix}0 & a_1\\ a_2 & 0\\\end{pmatrix}\middle| a_1,a_2\in K, a_1a_2\neq 0\right\}$。

## 实对称矩阵的对角化

### 常见结论

* 如果实矩阵 $A$ 的特征多项式在复数域上的根值都是实数，那么 $A$ **正交相似**于一个上三角矩阵。（要求是实数是因为上三角矩阵也必须在实数域内）
* 任一 $n$ 级复矩阵一定**相似**于一个上三角矩阵。
* 对于特征值 $A\alpha=\lambda\alpha$，因此我们可以有一个**启发式**的套路，考虑 $\alpha^T A\alpha$。

### 典型题目

> 证明：如果 $A$ 是 $s\times n$ 实矩阵，那么 $A^TA$ 的特征值都是非负实数。

$A^TA$ 实对称，那么所有特征值都是实数，不妨假设对于特征值 $\lambda$，其中一个特征向量是 $\alpha$，有 $A^TA\alpha = \lambda\alpha$。

有 $\alpha^TA^TA\alpha=\lambda\alpha^T\alpha$，而 $\alpha\neq 0$，进而 $\lambda = \frac{(A\alpha,A\alpha)  }{(\alpha,\alpha )} \geqslant 0$。

> 证明：任一 $n$ 级复矩阵一定相似于一个上三角矩阵。

考虑归纳法，对于 $n=1$ 显然成立。对于 $n>1$，对于 $n$ 级复矩阵 $A$，一定可以取出一个特征值 $\lambda_1$，有一个属于 $\lambda_1$ 的特征向量 $\alpha_1$，取出一个包含 $\alpha_1$ 的线性无关组， $\alpha_1,\cdots,\alpha_n$，进而令 $T=(\alpha_1,\cdots,\alpha_n)$ 是可逆矩阵。

考虑 $T^{-1}AT=T^{-1}(A\alpha_1,\cdots,A\alpha_n)=(\lambda_1T^{-1}\alpha_1,T^{-1}A\alpha_2,\cdots,T^{-1}A\alpha_n)$，因为 $T^{-1}T=I$，因此

$$
T^{-1}AT=\begin{pmatrix}
\lambda_1 & B\\
0 & C
\end{pmatrix}
$$

$C$ 是 $n-1$ 级复矩阵，那么一定存在可逆矩阵 $D'$ 使得 $D'^{-1}CD'$ 为上三角矩阵 $E$，进而令 $D=\begin{pmatrix}1 & 0\\0 & D'\\\end{pmatrix}$

$$
D^{-1}T^{-1}ATD=\begin{pmatrix}
\lambda_1 & BD'\\
0 & E\\
\end{pmatrix}
$$

因此任一 $n$ 级复矩阵一定相似于上三角矩阵。

**注意：**在复数域上没有所谓“正交”！因此仅仅是相似。

> 设 $A$ 是 $n$ 级实矩阵，证明：如果 $A$ 的特征多项式在复数域中的根都是**非负**实数，且 $A$ 的主对角元都是 $1$，那么 $|A|\leqslant 1$。

因为 $A$ 的特征多项式在复数域中的根都是非负实数，$A$ 正交相似于一个上三角矩阵 $U$，也就是存在正交矩阵 $T$ 使得 $A=T^TUT$。且 $\mathrm{tr}(U)=\mathrm{tr}(A)=n$。

考虑 $A$ 的秩就是 $U$ 的秩，也就是 $U$ 对角线元素之积，令 $U$ 对角线上元素（也就是 $A$ 的特征值）为 $\lambda_1,\lambda_2,\cdots,\lambda_n$，其中 $\lambda_1+\lambda_2+\cdots+\lambda_n=n$。

如果其中有一个是 $0$，那么 $|A|=0$，满足。

否则，这些数全是正数，因此 $\sqrt[n]{\lambda_1 \cdots \lambda_n} \leqslant \frac{\lambda_1+\cdots+\lambda_n}{n}=1,|\lambda_1\cdots\lambda_n|\leqslant 1$。

> 设 $A$ 是 $n$ 级实矩阵，证明：如果 $A$ 的特征多项式在复数域中的根都是实数，且 $A$ 的一阶主子式之和与二阶主子式之和都等于零，那么 $A$ 是幂零矩阵。

因为 $A$ 的特征多项式在复数域中的根都是非负实数，$A$ 正交相似于一个上三角矩阵 $U$，也就是存在正交矩阵 $T$ 使得 $A=T^TUT$。记 $U$ 对角线上元素也就是 $A$ 的特征值为 $\lambda_1,\cdots,\lambda_n$。有 $\lambda_1+\cdots+\lambda_n = 0,\sum_{i < j}\lambda_i\lambda_j = 0$。

进而 $\lambda_1^2+\lambda_2^2+\cdots+\lambda_n^2=(\lambda_1+\cdots+\lambda_n)^2-2\sum_{i<j}\lambda_i\lambda_j = 0$，于是 $\lambda_1=\lambda_2=\cdots=\lambda_n=0$，也就是 $U$ 为一个对角线全是 $0$ 的上三角矩阵，因此 $U^n$ 一定会变成 0 矩阵（证明省略了），进而 $A$ 一定是幂零矩阵。

> 设 $A$ 是 $n$ 级复矩阵，如果 $A^*=A$，则称 $A$ 是 **Hermite 矩阵，**或**自伴矩阵**（其中 $A^*=\overline{A}^T$）。证明：Hermite 矩阵的特征值是实数。

考虑 $A$ 的任一特征值 $\lambda$ 以及任一相应的特征向量 $\alpha$，有 $A\alpha = \lambda\alpha$，同时 $A^{T}=\overline{A}$ 于是有

$$
\overline{\alpha^T}A\alpha = \lambda\overline{\alpha^T}\alpha
$$

$$
\overline{A\alpha}=\overline{\lambda\alpha}\Rightarrow A^{T}\overline{\alpha}=\overline{\lambda\alpha}\Rightarrow \alpha^TA^{T}\overline{\alpha}=\overline{\lambda}\alpha^T\overline{\alpha}\Rightarrow \overline{\alpha^T}A\alpha=\overline{\lambda\alpha^T}\alpha
$$

因此 $(\lambda - \overline{\lambda})\overline{\alpha^T}\alpha=0$，而 $\alpha\neq0,\overline{\alpha^T}\alpha\neq0$，于是 $\lambda = \overline{\lambda}$，因此所有 $\lambda$ 都是实数。

> 证明：正交矩阵 $A$ 如果有两个不同的特征值，那么 $A$ 属于不同特征值的特征向量是正交的。

考虑 $A$ 的两个不同特征值 $\lambda_1,\lambda_2$，分别对应的任意两个特征向量 $\alpha_1,\alpha_2$，有 $A\alpha_1=\lambda_1\alpha_1,A\alpha_2=\lambda_2\alpha_2$，$\alpha_2^TA^T=\lambda_2\alpha_2^T$。

于是 $\alpha_2^T\alpha_1=\lambda_1\lambda_2\alpha_2^T\alpha_1$，如果 $\alpha_2^T\alpha_1\neq0$，那么 $\lambda_1\lambda_2=1$。

又 $A$ 是正交矩阵，对于任意特征值 $\lambda$ 和相应的特征向量 $\alpha$，有 $A\alpha=\lambda\alpha$，$\alpha^T A^TA\alpha=\lambda^2\alpha^T\alpha\Rightarrow \alpha^T\alpha = \lambda^2\alpha^T\alpha\Rightarrow \lambda^2=1$，进而 $\lambda=\pm1$，进而无法找到满足上面条件的不同的 $\lambda_1,\lambda_2$。（**第一次做的时候还没有想到**）

综上可以发现，$A$ 属于不同特征值的特征向量是正交的。

## 其他

### ​#TODO#​

* [ ] 补充题 2（候选）
* [ ] 补充题 3

‍
