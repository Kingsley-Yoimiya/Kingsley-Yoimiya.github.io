---
title: Hello World
---

> 设 $A_{s \times n}$，证明：$A$ 的秩为 $r$ 的充要条件是存在数域 $K$ 上 $s\times r$ 列满秩矩阵和 $r\times n$ 行满秩矩阵 $C$，使得 $A=BC$。

证明 $\Rightarrow$，考虑可逆 $P,Q$，有 $A=P\begin{pmatrix} I_r &0 \\ 0 & 0\end{pmatrix} Q$，进而表示 $A=\begin{pmatrix}P_1,P_2\end{pmatrix}\begin{pmatrix} I_r &0 \\ 0 & 0\end{pmatrix}\begin{pmatrix} Q_1\\ Q_2\end{pmatrix}$，其中 $P_1$ $r$列，$Q_1$ $r$ 行。

Welcome to [Hexo](https://hexo.io/)! This is your very first post. Check [documentation](https://hexo.io/docs/) for more info. If you get any problems when using Hexo, you can find the answer in [troubleshooting](https://hexo.io/docs/troubleshooting.html) or you can ask me on [GitHub](https://github.com/hexojs/hexo/issues).

## Quick Start

### Create a new post

``` bash
$ hexo new "My New Post"
```

More info: [Writing](https://hexo.io/docs/writing.html)

### Run server

``` bash
$ hexo server
```

More info: [Server](https://hexo.io/docs/server.html)

### Generate static files

``` bash
$ hexo generate
```

More info: [Generating](https://hexo.io/docs/generating.html)

### Deploy to remote sites

``` bash
$ hexo deploy
```

More info: [Deployment](https://hexo.io/docs/one-command-deployment.html)
