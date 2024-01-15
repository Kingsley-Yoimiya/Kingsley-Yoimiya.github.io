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

> 设 {% raw %}$A_{s \times n}${% endraw %}，证明：{% raw %}$A${% endraw %} 的秩为 {% raw %}$r${% endraw %} 的充要条件是存在数域 {% raw %}$K${% endraw %} 上 {% raw %}$s\times r${% endraw %} 列满秩矩阵和 {% raw %}$r\times n${% endraw %} 行满秩矩阵 {% raw %}$C${% endraw %}，使得 {% raw %}$A=BC${% endraw %}。

证明 {% raw %}$\Rightarrow${% endraw %}，考虑可逆 {% raw %}$P,Q${% endraw %}，有 {% raw %}$A=P\begin{pmatrix} I_r &0 \\ 0 & 0\end{pmatrix} Q${% endraw %}，进而表示 {% raw %}$A=\begin{pmatrix}P_1,P_2\end{pmatrix}\begin{pmatrix} I_r &0 \\ 0 & 0\end{pmatrix}\begin{pmatrix} Q_1\\ Q_2\end{pmatrix}${% endraw %}，其中 {% raw %}$P_1${% endraw %} {% raw %}$r${% endraw %}列，{% raw %}$Q_1${% endraw %} {% raw %}$r${% endraw %} 行。

于是 {% raw %}$A=P_1Q_1${% endraw %}。

证明 {% raw %}$\Leftarrow${% endraw %}，有 {% raw %}$r(A)\leqslant r(B)${% endraw %}，因此 {% raw %}$r(A)\leqslant r${% endraw %}。

而同时 {% raw %}$r(A)\geqslant r(B)+r(C)-r${% endraw %}（练习题目，直接构造分块矩阵即可），因此 {% raw %}$r(A)\geqslant r${% endraw %}。于是 {% raw %}$r(A)=r${% endraw %}。

> 设 {% raw %}$A${% endraw %} 为实数域上 {% raw %}$n${% endraw %} 级对称矩阵，且 {% raw %}$A${% endraw %} 的秩为 {% raw %}$r>0${% endraw %}，证明 {% raw %}$A${% endraw %} 的所有非 0 主子式同号。

存在可逆 {% raw %}$P,Q${% endraw %} 满足 {% raw %}$A=P\begin{pmatrix}I_{r} & 0\\0 & 0\end{pmatrix} Q${% endraw %}，同时

{% raw %}$$
A^{T} =Q^{T}\begin{pmatrix}I_{r} & 0\\0 & 0\end{pmatrix} P^{T} =T=P\begin{pmatrix}I_{r} & 0\\0 & 0\end{pmatrix} Q\Rightarrow P^{-1} Q^{T}\begin{pmatrix}I_{r} & 0\\0 & 0\end{pmatrix} =\begin{pmatrix}I_{r} & 0\\0 & 0\end{pmatrix} Q\left( P^{T}\right)^{-1}
$${% endraw %}

令 

{% raw %}$$
\displaystyle P^{-1} Q^{T} =\begin{pmatrix}
H_{1} & H_{2}\\
H_{3} & H_{4}
\end{pmatrix}
$${% endraw %}

其中 {% raw %}$H_1${% endraw %} 是 {% raw %}$r\times r${% endraw %} 的。

于是有 {% raw %}$\begin{pmatrix}H_{1} & 0\\H_{3} & 0\end{pmatrix} =\begin{pmatrix}H_{1}^{T} & H_{3}^{T}\\0 & 0\end{pmatrix}${% endraw %}，进而 {% raw %}$H_1=H_1^T${% endraw %}，且 {% raw %}$H_3=0${% endraw %}。

于是 {% raw %}$Q^{T} =P\begin{pmatrix}H_{1} & H_{2}\\0 & H_{4}\end{pmatrix} ,A=P\begin{pmatrix}H_{1}^{T} & 0\\0 & 0\end{pmatrix} P^{T}${% endraw %}。

由比内-柯西公式，

{% raw %}$$
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
$${% endraw %}

因此，{% raw %}$A${% endraw %} 的所有 {% raw %}$r${% endraw %} 阶主子式都和 {% raw %}$|H_1|${% endraw %} 同号。

> 设 {% raw %}$A,B,C${% endraw %}分别是数域 {% raw %}$K${% endraw %} 上的 {% raw %}$s\times n,p\times m,s\times m${% endraw %}矩阵，证明：
>
> {% raw %}$AX-YB=C${% endraw %} 有解 {% raw %}$\Leftrightarrow${% endraw %} {% raw %}$\mathrm{rank}\begin{pmatrix}A & 0 \\ 0 & B\end{pmatrix}=\mathrm{rank}\begin{pmatrix}A & C \\ 0 & B\end{pmatrix}${% endraw %}。

证明 {% raw %}$\Rightarrow${% endraw %} 是可以直接代入得出。

证明 {% raw %}$\Leftarrow${% endraw %}则需要考虑找到一个初等变换的方式使得两个矩阵相同，而相抵可以提供一种思路，就是将左右都化成一个形式，

因此可以找到 {% raw %}$P_1AQ_1=\begin{pmatrix}I_r & 0 \\ 0 & 0\end{pmatrix},P_2BQ_2=\begin{pmatrix}I_t & 0 \\ 0 & 0\end{pmatrix}${% endraw %}，进而可以找到 {% raw %}$\begin{pmatrix}P_1 & 0 \\ 0 & P_2\end{pmatrix}\begin{pmatrix}A & 0 \\ 0 & B\end{pmatrix}\begin{pmatrix}Q_1 & 0 \\ 0 & Q_2\end{pmatrix} = \begin{pmatrix}I_r & 0 & 0 &  0 \\0 & 0 & 0 & 0 \\0 & 0 & I_t & 0 \\0 & 0 & 0 & 0\\\end{pmatrix}${% endraw %}。

因此对于右边，也只要找到类似的方式变成这个玩意儿即可。

……

> 设 {% raw %}$A,B${% endraw %} 都是 {% raw %}$n${% endraw %} 级矩阵，证明：如果 {% raw %}$AB=BA=0${% endraw %}，且 {% raw %}$\mathrm{rank}(A^2)=\mathrm{rank}(A)${% endraw %}，那么
>
> {% raw %}$$
> \mathrm{rank}(A+B)=\mathrm{rank}(A)+\mathrm{rank}(B)
> $${% endraw %}

题目中，{% raw %}$\mathrm{rank}(A^2)=\mathrm{rank}(A)${% endraw %}的运用非常棘手，之后要形成条件反射：

对于 {% raw %}$\mathrm{rank}(X)=\mathrm{rank}(Y)${% endraw %}，实际上是存在一个 {% raw %}$C${% endraw %}，满足 {% raw %}$XC=Y${% endraw %}，在本题中，就像是 {% raw %}$A${% endraw %}的一个*勉强的逆*。

因此本题存在 {% raw %}$C${% endraw %} 满足，{% raw %}$A^2C=A${% endraw %}，同时，因为 {% raw %}$\mathrm{rank}(A+B)\leqslant\mathrm{rank}(A)+\mathrm{rank}(B)${% endraw %}，故我们只要证明 {% raw %}$\mathrm{rank}(A+B)\geqslant\mathrm{rank}(A)+\mathrm{rank}(B)${% endraw %}。

因此

{% raw %}$$
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
$${% endraw %}

{% raw %}$\mathrm{rank}(A+B)=\mathrm{rank}(A)+\mathrm{rank}(B)${% endraw %}

故有 {% raw %}$\mathrm{rank}( A+B) =\mathrm{rank}\begin{pmatrix}A+B & B\\A^{2} & 0\end{pmatrix} =\mathrm{rank}\begin{pmatrix}B & A+B\\0 & A^{2}\end{pmatrix} \geqslant \mathrm{rank}( B) +\mathrm{rank}\left( A^{2}\right) =\mathrm{rank}( A) +\mathrm{rank}( B)${% endraw %}。

因此

{% raw %}$$
\mathrm{rank}(A+B)=\mathrm{rank}(A)+\mathrm{rank}(B)
$${% endraw %}

## 矩阵的相似

> 证明：幂等矩阵的秩等于幂等矩阵的迹。

对于 {% raw %}$A^2=A${% endraw %}，令 {% raw %}$A=P\begin{pmatrix}I_{r} & 0\\0 & 0\end{pmatrix} Q${% endraw %}，其中 {% raw %}$P,Q${% endraw %}可逆且 {% raw %}$r${% endraw %} 为 {% raw %}$A${% endraw %} 的秩，有

{% raw %}$$
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
$${% endraw %}

令{% raw %}$QP=\begin{pmatrix}
H_{1} & H_{2}\\
H_{3} & H_{4}
\end{pmatrix}${% endraw %}，有 {% raw %}$H_1=I_r${% endraw %}，进而 {% raw %}$Q=\begin{pmatrix}
I_{r} & H_{2}\\
H_{3} & H_{4}
\end{pmatrix} P^{-1}${% endraw %}，得到

{% raw %}$$
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
$${% endraw %}

可以发现 {% raw %}$A\sim \begin{pmatrix}I_{r} & H_{2}\\0 & 0\end{pmatrix}${% endraw %}，因此 {% raw %}$\mathrm{tr}(A)=\mathrm{tr}\begin{pmatrix}
I_{r} & H_{2}\\
0 & 0
\end{pmatrix}=r${% endraw %}。

实际上可以进一步证明 {% raw %}$A\sim \begin{pmatrix}
I_{r} & 0\\
0 & 0
\end{pmatrix}${% endraw %}，只是我比较懒。

> 证明：如果数域 {% raw %}$K${% endraw %} 上 2 级矩阵 {% raw %}$A${% endraw %} 满足 {% raw %}$AB-BA=A${% endraw %}，那么 {% raw %}$A^2=0${% endraw %}。

如果 {% raw %}$A${% endraw %} 的秩为 {% raw %}$0${% endraw %}，那么 {% raw %}$A=0${% endraw %} 成立。

如果 {% raw %}$A${% endraw %} 的秩为 {% raw %}$2${% endraw %}，那么 {% raw %}$A${% endraw %} 可逆，因此 {% raw %}$B-A^{-1}BA=I${% endraw %}，而相似的矩阵有相同的迹，矛盾。

如果 {% raw %}$A${% endraw %} 的秩为 {% raw %}$1${% endraw %}，那么令 {% raw %}$A=\begin{pmatrix}x & a\\b & -x\\\end{pmatrix}${% endraw %}，写 {% raw %}$-x${% endraw %} 是因为 {% raw %}$A${% endraw %} 的迹为 0，于是可以得到 {% raw %}$x^2+ab=0${% endraw %}，进而 {% raw %}$A^2${% endraw %} 通过计算得到 0。

> 证明：如果 {% raw %}$A,B,C${% endraw %} 都是 {% raw %}$n${% endraw %} 级矩阵，且满足 {% raw %}$AB-BA=C,AC=CA${% endraw %}，那么 {% raw %}$\mathrm{tr}(C^k)=0,\forall k \in \mathbb{Z}\cap(0,+\infty)${% endraw %}。

对于 {% raw %}$\mathrm{tr}(C^1)=\mathrm{tr}(AB)-\mathrm{tr}(BA)=0${% endraw %}。

对于 {% raw %}$k>1${% endraw %}，有 {% raw %}$\mathrm{tr}(C^k)=\mathrm{tr}(C^{k-1}(AB-BA))=\mathrm{tr}(C^{k-1}AB)-\mathrm{tr}(C^{k-1}BA)=\mathrm{tr}(C^{k-1}AB)-\mathrm{tr}(AC^{k-1}B)=\mathrm{tr}(C^{k-1}AB)-\mathrm{tr}(CAC^{k-2}B)=\cdots=\mathrm{tr}(C^{k-1}AB)-\mathrm{tr}(C^{k-1}AB)=0${% endraw %}。

**注意：**{% raw %}$\mathrm{tr}${% endraw %} 的法则中只写了 {% raw %}$\mathrm{tr}(AB)=\mathrm{tr}(BA)${% endraw %}，也就是只能进行乘法的类似于置换的交换，而不能任意交换！

> 设 {% raw %}$b_1,b_2,\cdots,b_n${% endraw %} 都是正实数，且 {% raw %}$\sum\limits_{i=1}^n b_i=1${% endraw %}。设 {% raw %}$A=(a_{ij})${% endraw %} 其中
>
> {% raw %}$$
> a_{ij}=\begin{cases} 1 - b_i, &i=j\\-\sqrt{b_ib_j}, &i\neq j\end{cases}
> $${% endraw %}
>
> 求矩阵 {% raw %}$A${% endraw %} 的秩；{% raw %}$A${% endraw %} 能否对角化？若 {% raw %}$A${% endraw %} 能对角化，写出和 {% raw %}$A${% endraw %} 相似的对角矩阵。

**方法一（再做的时候想出来的）**：

设矩阵 {% raw %}$B=\begin{pmatrix}\sqrt{b_1} \\ \sqrt{b_2} \\ \vdots \\ \sqrt{b_n}\end{pmatrix}${% endraw %}，则 {% raw %}$A=I-BB^T${% endraw %}，对于 {% raw %}$BB^T${% endraw %} 通过降幂公式可以求出其特征值为 {% raw %}$-1,0(n-1)${% endraw %}（当然特征向量也可以出来，但是不必要），{% raw %}$A${% endraw %} 是 {% raw %}$BB^T${% endraw %} 的一个多项式，于是其特征值为 {% raw %}$0,1(n-1)${% endraw %}，进而其对角矩阵就是 {% raw %}$\mathrm{diag}\{I_{n-1},0\}${% endraw %}，秩为 {% raw %}$n-1${% endraw %}。

**方法二（书上的方法，注意力惊人）**：

可以证明 {% raw %}$A${% endraw %} 是幂等矩阵，然后幂等矩阵的秩就是迹，于是 {% raw %}$A${% endraw %} 的秩为 {% raw %}$n-1${% endraw %}，对角矩阵 {% raw %}$\mathrm{diag}\{I_{n-1},0\}${% endraw %}。

## 矩阵的特征值和特征向量

### 注意事项

* 小心计算！
* 注意，对于证明<某种矩阵一定有特征值，并且特征值为……>一定要证明<有特征值>，而不是光说明特征值是什么，因此需要从 {% raw %}$|\lambda I-A|=0${% endraw %}入手。

### 结论

* 设 {% raw %}$A${% endraw %}是数域 {% raw %}$K${% endraw %}上的 {% raw %}$n${% endraw %}级矩阵，证明：若 {% raw %}$A${% endraw %}的秩为 {% raw %}$r${% endraw %}，则 {% raw %}$A${% endraw %}的特征多项式

  {% raw %}$$
  |\lambda I-A|=\lambda^n+b_{n-1}\lambda^{n-1}+\dots + b_{n-r}\lambda^{n-r}
  $${% endraw %}

  其中 {% raw %}$b_{n-k}${% endraw %}等于 {% raw %}$(-1)^k${% endraw %}乘以 {% raw %}$A${% endraw %} 的所有 {% raw %}$k${% endraw %} 阶主子式的和{% raw %}$\forall k=1,2,\dots,r${% endraw %}。
* {% raw %}$A${% endraw %} 的 {% raw %}$n${% endraw %} 个复根之和为 {% raw %}$A${% endraw %} 的迹，之积为 {% raw %}$|A|${% endraw %}。
* 如果 {% raw %}$A${% endraw %} 是一个 {% raw %}$n${% endraw %} 阶正交矩阵，如果 {% raw %}$|A|=1${% endraw %} 且 {% raw %}$n${% endraw %} 为奇数，那么 {% raw %}$1${% endraw %} 是 {% raw %}$A${% endraw %} 的一个特征值；如果 {% raw %}$|A|=-1${% endraw %}，那么 {% raw %}$-1${% endraw %} 是 {% raw %}$A${% endraw %} 的一个特征值。

### 典型题目

✅TODO✅

* [X] 【几何重数 {% raw %}$\leqslant${% endraw %} 代数重数】证明
* [X] 例题 7（关于开始犯了的代数重数和几何重数的问题）
* [X] 例题 14
* [X] 练习 8
* [X] 练习 13
* [X] 练习 16
* [X] 练习 18（-> 13）

> 设 {% raw %}$\lambda_1${% endraw %} 是数域 {% raw %}$K${% endraw %} 上 {% raw %}$n${% endraw %} 级矩阵 {% raw %}$A${% endraw %} 的一个特征值，则 {% raw %}$\lambda_1${% endraw %} 的几何重数不超过它的代数重数。

思路：相似的矩阵有相似的特征多项式，考虑将矩阵进行转化变成一个和几何重数有关的量，然后比较。

对于 {% raw %}$A${% endraw %}的特征多项式在复数域下进行分解，有 {% raw %}$|\lambda I-A|=(\lambda-\lambda_1)^{l_1}\dots (\lambda-\lambda_k)^{l_k}${% endraw %}。

对于 {% raw %}$\lambda_1${% endraw %} 的特征向量空间 {% raw %}$U${% endraw %}，取一个基向量，{% raw %}$\alpha_1,\alpha_2,\dots,\alpha_t${% endraw %}，将其扩充成 {% raw %}$K^n${% endraw %} 上的一个基向量 {% raw %}$\alpha_1,\dots,\alpha_t, \beta_1,\dots, \beta_{n-t}${% endraw %}，令 {% raw %}$P=(\alpha_1,\dots,\alpha_t, \beta_1,\dots, \beta_{n-t})${% endraw %}，有 {% raw %}$P${% endraw %} 可逆，进而

{% raw %}$$
\begin{aligned}
P^{-1}AP=&P^{-1}A(\alpha_1,\dots,\alpha_t, \beta_1,\dots, \beta_{n-t})\\
=&P^{-1}(\lambda_1\alpha_1,\dots,\lambda_1\alpha_t, A\beta_1,\dots, A\beta_{n-t})\\
=&(\lambda_1\varepsilon_1,\dots,\lambda_t\varepsilon_t,P^{-1}A\beta_1,\cdots, P^{-1}A\beta_{n-t})\\
=&\begin{pmatrix}
\lambda_1I_t & B\\
0 & C\\
\end{pmatrix}
\end{aligned}
$${% endraw %}

而因为相似的矩阵有相似的特征多项式，于是

{% raw %}$$
\begin{aligned}
|\lambda I-A|=&\begin{vmatrix}
(\lambda-\lambda_1)I_t & -B\\
0 & \lambda I_{n-t}-C\\
\end{vmatrix}\\
=&|(\lambda-\lambda_1)I_t||\lambda I_{n-t}-C|\\
=&(\lambda-\lambda_1)^t |\lambda I_{n-t}-C|\\
\end{aligned}
$${% endraw %}

因此，代数重数至少为 {% raw %}$t${% endraw %}，于是{% raw %}$\lambda_1${% endraw %} 的几何重数不超过它的代数重数。

> 设 {% raw %}$A${% endraw %} 是数域 {% raw %}$K${% endraw %} 上的 {% raw %}$n${% endraw %} 级矩阵，证明：如果 {% raw %}$\lambda_0${% endraw %} 是 {% raw %}$A${% endraw %} 的 {% raw %}$l${% endraw %} 重特征值，那么 {% raw %}$\lambda_0^2${% endraw %} 是 {% raw %}$A^2${% endraw %}的至少 {% raw %}$l${% endraw %} 重特征值。

**注意区分代数重数和几何重数！**

在复数域上分解 {% raw %}$A${% endraw %} 的特征多项式，有 {% raw %}$f(\lambda)=|\lambda I-A|=(\lambda-\lambda_0)^l(\lambda-\lambda_1)^{l_1}\dotsb(\lambda-\lambda_k)^{l_k}${% endraw %}。

考虑 {% raw %}$f(-\lambda)=|-\lambda I-A|=(-1)^n|+\lambda I+A|=(-1)^n(\lambda-\lambda_0)^l(\lambda-\lambda_1)^{l_1}\dotsb(\lambda-\lambda_k)^{l_k}${% endraw %}，

因此 {% raw %}$|\lambda I+A|=(\lambda-\lambda_0)^l(\lambda-\lambda_1)^{l_1}\dotsb(\lambda-\lambda_k)^{l_k}${% endraw %}，有

{% raw %}$$
|\lambda I-A^2|=|\lambda I-A||\lambda I+A|=(\lambda - \lambda_0^2)^l(\lambda - \lambda_1^2)^{l_1}\dotsb(\lambda - \lambda_k^2)^{l_k}
$${% endraw %}

> 复数域上的 {% raw %}$n${% endraw %} 级矩阵
>
> {% raw %}$$
> A=\begin{pmatrix}
>  & 1 &  &  & \\
>  &  & 1 &  & \\
>  &  &  & \ddots  & \\
>  &  &  &  & 1\\
> -a_{0} & -a_{1} & -a_{2} & \cdots  & -a_{n-1}
> \end{pmatrix}
> $${% endraw %}
>
> 称为 **Frobenius 矩阵**，{% raw %}$n\geqslant 2${% endraw %}。求 {% raw %}$A${% endraw %}的特征多项式和全部特征向量。

{% raw %}$$
f( \lambda ) =|\lambda I-A|=\begin{vmatrix}
\lambda  & -1 &  &  & \\
 & \lambda  & -1 &  & \\
 &  & \lambda  & \ddots  & \\
 &  &  & \ddots  & -1\\
+a_{0} & +a_{1} & +a_{2} & \cdots  & \lambda +a_{n-1}
\end{vmatrix} =\lambda ^{n} +a_{n-1} \lambda ^{n-1} +\cdots +a_{0}
$${% endraw %}

因为在复数域上，所以特征多项式必有 {% raw %}$n${% endraw %} 个根，设为 {% raw %}$\lambda_1,\dots,\lambda_n${% endraw %}。

对于 {% raw %}$\lambda_i${% endraw %}，有

{% raw %}$$
f(\lambda_i)=\begin{vmatrix}
\lambda_i  & -1 &  &  & \\
 & \lambda_i  & -1 &  & \\
 &  & \lambda_i  & \ddots  & \\
 &  &  & \ddots  & -1\\
+a_{0} & +a_{1} & +a_{2} & \cdots  & \lambda_i +a_{n-1}
\end{vmatrix}
$${% endraw %}

记这个矩阵为 {% raw %}$B${% endraw %}，有 {% raw %}$B\begin{pmatrix}1 & 2 & \cdots  & n-1\\2 & 3 & \cdots  & n\end{pmatrix}\neq0${% endraw %}，存在一个 {% raw %}$n-1${% endraw %} 阶子式不等于 0，因此，特征向量为：

{% raw %}$$
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
$${% endraw %}

于是 {% raw %}$A${% endraw %} 的属于 {% raw %}$\lambda_i${% endraw %}的全部特征向量的集合是 {% raw %}$\{k\eta_i|k\in \mathbb{C},k\neq 0\}${% endraw %}。

> 设 {% raw %}$A${% endraw %}是数域 {% raw %}$K${% endraw %} 上的 {% raw %}$n${% endraw %}级矩阵，{% raw %}$m${% endraw %} 是任一正整数。证明：如果 {% raw %}$\lambda_0${% endraw %} 是 {% raw %}$A${% endraw %}的 {% raw %}$l${% endraw %} 重特征值，那么 {% raw %}$\lambda_0^m${% endraw %} 是 {% raw %}$A^m${% endraw %} 的 {% raw %}$l${% endraw %} 重特征值。

将 {% raw %}$A${% endraw %} 的特征多项式在复数域上进行分解，有

{% raw %}$$
|\lambda I-A|=(\lambda - \lambda_0)^{l}(\lambda - \lambda_1)^{l_1}\cdots (\lambda - \lambda_k)^{l_k}
$${% endraw %}

令 {% raw %}$\omega=e^{i\frac{2\pi}{m}}${% endraw %}，也就是 {% raw %}$m${% endraw %} 次单位根，计算 {% raw %}$|\lambda I-\omega^i A|${% endraw %}并将结果相乘，因为 {% raw %}$a^m-b^m=(a-b)(a-\omega b)(a-\omega^2b)\cdots (a-\omega^{m-1} b)${% endraw %}，于是

{% raw %}$$
|\lambda^mI-A|=(\lambda^m - \lambda_0^m)^{l}(\lambda^m - \lambda_1^m)^{l_1}\cdots (\lambda^m - \lambda_k^m)^{l_k}
$${% endraw %}

将 {% raw %}$\lambda^m${% endraw %} 换成 {% raw %}$\lambda${% endraw %}，有

{% raw %}$$
|\lambda I-A^m|=(\lambda - \lambda_0^m)^{l}(\lambda - \lambda_1^m)^{l_1}\cdots (\lambda - \lambda_k^m)^{l_k}
$${% endraw %}

于是{% raw %}$\lambda_0^m${% endraw %} 是 {% raw %}$A^m${% endraw %} 的 {% raw %}$l${% endraw %} 重特征值。

> 设 {% raw %}$A${% endraw %} 是数域 {% raw %}$K${% endraw %} 上的 {% raw %}$n${% endraw %} 级矩阵，{% raw %}$\lambda_1,\lambda_2,\cdots,\lambda_n${% endraw %} 是 {% raw %}$A${% endraw %} 的特征多项式 {% raw %}$|\lambda I-A|${% endraw %} 在复数域中的全部根（可能相同）。证明：
>
> （1）对于复数域上的任一多项式 {% raw %}$g(x)${% endraw %} 有
>
> {% raw %}$$
> |g(A)|=g(\lambda_1)g(\lambda_2)\cdots g(\lambda_n)
> $${% endraw %}
>
> （2）对于数域 {% raw %}$K${% endraw %}上任一多项式，有 {% raw %}$f(\lambda_1),f(\lambda_2),\cdots,f(\lambda_n)${% endraw %} 是矩阵 {% raw %}$f(A)${% endraw %}的特征多项式 {% raw %}$|\lambda I-f(A)|${% endraw %} 在复数域中的全部根，从而如果 {% raw %}$\lambda_1${% endraw %} 是 {% raw %}$A${% endraw %} 的 {% raw %}$l_1${% endraw %} 重特征值，那么 {% raw %}$f(\lambda_1)${% endraw %}是 {% raw %}$f(A)${% endraw %} 的至少 {% raw %}$l_1${% endraw %} 重特征值。

（1）将 {% raw %}$g(x)${% endraw %} 分解，{% raw %}$g(x)=(x-\mu_1)(x-\mu_2)\cdots(x-\mu_k)${% endraw %}，

则 {% raw %}$|g(A)|=\prod_{i=1}^k |A-\mu_iI|=\prod_{i=1}^k (-1)^n\prod_{j=1}^n (\mu_i-\lambda_j)=\prod_{i=1}^k\prod_{j=1}^n(\lambda_j-\mu_i)${% endraw %}

而 {% raw %}$\prod_{j=1}^n g(\lambda_j)=\prod_{j=1}^n\prod_{i=1}^k (\lambda_j-\mu_i)${% endraw %}。证明完毕。

（2）令 {% raw %}$g(x)=\lambda x^0-f(x)${% endraw %}，则 {% raw %}$|\lambda I - A|=|g(A)|=g(\lambda_1)\cdots g(\lambda_n)=(\lambda-f(\lambda_1))\cdots (\lambda-f(\lambda_n))${% endraw %}，因此有 {% raw %}$f(\lambda_1),f(\lambda_2),\cdots,f(\lambda_n)${% endraw %} 是矩阵 {% raw %}$f(A)${% endraw %}的特征多项式 {% raw %}$|\lambda I-f(A)|${% endraw %} 在复数域中的全部根。

> 设 {% raw %}$A${% endraw %} 是复数域上的 {% raw %}$n${% endraw %} 级矩阵，{% raw %}$\lambda_1,\lambda_2,\cdots,\lambda_n${% endraw %} 是 {% raw %}$A${% endraw %} 的全部特征值，求 {% raw %}$A${% endraw %} 的伴随矩阵 {% raw %}$A^*${% endraw %} 的全部特征值。

因为 {% raw %}$AA^*=|A|I${% endraw %}，假设 {% raw %}$\lambda \neq 0${% endraw %}，

{% raw %}$$
\begin{aligned}
|\lambda I-A|&=\left| \frac{\lambda}{|A|}A^*A -A\right|\\
&=(-1)^n|A|\left|\frac{\lambda}{|A|}\left(\frac{|A|}{\lambda}I-A^*\right)\right|

\end{aligned}
$${% endraw %}

因此，如果 {% raw %}$\lambda_i\neq0${% endraw %}，则 {% raw %}$\frac{|A|}{\lambda_i}${% endraw %} 是 {% raw %}$A^*${% endraw %} 的特征值。

如果 {% raw %}$\lambda_i=0${% endraw %}，则 {% raw %}$|A|=0${% endraw %}，{% raw %}$0${% endraw %} 也是 {% raw %}$A^*${% endraw %} 特征值。

更加具体，不依赖 {% raw %}$|A|${% endraw %}：

如果 {% raw %}$A${% endraw %} 可逆，那么 {% raw %}$|A|=\lambda_1\cdots\lambda_n${% endraw %}，因此 {% raw %}$\lambda_2\cdots\lambda_n,\lambda_1\lambda_3\cdots\lambda_n,\lambda_1\cdots\lambda_{n-1}${% endraw %} 是 {% raw %}$A^*${% endraw %} 全部特征值。

如果 {% raw %}$A${% endraw %} 不可逆，假设 {% raw %}$\lambda_{n}=0${% endraw %}，而如果 {% raw %}$\mathrm{rank}(A) < n-2${% endraw %}，{% raw %}$A^*=0${% endraw %}，只有 {% raw %}$0${% endraw %} 是 {% raw %}$n${% endraw %} 重特征值。如果 {% raw %}$\mathrm{rank}(A)=n-1${% endraw %}，那么 {% raw %}$\mathrm{rank}(A^*)=1${% endraw %}，因此 {% raw %}$0${% endraw %} 至少是 {% raw %}$n-1${% endraw %} 重特征值，#TODO#​ 则令 {% raw %}$\mu=\lambda_1\cdots\lambda_{n-1}${% endraw %} 是 {% raw %}$A^*${% endraw %} 特征值。

> 设 {% raw %}$A${% endraw %} 是数域 {% raw %}$K${% endraw %} 上的 {% raw %}$n${% endraw %} 级矩阵，{% raw %}$\lambda_1,\lambda_2,\cdots,\lambda_n${% endraw %} 是 {% raw %}$A${% endraw %} 的特征多项式的全部复根。令
>
> {% raw %}$$
> G=\begin{pmatrix}A & A^m\\ A^m & A\\\end{pmatrix}
> $${% endraw %}
>
> 求 {% raw %}$G${% endraw %} 的特征多项式的全部复根。

{% raw %}$$
|\lambda I - G|=|(\lambda I_n - A)^2 - A^{2m}| = |\lambda - A - A^m| |\lambda - A + A^m|
$${% endraw %}

两个都是关于 {% raw %}$A${% endraw %} 的多项式，根据[前面结论](/post/5-similarlysummary-of-the-matrix-1adajh.html)， {% raw %}$\lambda_i+\lambda_i^m${% endraw %} 和 {% raw %}$\lambda_i - \lambda_i^m${% endraw %} 都是这个特征多项式的解，因此全部复根就是 {% raw %}$\lambda_i+\lambda_i^m${% endraw %} 和 {% raw %}$\lambda_i - \lambda_i^m${% endraw %}。

>  下列矩阵是否可对角化？如果可对角化，求出一个可逆矩阵 {% raw %}$\displaystyle P${% endraw %} 使得 {% raw %}$\displaystyle P^{-1} AP${% endraw %} 为对角矩阵。
>
> （1）元素全为 {% raw %}$\displaystyle 1${% endraw %} 的矩阵 {% raw %}$\displaystyle J${% endraw %}；
>
> （2）{% raw %}$\displaystyle A=aI+bJ,a\neq 0,b\neq 0${% endraw %}。

（1）

{% raw %}$$
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
$${% endraw %}

因此 {% raw %}$\displaystyle J${% endraw %} 有特征值 {% raw %}$\displaystyle n,1${% endraw %}（{% raw %}$\displaystyle n-1${% endraw %} 重）。

可以求出其一组线性无关的特征向量为

{% raw %}$$
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
$${% endraw %}

因此 {% raw %}$P=\begin{pmatrix}1 & 1 & 1 & \cdots  & 1\\1 & -1 & 0 & \cdots  & 0\\1 & 0 & -1 & \cdots  & 0\\\vdots  & \vdots  & \vdots  &  & \vdots \\1 & 0 & 0 & \cdots  & -1\end{pmatrix}${% endraw %}。

（2）

可以发现，{% raw %}$\displaystyle P^{-1} AP=\mathrm{diag}\{a+bn,a,\cdots ,a\}${% endraw %}，因此可以，本小问和上一小问的 {% raw %}$\displaystyle P${% endraw %} 相同。

## 矩阵可对角化的条件

### 三个考虑方向

* {% raw %}$|\lambda I-A|=0${% endraw %}
* {% raw %}$A\alpha=\lambda_0\alpha${% endraw %}
* {% raw %}$(\lambda I-A)X=0${% endraw %}的解空间

### 常见结论

* 对于复数域上的循环位移矩阵 {% raw %}$C=(\varepsilon_n,\varepsilon_1,\cdots,\varepsilon_{n-1})${% endraw %} 可以通过

  {% raw %}$$
  P=\begin{pmatrix}
  1 & 1 & 1 & \cdots & 1 \\
  1 & \omega_n^1 & \omega_n^2 &\cdots  & \omega_n^{n-1}\\
  1 & \omega_n^2 & \omega_n^4 &\cdots  & \omega_n^{2(n-1)}\\
  \vdots & \vdots & \vdots & & \vdots \\
  1 & \omega_n^{n-1} & \omega_n^{2(n-1)} &\cdots  & \omega_n^{(n-1)(n-1)}\\
  \end{pmatrix}
  $${% endraw %}

  进行对角化，同时特征值为 {% raw %}$\omega_n^k${% endraw %}。

### 典型题目

> 设 {% raw %}$A${% endraw %} 是数域 {% raw %}$K${% endraw %} 上的 {% raw %}$n${% endraw %} 级矩阵。证明：如果 {% raw %}$K^n${% endraw %} 中任意非零列向量都是 {% raw %}$A${% endraw %} 的特征向量，那么 {% raw %}$A${% endraw %} 一定是数量矩阵。

首先，证明一个结论，如果 {% raw %}$\alpha,\beta${% endraw %} 是属于 {% raw %}$A${% endraw %} 的不同特征值的两个特征向量，那么 {% raw %}$\alpha+\beta${% endraw %} 一定不是 {% raw %}$A${% endraw %} 的特征向量。……（omission）

然后 {% raw %}$A${% endraw %} 只有一个特征值，同时 {% raw %}$A${% endraw %} 有 {% raw %}$n${% endraw %} 个线性无关的特征向量，取 {% raw %}$\varepsilon_1,\cdots,\varepsilon_n${% endraw %}，有 {% raw %}$(\varepsilon_1,\cdots,\varepsilon_n)^{-1}A(\varepsilon_1,\cdots,\varepsilon_n)=\mathrm{diag}(\lambda,\cdots,\lambda)${% endraw %}，因此 {% raw %}$A${% endraw %} 是数量矩阵。

> 设 {% raw %}$A,B${% endraw %} 分别是数域 {% raw %}$K${% endraw %} 上的 {% raw %}$n${% endraw %} 级、{% raw %}$m${% endraw %} 级矩阵，它们分别有 {% raw %}$n${% endraw %} 个、{% raw %}$m${% endraw %} 个不同的特征值，设 {% raw %}$f(\lambda)${% endraw %} 是 {% raw %}$A${% endraw %} 的特征多项式，且 {% raw %}$f(B)${% endraw %} 是可逆矩阵。证明：对于任意 {% raw %}$n\times m${% endraw %} 矩阵 {% raw %}$C${% endraw %}，有 {% raw %}$G=\begin{pmatrix}
> A & C \\ 0 & B\\
> \end{pmatrix}${% endraw %}可对角化。

考虑 {% raw %}$|\lambda I - G| = |\lambda I - A||\lambda I - B|=(\lambda - \lambda_1)\cdots (\lambda - \lambda_n)(\lambda - \mu_1)\cdots (\lambda - \mu_m)${% endraw %}，其中 {% raw %}$\lambda_1,\cdots,\lambda_n${% endraw %} 互不相同，{% raw %}$\mu_1,\cdots,\mu_m${% endraw %} 互不相同。

而 {% raw %}$f(\mu_i)${% endraw %} 也是 {% raw %}$f(B)${% endraw %} 的特征值，又 {% raw %}$f(B)${% endraw %} 可逆，因此 {% raw %}$f(\mu_i)\neq 0${% endraw %}，于是 {% raw %}$\mu_i\neq \lambda_j${% endraw %}，于是 {% raw %}$G${% endraw %} 有 {% raw %}$n+m${% endraw %} 个互不相同特征值，{% raw %}$G${% endraw %} 可逆。

> 证明：数域 {% raw %}$\displaystyle K${% endraw %} 上的对合矩阵一定可以对角化；写出它的相似标准型．

注意：在这里发现了之前学习漏洞！

对于 {% raw %}$\displaystyle A^{2} =I${% endraw %}，如果存在特征值 {% raw %}$\displaystyle \lambda${% endraw %} 和特征向量 {% raw %}$\displaystyle \alpha${% endraw %} 使得 {% raw %}$\displaystyle A\alpha =\lambda \alpha${% endraw %}，有

{% raw %}$$
\displaystyle  \begin{array}{c}
		A\alpha &=\lambda \alpha \\
		A^{2} \alpha &=\lambda A\alpha \\
		\alpha &=\lambda ^{2} \alpha \\
		\lambda &=\pm 1
	\end{array}
$${% endraw %}

对于 {% raw %}$\displaystyle \lambda =1${% endraw %}，考虑 {% raw %}$\displaystyle ( I-A) X=0${% endraw %} 的解空间维数为 {% raw %}$n-\displaystyle \mathrm{rank}( I-A)${% endraw %}．

对于 {% raw %}$\displaystyle \lambda =-1${% endraw %}，考虑 {% raw %}$\displaystyle ( -I-A) X=0${% endraw %} 的解空间维数为 {% raw %}$n-\displaystyle \mathrm{rank}( I+A)${% endraw %}．

而 ​{% raw %}$(I-A)(I+A)=0\Rightarrow \displaystyle \mathrm{rank}( I-A) +\mathrm{rank}( I+A) \leqslant \mathrm{rank}( 2I) =n\Rightarrow 2n-\displaystyle \mathrm{rank}( I+A)\geqslant n${% endraw %}，因此一定可以将 ​{% raw %}$\displaystyle A${% endraw %}​ 对角化．

**（注意证明！）**

且 {% raw %}$\displaystyle A${% endraw %} 的相似标准型为 {% raw %}$\displaystyle \mathrm{diag}\{1,\cdots ,1,-1,\cdots ,-1\}${% endraw %}，其中 {% raw %}$\displaystyle 1${% endraw %} 有 {% raw %}$\displaystyle n - \mathrm{rank}( I-A)${% endraw %} 个，{% raw %}$\displaystyle -1${% endraw %} 有 {% raw %}$\displaystyle \mathrm{rank}( I-A)${% endraw %} 个．

> 求数域 {% raw %}$K${% endraw %} 上 2 级可逆矩阵 {% raw %}$P${% endraw %} 组成的集合 {% raw %}$\Omega_1${% endraw %}，{% raw %}$P${% endraw %} 使得对于数域 {% raw %}$K${% endraw %} 上任何一个可逆对角矩阵 {% raw %}$\mathrm{diag}\{d_1,d_2\}${% endraw %} 都有 {% raw %}$P^{-1}\mathrm{diag}\{d_1,d_2\}P${% endraw %} 为对角矩阵。

{% raw %}$\mathrm{diag}\{d_1,d_2\} \sim P^{-1}\mathrm{diag}\{d_1,d_2\}P${% endraw %}，相似的矩阵有相同的特征值，因此 {% raw %}$P^{-1}\mathrm{diag}\{d_1,d_2\}P=\mathrm{diag}\{d_1,d_2\}${% endraw %} 或 {% raw %}$\mathrm{diag}\{d_2,d_1\}${% endraw %}，因此

{% raw %}$$
P=\begin{pmatrix}a_1 & 0\\ 0 & a_2\\\end{pmatrix}
$${% endraw %}

或者

{% raw %}$$
P=\begin{pmatrix}0 & a_1\\ a_2 & 0\\\end{pmatrix}
$${% endraw %}

综上，{% raw %}$\Omega_1=\left\{\begin{pmatrix}a_1 & 0\\ 0 & a_2\\\end{pmatrix},\begin{pmatrix}0 & a_1\\ a_2 & 0\\\end{pmatrix}\middle| a_1,a_2\in K, a_1a_2\neq 0\right\}${% endraw %}。

## 实对称矩阵的对角化

### 常见结论

* 如果实矩阵 {% raw %}$A${% endraw %} 的特征多项式在复数域上的根值都是实数，那么 {% raw %}$A${% endraw %} **正交相似**于一个上三角矩阵。（要求是实数是因为上三角矩阵也必须在实数域内）
* 任一 {% raw %}$n${% endraw %} 级复矩阵一定**相似**于一个上三角矩阵。
* 对于特征值 {% raw %}$A\alpha=\lambda\alpha${% endraw %}，因此我们可以有一个**启发式**的套路，考虑 {% raw %}$\alpha^T A\alpha${% endraw %}。

### 典型题目

> 证明：如果 {% raw %}$A${% endraw %} 是 {% raw %}$s\times n${% endraw %} 实矩阵，那么 {% raw %}$A^TA${% endraw %} 的特征值都是非负实数。

{% raw %}$A^TA${% endraw %} 实对称，那么所有特征值都是实数，不妨假设对于特征值 {% raw %}$\lambda${% endraw %}，其中一个特征向量是 {% raw %}$\alpha${% endraw %}，有 {% raw %}$A^TA\alpha = \lambda\alpha${% endraw %}。

有 {% raw %}$\alpha^TA^TA\alpha=\lambda\alpha^T\alpha${% endraw %}，而 {% raw %}$\alpha\neq 0${% endraw %}，进而 {% raw %}$\lambda = \frac{(A\alpha,A\alpha)  }{(\alpha,\alpha )} \geqslant 0${% endraw %}。

> 证明：任一 {% raw %}$n${% endraw %} 级复矩阵一定相似于一个上三角矩阵。

考虑归纳法，对于 {% raw %}$n=1${% endraw %} 显然成立。对于 {% raw %}$n>1${% endraw %}，对于 {% raw %}$n${% endraw %} 级复矩阵 {% raw %}$A${% endraw %}，一定可以取出一个特征值 {% raw %}$\lambda_1${% endraw %}，有一个属于 {% raw %}$\lambda_1${% endraw %} 的特征向量 {% raw %}$\alpha_1${% endraw %}，取出一个包含 {% raw %}$\alpha_1${% endraw %} 的线性无关组， {% raw %}$\alpha_1,\cdots,\alpha_n${% endraw %}，进而令 {% raw %}$T=(\alpha_1,\cdots,\alpha_n)${% endraw %} 是可逆矩阵。

考虑 {% raw %}$T^{-1}AT=T^{-1}(A\alpha_1,\cdots,A\alpha_n)=(\lambda_1T^{-1}\alpha_1,T^{-1}A\alpha_2,\cdots,T^{-1}A\alpha_n)${% endraw %}，因为 {% raw %}$T^{-1}T=I${% endraw %}，因此

{% raw %}$$
T^{-1}AT=\begin{pmatrix}
\lambda_1 & B\\
0 & C
\end{pmatrix}
$${% endraw %}

{% raw %}$C${% endraw %} 是 {% raw %}$n-1${% endraw %} 级复矩阵，那么一定存在可逆矩阵 {% raw %}$D'${% endraw %} 使得 {% raw %}$D'^{-1}CD'${% endraw %} 为上三角矩阵 {% raw %}$E${% endraw %}，进而令 {% raw %}$D=\begin{pmatrix}1 & 0\\0 & D'\\\end{pmatrix}${% endraw %}

{% raw %}$$
D^{-1}T^{-1}ATD=\begin{pmatrix}
\lambda_1 & BD'\\
0 & E\\
\end{pmatrix}
$${% endraw %}

因此任一 {% raw %}$n${% endraw %} 级复矩阵一定相似于上三角矩阵。

**注意：**在复数域上没有所谓“正交”！因此仅仅是相似。

> 设 {% raw %}$A${% endraw %} 是 {% raw %}$n${% endraw %} 级实矩阵，证明：如果 {% raw %}$A${% endraw %} 的特征多项式在复数域中的根都是**非负**实数，且 {% raw %}$A${% endraw %} 的主对角元都是 {% raw %}$1${% endraw %}，那么 {% raw %}$|A|\leqslant 1${% endraw %}。

因为 {% raw %}$A${% endraw %} 的特征多项式在复数域中的根都是非负实数，{% raw %}$A${% endraw %} 正交相似于一个上三角矩阵 {% raw %}$U${% endraw %}，也就是存在正交矩阵 {% raw %}$T${% endraw %} 使得 {% raw %}$A=T^TUT${% endraw %}。且 {% raw %}$\mathrm{tr}(U)=\mathrm{tr}(A)=n${% endraw %}。

考虑 {% raw %}$A${% endraw %} 的秩就是 {% raw %}$U${% endraw %} 的秩，也就是 {% raw %}$U${% endraw %} 对角线元素之积，令 {% raw %}$U${% endraw %} 对角线上元素（也就是 {% raw %}$A${% endraw %} 的特征值）为 {% raw %}$\lambda_1,\lambda_2,\cdots,\lambda_n${% endraw %}，其中 {% raw %}$\lambda_1+\lambda_2+\cdots+\lambda_n=n${% endraw %}。

如果其中有一个是 {% raw %}$0${% endraw %}，那么 {% raw %}$|A|=0${% endraw %}，满足。

否则，这些数全是正数，因此 {% raw %}$\sqrt[n]{\lambda_1 \cdots \lambda_n} \leqslant \frac{\lambda_1+\cdots+\lambda_n}{n}=1,|\lambda_1\cdots\lambda_n|\leqslant 1${% endraw %}。

> 设 {% raw %}$A${% endraw %} 是 {% raw %}$n${% endraw %} 级实矩阵，证明：如果 {% raw %}$A${% endraw %} 的特征多项式在复数域中的根都是实数，且 {% raw %}$A${% endraw %} 的一阶主子式之和与二阶主子式之和都等于零，那么 {% raw %}$A${% endraw %} 是幂零矩阵。

因为 {% raw %}$A${% endraw %} 的特征多项式在复数域中的根都是非负实数，{% raw %}$A${% endraw %} 正交相似于一个上三角矩阵 {% raw %}$U${% endraw %}，也就是存在正交矩阵 {% raw %}$T${% endraw %} 使得 {% raw %}$A=T^TUT${% endraw %}。记 {% raw %}$U${% endraw %} 对角线上元素也就是 {% raw %}$A${% endraw %} 的特征值为 {% raw %}$\lambda_1,\cdots,\lambda_n${% endraw %}。有 {% raw %}$\lambda_1+\cdots+\lambda_n = 0,\sum_{i < j}\lambda_i\lambda_j = 0${% endraw %}。

进而 {% raw %}$\lambda_1^2+\lambda_2^2+\cdots+\lambda_n^2=(\lambda_1+\cdots+\lambda_n)^2-2\sum_{i<j}\lambda_i\lambda_j = 0${% endraw %}，于是 {% raw %}$\lambda_1=\lambda_2=\cdots=\lambda_n=0${% endraw %}，也就是 {% raw %}$U${% endraw %} 为一个对角线全是 {% raw %}$0${% endraw %} 的上三角矩阵，因此 {% raw %}$U^n${% endraw %} 一定会变成 0 矩阵（证明省略了），进而 {% raw %}$A${% endraw %} 一定是幂零矩阵。

> 设 {% raw %}$A${% endraw %} 是 {% raw %}$n${% endraw %} 级复矩阵，如果 {% raw %}$A^*=A${% endraw %}，则称 {% raw %}$A${% endraw %} 是 **Hermite 矩阵，**或**自伴矩阵**（其中 {% raw %}$A^*=\overline{A}^T${% endraw %}）。证明：Hermite 矩阵的特征值是实数。

考虑 {% raw %}$A${% endraw %} 的任一特征值 {% raw %}$\lambda${% endraw %} 以及任一相应的特征向量 {% raw %}$\alpha${% endraw %}，有 {% raw %}$A\alpha = \lambda\alpha${% endraw %}，同时 {% raw %}$A^{T}=\overline{A}${% endraw %} 于是有

{% raw %}$$
\overline{\alpha^T}A\alpha = \lambda\overline{\alpha^T}\alpha
$${% endraw %}

{% raw %}$$
\overline{A\alpha}=\overline{\lambda\alpha}\Rightarrow A^{T}\overline{\alpha}=\overline{\lambda\alpha}\Rightarrow \alpha^TA^{T}\overline{\alpha}=\overline{\lambda}\alpha^T\overline{\alpha}\Rightarrow \overline{\alpha^T}A\alpha=\overline{\lambda\alpha^T}\alpha
$${% endraw %}

因此 {% raw %}$(\lambda - \overline{\lambda})\overline{\alpha^T}\alpha=0${% endraw %}，而 {% raw %}$\alpha\neq0,\overline{\alpha^T}\alpha\neq0${% endraw %}，于是 {% raw %}$\lambda = \overline{\lambda}${% endraw %}，因此所有 {% raw %}$\lambda${% endraw %} 都是实数。

> 证明：正交矩阵 {% raw %}$A${% endraw %} 如果有两个不同的特征值，那么 {% raw %}$A${% endraw %} 属于不同特征值的特征向量是正交的。

考虑 {% raw %}$A${% endraw %} 的两个不同特征值 {% raw %}$\lambda_1,\lambda_2${% endraw %}，分别对应的任意两个特征向量 {% raw %}$\alpha_1,\alpha_2${% endraw %}，有 {% raw %}$A\alpha_1=\lambda_1\alpha_1,A\alpha_2=\lambda_2\alpha_2${% endraw %}，{% raw %}$\alpha_2^TA^T=\lambda_2\alpha_2^T${% endraw %}。

于是 {% raw %}$\alpha_2^T\alpha_1=\lambda_1\lambda_2\alpha_2^T\alpha_1${% endraw %}，如果 {% raw %}$\alpha_2^T\alpha_1\neq0${% endraw %}，那么 {% raw %}$\lambda_1\lambda_2=1${% endraw %}。

又 {% raw %}$A${% endraw %} 是正交矩阵，对于任意特征值 {% raw %}$\lambda${% endraw %} 和相应的特征向量 {% raw %}$\alpha${% endraw %}，有 {% raw %}$A\alpha=\lambda\alpha${% endraw %}，{% raw %}$\alpha^T A^TA\alpha=\lambda^2\alpha^T\alpha\Rightarrow \alpha^T\alpha = \lambda^2\alpha^T\alpha\Rightarrow \lambda^2=1${% endraw %}，进而 {% raw %}$\lambda=\pm1${% endraw %}，进而无法找到满足上面条件的不同的 {% raw %}$\lambda_1,\lambda_2${% endraw %}。（**第一次做的时候还没有想到**）

综上可以发现，{% raw %}$A${% endraw %} 属于不同特征值的特征向量是正交的。

## 其他

### ​#TODO#​

* [ ] 补充题 2（候选）
* [ ] 补充题 3

‍
