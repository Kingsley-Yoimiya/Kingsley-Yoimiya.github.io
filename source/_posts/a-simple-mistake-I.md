---
title: 一个典中典错误——不判断一致收敛的结果
date: 2024-6-3 14:37:00
update: 2024-6-3 14:37:00
tags:
   - 数学
   - 数学分析
excerpt: >-
  受伤翘课引发的血案。
categories: [数学向]
permalink: /post/a-simple-mistake-I.html
comments: true
---

## 题目

> 利用幂级数求级数的和（闭式）：
>
> $$
> \begin{equation*}
> \sum _{n=0}^{\infty }\left(\frac{1}{4n+1} +\frac{1}{4n+3} -\frac{1}{2n+2}\right) 
> \end{equation*}
> $$

## 错误解法

　　有一个这样的解法，看起来一点问题也没有，ChatGPT 看了也觉得没问题：

> 记
>
> $$
> \begin{equation}f( x) =\sum _{n=0}^{\infty }\left(\frac{x^{4n+1}}{4n+1} +\frac{x^{4n+3}}{4n+3} -\frac{x^{2n+2}}{2n+2}\right)\end{equation}
> $$
>
> ‍
>
> 则答案就是 $\displaystyle f(1)$。
>
> $$
> \begin{align*}
> f'( x) & =\sum _{n=0}^{\infty } x^{4n} +x^{4n+2} -x^{2n+1}\\
>  & =\frac{1}{1-x^{4}} +\frac{x^{2}}{1-x^{4}} -\frac{x}{1-x^{2}}\\
>  & =\frac{1}{1+x}\\
> f( 1) =\int _{0}^{1} f'( x)\mathrm{d} x & =\int _{0}^{1}\frac{1}{1+x}\mathrm{d} x\\
>  & =\ln( 1+x) | _{0}^{1}\\
>  & =\ln 2
> \end{align*}
> $$

　　问题出在了那里呢？（属于是翘课 + 看书不仔细导致的）其实就在第一步出了错  $f( x) =\sum _{n=0}^{\infty }\left(\frac{x^{4n+1}}{4n+1} +\frac{x^{4n+3}}{4n+3} -\frac{x^{2n+2}}{2n+2}\right)$ 因为 $x$  的次幂不同，根本不能保证连续性、换序求导，于是导致了出错。

## 正确的解法

$$
\begin{equation}f( x) =\sum _{n=0}^{\infty }\left(\frac{1}{4n+1} +\frac{1}{4n+3} -\frac{1}{2n+2}\right)x^{4n+4}\end{equation}\\
$$

$$
\begin{equation}f( x) =\sum _{n=0}^{\infty }\left(\frac{1}{4n+1} -\frac{1}{4n+2} +\frac{1}{4n+3} -\frac{1}{4n+4}+\frac{1}{4n+2} -\frac{1}{4n+4}\right)x^{4n+4}\end{equation}
$$

　　

其收敛半径为 $1$，且当 $x=1$ 时，$f(1)$ 为两个交错级数的和，收敛，于是 $f(x)$ 在 $(-1,1]$​ 内闭一致收敛。

> 其实如果观察到了这一步就已经可以快速出结果了：
>
> $$
> \begin{aligned}
> S&=\lim_{N\to\infty}\sum_{n=1}^N\left(\frac{1}{4n+1} -\frac{1}{4n+2} +\frac{1}{4n+3} -\frac{1}{4n+4}\right)+\left(\frac{1}{4n+2} -\frac{1}{4n+4}\right)\\
> S_N&=\sum_{n=1}^{4N+4}(-1)^{n+1}\frac{1}{n} + \frac{1}{2}\sum_{n=1}^{2N + 2}(-1)^{n+1}\frac{1}{n}\\
> S&=\lim_{N\to\infty}S_N =\sum_{n=1}^{4N+4}(-1)^{n+1}\frac{1}{n} + \frac{1}{2}\sum_{n=1}^{2N + 2}(-1)^{n+1}\frac{1}{n}=\frac{3}{2}\ln2\\
> \end{aligned}
> $$

　　于是有：

$$
\begin{aligned}
f( x) =&\sum _{n=0}^{\infty }\left(\frac{1}{4n+1} +\frac{1}{4n+3} -\frac{1}{2n+2}\right)x^{4n+4}\\
=&x^3\left(-\frac{1}{2}\arctan x +\frac{1}{4}\ln(1+x)-\frac{1}{4}\ln(1-x)\right)+\\
&x\left(-\frac{1}{2}\arctan x + \frac{1}{4}\ln(1+x)-\frac{1}{4}\ln(1-x)\right)+\\
&\frac{1}{2}\ln(1-x^4)
\end{aligned}
$$

　　其中每项都是先求导再换序最后积分得到（需要**一致连续性质**，以及注意 $f(0) = 0$）。

　　而因为 $f(x)$ 在 $(-1,1]$ 一致连续，于是由 Abel 第二引理的推论可以得到（$f(x)$ 在 $(-1,1]$ 连续）：

$$
\begin{aligned}
f(1)=&\lim_{x\to 1^-}f(x)\\
=&\frac{1}{2}\ln 2 + \lim_{x\to 1^-} \left(\frac{1}{2}\ln\frac{1-x^4}{(1-x)^{\frac{x}{2}+\frac{x^3}{2}}}\right)\\
=&\frac{3}{2}\ln 2
\end{aligned}
$$

　　注意，第二步的时候，利用了 $(1-x)^{1-\frac{x}{2}-\frac{x^3}{2}}(x\to 1)=e^{(2t-\frac{3}{2}t^2 + \frac{t^3}{2})\ln t}(t\to0)=1$。
