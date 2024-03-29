---
title: 如何优雅地获得 ChatGPT 使用权
date: '2024-01-31 19:00:00'
updated: '2024-01-31 19:00:00'
excerpt: >-
  ChatGPT 是一个非常有用的东西，但是因为某种原因在中国大陆地区无法访问。因此这篇文章主要介绍我获取 ChatGPT 中尝试的各种方式。
tags:
  - ChatGPT
  - CS/AI
categories: [技术向]
permalink: /post/how-get-GPT.html
comments: true
---

## 序

ChatGPT 是一个非常有用的东西，但是因为某种原因在中国大陆地区无法访问。因此这篇文章主要介绍我获取 ChatGPT 中尝试的各种方式。

在本文中，默认读者已经翻墙成功。

同时，我认为，ChatGPT 更多地不仅仅是聊天，**我们更应研究相关的深层次技巧**。

### 初等：各种套壳网站

用过一小段这种网站，还算不错

## 初等：官网版 + 充值

### 优点

* 能接触到官网上最新的工具，如 GPTStore，GPTs 等等。
* 可以利用 GPTAPI 版本

### 缺点

* 贵。$20 一月。如果是虚拟信用卡，中途还要一些手续费。
* 麻烦。

### 官网版本账号注册 + 激活 GPT4 API 版本

要求较高。

#### 注册

* 首先全程使用解锁 GPT 的翻墙节点（通常购买套餐前应该会有说明，如果没有就尽量选择美国 🇺🇸 节点）。
* 通过虚拟手机接码平台 [SMS-Activate 是在线接受短信的虚拟号码服务](https://sms-activate.org/cn) 中选择 OpenAI 来注册账号。

#### 充值 激活 GPT4 API 版本

* **激活条件**：充值 $5。
* 使用虚拟信用卡，我第一次使用的是 [FOMEPay](https://www.fomepay.com/) 购买的虚拟信用卡（综合考虑的结果，因为我并不是长期使用虚拟信用卡的人，同时也不想充值大量金额因此愿意支付开卡费用，而事实也证明这是正确的，我用完第一次充进去的钱都不知道要什么时候。如果你想通过 FOMEPay 来获取 GPT，欢迎使用我的[推荐链接](https://gpt.fomepay.com/#/pages/login/index?d=X8EYXZ)）
* 然后按照虚拟信用卡来填写 OpenAI 的付款方式，注意账单地址尽量填写在美国的四个免税州，省点钱。
* 然后就能激活了。

只不过涉及 OpenAI 的步骤都有失败或者卡住概率，需要多次尝试（如果你翻墙节点足够好，那么请忽略）。

然后就能激活了。

#### 使用

* 注册成功就能免费进行 GPT3.5 版本对话。
* 如果想在官网界面和 GPT4 对话，可以购买 Plus，支付 $20 每月。
* 如果仅仅想通过 API 进行付费对话，可以在激活 GPT4 API 后在 PlayGround 测试。
* 当然 GPTAPI 的 token 可以用于各种其他软件，比如 [ChatGPTNextWeb](https://github.com/ChatGPTNextWeb/ChatGPT-Next-Web) 就是一个很好的开源软件。

## 中等：其他网站获取 GPT4

### 优点

* 便宜！
* 按需付费
* 不翻墙？

### 缺点

* 只能利用 API 版本
* 没有 GPTs 和 GPTStore 加持。（不过可以自己开发属于自己的 GPT！）

### 概况

OpenAI 似乎也有代理商，比如可以在 [首页 | OpenAI-SB](https://openai-sb.com/) 和 [CloseAI (closeai-asia.com)](https://www.closeai-asia.com/) 中获得他们本地部署的 GPT 的 token，进而利用软件进行交互。

## 中等：官网版本 + 拼车

### 优点

* 便宜！我看到的是 ￥39 每月，不过因为我和这个销售商没有直接利益关系，同时广告放的位置比较明显，不列出。
* 解决方案成熟，项目开源，有**一定的隐私性保障**。
* 如果你很有钱以及时间，你可以按照项目搞一个然后赚点钱。
* 和官网一致，意味着

### 缺点

* 没有 API 版本支持，不利于研究更多有意思的操作。
* 虽然拼车的人不会看到你说了啥，但是管理员还是看得到的，因此隐私的保障只是片面的。（好消息是可以让网站不保存历史消息记录提升隐私保障）

### 概述

这是我偶尔逛到的一个项目，在这里：[chatpire/chatgpt-web-share: ChatGPT Plus 共享方案](https://github.com/chatpire/chatgpt-web-share)。

## （免费）中等 +：Coze！

Coze 是唯一真神。（我真不是广）

### 优点

* 真正的免费！字节跳动为你买单！整个网站看不到充值按钮！
* 同时我认为字节跳动的背书还是有一定隐私保障的。
* Coze 上也有类似于 GPTStore 商店，解决了无法接触官方 GPTStore 的烦恼。
* 同时提供很多高级操作，比如 Knowledge、GPTVision 插件、WebBrowser 插件，还能提供自己的插件。
* 可以快速发布集成到其他网站上，比如 Discord、Telegram 等等。
* 提供 MultiAgent 模式，只不过我还没用过。
* 总之来说，对于研究 GPT 产品设计非常方便。

### 缺点

* 仍需翻墙，发布集成到的其他网站都是国外常见网站，并不是国内网站。
* <u>暂时</u>​~~不能给你明确的答复~~没有 API 的额外接入（听说在做了），也就意味这不能直接通过该网站在国内进行变现（但是研究 GPT 操作还是一个非常好的网站）。

### 概述

上 coze.com。

日常使用可以把机器人发布到 Discord 上，然后进行对话。
