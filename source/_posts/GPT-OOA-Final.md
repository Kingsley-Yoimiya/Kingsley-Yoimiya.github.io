---
title: 软工实验班 OOA 分析终稿
date: '2024-04-09 23:26:00'
updated: '2024-04-09 23:26:00'
excerpt: >-
    软工实验班 OOA 分析终稿
tags:
   - CS/AI
   - ChatGPT
   - CS/Software
categories: [技术向]
permalink: /post/GPT-OOA-Final.html
comments: true
---

## 更新情况总结

* 增强了顺序图和状态图、活动图、类图的关联。
* 为了保证强关联，已经强制要求 GPT 在后面的图中使用顺序图中已有的函数、对象，并且保证不会出现新的内容。
* 已经进行人工核对，应该是后面图中出现的内容在顺序图已经出现了。
* 对于顺序图进行了细小的调整，”植识通应用“ $\to$ ”主界面“。

## 顺序图绘制

### 用户注册

![](../assets/net-img-bPJFQXH14CRlynJDdbQ8B-118lw17FHWr7lRKraR-y_GtREBHo-oofgJGOG8sQ2ug22YgE0XBvEPJTx2xftERCquB9DJIErNl_w-gjhTjeuQbqkHPFulPpoZof7bcqKv_Kse9Ra5q_XeK7uzFZlPNnxCpjyV3u9a0e9f2RlC0AYMziUYU353MWCZRfsXZ-20240409232148-749u6j1.svg)​

### 用户登录

![](../assets/net-img-ZPFDYjH058NtzHHbLXdG5t0X8-CFWhePSN-jN6OAwoTKLRfnwSfMT5OsCZ22piO1bTwfq8WlOvBsBQoaE-rD3DhRM-TyvznSiky3k51enIw5OzJ8DJZFyZYJGkPW0gzVNrIphnmyBpowtbDIVJfV_JYfvoz_lJrF6iaKbR0Q3uL3D7rjVReily-9LjaZQ-20240409232149-5hvy5kr.svg)​

### 植物生理指标预测

![](../assets/net-img-XLJTQjH05BwVfnXpjRtm1RoG5dz0H2WjFi2O79hGoSmmCr7gdOAu_YY2zaBGOaNQlV2c2ElY-ZYRP7qBvoSi9o6mDnDoplVppPn9TerbsbOb9zTi3YNGacb3bAiLQQ6OiBJzD6kcloapj3AWUwrajLYsfs__VVsU-3vJQjX-lVhx3I4gnINB3bCD8FhGv-20240409232150-dcx5n9a.svg)​

### 植物养护建议

![](../assets/net-img-ZTAnIWCn60VmFKyHExLWjquEKb7eMbhf7YuVNk0kEPDSYs_GGLoqWw0E8jYfuABGFi_TwLkOYvOavmsEN_BTB_ylkQ7IHEeyJT21ZY45d1AfK6RMMCGomZMkxjRbyWCJXNC5CjZgLBlRykcXU5jLBzjgTVtr-Dof6oMeFD7JI0Bmy8FovhLOlXVtQziN2-20240409232151-8ed6ip6.svg)​

### 查询历史记录

![](../assets/net-img-fPJFQXD17CVlynHZJobKl7kG1aDH40y9UXztVvY5oKwScMs83n0MCLMe4GgrM2dOWvJgGQ7Yuyp6leNJsTdixdGdAoINpUvllf_V_zaLad2PZ2Yw8uSm0ZmYNA2n_XO5qPZ44Yy_d6VfBqm4JWJmccbB7SpKknz_BoxLdyLoyVRwqvUjcuF3I4Z6fuE00-20240409232152-w31gl78.svg)​

### 分享结果

![](../assets/net-img-ZPD1IiD058RtSugngmhr0YwaKElMrfnWI5zD8Cd4cHUb5v0k50Lr8rgfAq4GeOXeGI_JDFGMpgGONqWLLqFf_ttplpUagL4eJCA0hQ478V1GACrYeT1t_LX4oBFBX_dmbGlD4msgz5Sj7HxFH-VPz68-kbcCNnQtzpKRLA2J03jY7ohnsVjZTdNo7TIUK-20240409232153-nvl6h06.svg)​

### *发起比赛或挑战(视情况进行选择性开发)

![](../assets/net-img-TPBFIiD04CRl-nHhJodK5_0WbVGgbBOlC4t6Pc7_XDs9fI_WgQ0U12yYYcSHUjA2RnE2Rs6QfKtQfeUGXVdcDzz-itr7O2bJafrHWWgv0kjO2fP495BGn8lFj-BXBdzyvk0un4helNB7rukdvT_BUsUd6O96UI1ShOlrQoLn2qUe3ieVl_do9_zUvVTVb-20240409232154-d5gtp4z.svg)​

### 活动图（最初版，preview）

![](../assets/net-img-ZLJTZj905BwVfnXxQS8BU67s0RprodX1GcLDW3NGZHU6XCIaMrPMbjZLtO08XcXH0mP3gDIVb-dyz2sSzc1dsccZlI3qV3yptvpJEUfOrRPrscoWMzQnsJHnizhke0Ut7-9AvIuE_O1T3QAtxn4IFCkK1VmCOV50rM2kHvqTdNnYDm7vUMNWQWVVRpLEw-20240409232155-mccnajb.svg)​

## 状态图

### 控制器

![](../assets/net-img-XPJ1RjD054NtynLUsYZz0HQeKHO52QGgbTW0Yv7zIaOuup8pfYgh1cWmfGgH888AsYebKCJ2eGXQr0ZwC_7O_Wjcb4Hs4YjTFIMwzxnxtqHPvW8puTTT98XmmP2jaoWuY_Q_nRjdShiHXzsutKJethK7njBI3MDusPMDVlfzB-atKFw3STsuYrtYO05LU-20240409232155-j4ngr0e.svg)​

### 结果展示界面

![](../assets/net-img-SoWkIImgAStDuIh9BCb9LNY-U_ApUNEURfpwVCckvrDxNivTzBnhsxE6nkVh5ZwVqCR55QqLgw2hQwVmRCO-e0g8QYvaZeALGd16VdbGQd5fJacnHX64rep90udwfS8byk1CJIvK0n36FstT_QnhoTFTkrwiMmSrrpcnADKnfImpELKZ4KnfSc6g1Hi1T-20240409232156-now9q3c.svg)​

### 主界面

![](../assets/net-img-bLH1QnD15BxFhzZZhXYyUv0MYrHG4MjFwc7CFCt2P2RCpbhggL8JaxHgGL8KQzj8j1IaLf5IhUsloSni_eKxcKMsBYRiPMVtuttVzxxtXfs991OohbCaGqd16nwVcDxwwCD7tTbNttgcUwHNdfc3ljbe8NJlmWElKhdYgRFcQAMZr_PLToTPFKNe7y2xx-20240409232157-zkwt3a5.svg)

## 活动图

![](../assets/net-img-lLPVJzfG57_lfxZnIH_CtY6PVXMJuMp6q0ZB7XOJc5AAWh89J0UA68QwpHQ7cxDL_38zvzv-Yrqu3ciBT5cMtGTJ-_lnEt_ExroOJwOMLbElNiQLb9gAnnXOPLu-nRJjtExYfGsRfr3hiLdMVwbVELRBiTvZ8SFjSqoVm8qbEkkACj1G8b0o9PyKeego8-20240409232158-8i3h27t.svg)

## 类图 1

![](../assets/net-img-bLTVJnj747-_Jt6FLvM8bpxnK0L1eQX9Yt38-_QysAUSxzozDH6D8kLFS5m21eau3I8XCQM9rIG6chIqTXE-Z7TjVulEUVrdnqiiuC5hPdxpPtupimkN8quOpsLyYtlSfxQeFMu-hiWxzSR7xUPnNUn-iYpN9r5an-B2YNtBkjsJoBVxhTDYixJUVhuFS-20240409232159-fwoznxs.svg)​

## 类图-2

![](../assets/net-img-bLTFRnj55B_xKynnepetJdj0ZH8I8bgmugRtOVV57h6UCRFZL04X0H8X2cs2b5gYeaIaGY9ImQHK0ceJ-cKyw_0jcDtDUFpMQxhfmLFD_Dvltf_tUxEv7IigLQyJrHHJ4H0zV3nvV9vyFXfVdanUZFJt_v1beh--JFeN-lXG__gT_l9Sxt-b1wzgjI2YS-20240409232200-n8saydi.svg)​

## 类图 3

![](../assets/net-img-fLRDRkCs4BxhANYKqUJMamx56adJ1jrW0tktFS-AOvaeHQf3oa5QzDrN52KFPD8EdEp1sipFD_yp_EGyaEzRNNZbDOfrrsbLWrVMY2y79D1Qt6bmJjmhQ0XQSIiUUbC70IV0IB7rbb2AEsiy6k-AeXx5_q9TsnQtDI4QyL_n_ypOOAESfz74aIk6Vp-vl-20240409232201-u88b7jo.svg)​

## 具体过程

#### 1 用于顺序图生成

> 你是一个软件系统设计师，你要根据我的信息、要求，给出该流程我所需的 UML 图片对应 PlantUML 的代码。
>
> 1. 对于顺序图，你需要：
>
>     1. 考虑各个部分，比如 user,欢迎界面,注册界面,控制器,服务端,用户信息,主界面。
>     2. 同时给出 PlantUML 交互信息对应的具体内容（必须是函数），比如 用户点击，就可以在上面有函数 `ClickReg()`​。
>     3. 注意交互信息中箭头上具体内容中必须是英文同时符合编程习惯的命名，而各个部分名称必须是中文。
> 2. 对于状态图，你需要：
>
>     1. 尽可能清晰地给出各个模块
> 3. 对于活动图，你需要考虑清楚多个模块。

更多信息已在之前展示，不再赘述。

#### 2 用于状态图、活动图、类图生成

> ## ChatGPT:
>
> 你是一名软件设计工程师，你要根据提供的信息（比如顺序图），绘制状态图、活动图、类图，用输出 UML 图对应的 PlantUML 语言。
>
> 对于状态图，你需要：
>
> * **明确对象的生命周期**：确保你的状态图覆盖了对象从创建到销毁的整个生命周期。
> * **精确定义事件和条件**：转换的触发事件和条件应该是明确且无歧义的。
> * **考虑异常情况**：不要忽略那些可能导致状态异常变化的情况，确保状态图也能反映系统在非理想条件下的表现。
> * **使用PlantUML特性来提升表达**：利用PlantUML提供的语法和特性，如隐藏的转换、并发状态等，来更准确和高效地表达状态转换逻辑。
>
> 对于活动图，你需要：
>
> * 明确目标： 开始绘制活动图之前，首先明确目标。活动图旨在展示系统的动态行为，特别是业务流程或操作的顺序。确定你要表达的主要流程或行为。
> * 识别活动和参与者： 确定哪些是主要的活动和参与者。活动是由系统或参与者执行的操作步骤，而参与者则是与这些活动交互的个体或系统。
> * 使用标准符号： 确保使用UML标准的符号，如圆角矩形表示活动，菱形表示决策/分支点，箭头表示控制流，以及泳道来区分不同参与者的责任范围。
> * 简化流程： 尽可能地简化流程。避免过度复杂的活动图，这可能会导致理解上的难度。如果某个过程非常复杂，考虑将其分解为多个子过程。
>
> 对于类图，你要：
>
> * **一致性检查**：定期回顾你的类图和状态图，确保两者在方法命名和类职责方面保持一致。
> * **简洁明了**：在方法命名时使用简洁、描述性的名称，避免使用过于笼统或模糊的词语。
> * **反映行为**：方法名称应该反映它执行的具体行为或操作，使其一看就知所指。
>
> ## 用户:
>
> 以控制器为中心画状态图，注意详略选择，同时要在箭头上标注转换的函数，和顺序图中函数一致。  
> 删除待命这个状态，或者将待命放在图片中心。  
> 注意函数名和顺序图中函数名一致，顺序图没有出现的操作也不能出现，适当精简，只显示和成功状态有关的函数。  
> 给出状态图标题。  
> 箭头上的转换的函数和顺序图一致的同时，每个节点的名称必须为中文。
>
> ---
>
> 以结果展示界面为中心，绘制状态图，和之前要求类似。  
> 注意函数名和顺序图中函数名一致，顺序图没有出现的操作也不能出现，适当精简，只显示和成功状态有关的函数。
>
> ---
>
> 以主界面为中心生成类似的状态图。
>
> ---
>
> 拓展一层
>
> ---
>
> 很好，注意 ShowNewResults 函数不存在，使用 ShowResults 替代
>
> ---
>
> UpdateHistoryView 后直接返回历史记录界面
>
> ---
>
> 删除记录和更新历史记录合并，使得状态图更清晰明了
>
> ---
>
> 生成整个应用的活动图，注意层次。
>
> ---
>
> 登录注册单独分一层，并且注册登录时用户交互的前置条件。
>
> ---
>
> 同时用户交互应该是持续不断地，你要注意一个系统处理完后要回到应该在的界面
>
> ---
>
> 好的，生成整个应用的类图，包含所有在顺序图中出现的类、函数，注意精简，不能出现顺序图中没有出现的内容。
>
> ---
>
> 删除用户，每个类要不仅给出函数，还要给出存储内容（英文变量名），同时箭头上写明函数
>
> ---
>
> 类图上，每个节点都用英文名

‍
