## Solution to Homework 2

Name: Chen Shen

NetID: cs5236

### 1.

(a) For example, the sales of a product.

(b) Let $x_i$ be the frequency of occurrence of a certain word and $y$ be the sales of the product. Then we have the following linear model

$$
y = \beta_1 x_1 + \beta_2 x_2 + \cdots + \beta_k x_k + \epsilon
$$

(c) Normalized the scores so that they have a common limit.

(d) We can use an array of one-hot coding, such as [score, good, bad, no rating].

(e) Of course the fraction of reviews with the word "good". We need to consider both the reviews with the word "good" and the total number of reviews.

### 2.

(a)

$$
y = \beta_0 + \beta_1 x_1 + \beta_2 x_2 + \epsilon
$$

(b) First, we can have a formula in matrice form
$$
\mathbf{y}=\mathbf{A}\mathbf{\beta}
$$
where
$$
\mathbf{y}=\left[
\begin{matrix}
1 \\
4 \\
3 \\
7
\end{matrix} \right],
\mathbf{A}=\left[
\begin{matrix}
1 &0 &0 \\
1 &0 &1 \\
1 &1 &0 \\
1 &1 &1
\end{matrix} \right].
$$
So we have 
$$
\mathbf{\beta}=\left[
\begin{matrix}
0.75 \\
2.5 \\
3.5
\end{matrix} \right],
$$
i.e. $\beta_0=0.75$, $\beta_1=2.5$, $\beta_2=3.5$.

### 3. 

(a) The vactor $\mathbf{\beta}$ could be as follows. There are $M+N+1$ unknown parameters.
$$
\mathbf{\beta}=[a_1, a_2, \cdots, a_M, b_0, b_1, \cdots, b_N]^\mathrm{T}
$$

(b) The matrix $\mathbf{A}$ and $\mathbf{y}$ could be as follows.
$$
\mathbf{A}=\left[
\begin{matrix}
y_{M-1} &\cdots &y_0 &x_M &\cdots &x_{M-N} \\
y_{M} &\cdots &y_1 &x_{M+1} &\cdots &x_{M-N+1} \\
\vdots &\cdots &\vdots &\vdots &\cdots &\vdots \\
y_{T-2} &\cdots &y_0 &x_M &\cdots &x_{T-N-1}
\end{matrix} \right], \mathbf{y}=\left[
\begin{matrix}
y_M \\
\vdots \\
y_{T-1}
\end{matrix} \right].
$$

(c) First, we can divide the matrix $\mathbf{A}$ into two parts.
$$
\mathbf{A}=\left[
\begin{matrix}
\mathbf{A}_\mathbf{y} &\mathbf{A}_\mathbf{x}
\end{matrix} \right],
$$
where
$$
\mathbf{A}_\mathbf{y}=\left[
\begin{matrix}
y_{M-1} &\cdots &y_0 \\
y_{M} &\cdots &y_1 \\
\vdots &\cdots &\vdots \\
y_{T-2} &\cdots &y_0 
\end{matrix} \right],~
\mathbf{A}_\mathbf{x}=\left[
\begin{matrix}
x_M &\cdots &x_{M-N} \\
x_{M+1} &\cdots &x_{M-N+1} \\
\vdots &\cdots &\vdots \\
x_M &\cdots &x_{T-N-1}
\end{matrix} \right].
$$
So we have 
$$
\begin{aligned}
\frac{1}{T}\mathbf{A}^\mathrm{T}\mathbf{A}
&=\frac{1}{T}\left[
\begin{matrix}
\mathbf{A}_\mathbf{y}^\mathrm{T} \\
\mathbf{A}_\mathbf{x}^\mathrm{T}
\end{matrix} \right] \left[
\begin{matrix}
\mathbf{A}_\mathbf{y} &\mathbf{A}_\mathbf{x}
\end{matrix} \right] \\
&=\left[
\begin{matrix}
\frac{1}{T}\mathbf{A}_\mathbf{y}^\mathrm{T}\mathbf{A}_\mathbf{y} &\frac{1}{T}\mathbf{A}_\mathbf{y}^\mathrm{T}\mathbf{A}_\mathbf{x} \\
\frac{1}{T}\mathbf{A}_\mathbf{x}^\mathrm{T}\mathbf{A}_\mathbf{y} &\frac{1}{T}\mathbf{A}_\mathbf{x}^\mathrm{T}\mathbf{A}_\mathbf{x} \\
\end{matrix} \right]
\end{aligned}
$$
Now focus on a certain element.
$$
\begin{aligned}
\frac{1}{T}(\mathbf{A}_\mathbf{y}^\mathrm{T}\mathbf{A}_\mathbf{y})_{i,j}
&=\sum_{k=1}^{T-M}(\mathbf{A}_\mathbf{y}^\mathrm{T})_{i,k}(\mathbf{A}_\mathbf{y})_{k,j} \\
&=\sum_{k=1}^{T-M}(\mathbf{A}_\mathbf{y})_{k,i}(\mathbf{A}_\mathbf{y})_{k,j} \\
&=\sum_{k=1}^{T-M}y_{M+k-i-1}y_{M+k-j-1} \\
&=\sum_{k=M-i}^{T-i-1}y_{k}y_{k+(i-j)}
\end{aligned}
$$
Since $T \gg N$ and $T \gg M$, it goes like
$$
\frac{1}{T}(\mathbf{A}_\mathbf{y}^\mathrm{T}\mathbf{A}_\mathbf{y})_{i,j} \approx \sum_{k=0}^{T-1}y_{k}y_{k+(i-j)} = R_{yy}(i-j).
$$
Similarly, we have 
$$
\begin{aligned}
&\frac{1}{T}(\mathbf{A}_\mathbf{x}^\mathrm{T}\mathbf{A}_\mathbf{x})_{i,j} \approx \sum_{k=0}^{T-1}x_{k}x_{k+(i-j)} = R_{xx}(i-j), \\
&\frac{1}{T}(\mathbf{A}_\mathbf{y}^\mathrm{T}\mathbf{A}_\mathbf{x})_{i,j} = \frac{1}{T}(\mathbf{A}_\mathbf{x}^\mathrm{T}\mathbf{A}_\mathbf{y})_{i,j} \approx \sum_{k=0}^{T-1}x_{k}y_{k+(i-j)} = R_{xy}(i-j).
\end{aligned}
$$
To $\frac{1}{T}\mathbf{A}^\mathrm{T}\mathbf{y}$, we can take the same steps. First,
$$
\begin{aligned}
\frac{1}{T}\mathbf{A}^\mathrm{T}\mathbf{y}
&=\frac{1}{T}\left[
\begin{matrix}
\mathbf{A}_\mathbf{y}^\mathrm{T} \\
\mathbf{A}_\mathbf{x}^\mathrm{T}
\end{matrix} \right] \mathbf{y} \\
&=\left[
\begin{matrix}
\frac{1}{T}\mathbf{A}_\mathbf{y}^\mathrm{T}\mathbf{y} \\
\frac{1}{T}\mathbf{A}_\mathbf{x}^\mathrm{T}\mathbf{y} \\
\end{matrix} \right].
\end{aligned}
$$
Then concentrate on one element.
$$
\begin{aligned}
\frac{1}{T}(\mathbf{A}_\mathbf{y}^\mathrm{T}\mathbf{y})_{i,1}
&=\sum_{k=1}^{T-M}(\mathbf{A}_\mathbf{y}^\mathrm{T})_{i,k}(\mathbf{y})_{k,1} \\
&=\sum_{k=1}^{T-M}(\mathbf{A}_\mathbf{y})_{k,i}(\mathbf{y})_{k,1} \\
&=\sum_{k=1}^{T-M}y_{M+k-i-1}y_{M+k-1} \\
&=\sum_{k=M-i}^{T-i-1}y_{k}y_{k+i} \\
&\approx \sum_{k=0}^{T-1}y_{k}y_{k+i} \\
&= R_{yy}(i)
\end{aligned}
$$
And also we can get
$$
\begin{aligned}
\frac{1}{T}(\mathbf{A}_\mathbf{x}^\mathrm{T}\mathbf{y})_{i,1}
&\approx \sum_{k=0}^{T-1}x_{k}y_{k+i} \\
&= R_{xy}(i)
\end{aligned}
$$
In conclusion, $\frac{1}{T}\mathbf{A}^\mathrm{T}\mathbf{A}$ and $\frac{1}{T}\mathbf{A}^\mathrm{T}\mathbf{y}$ can be approximately computed from the autocorrelation functions.

### 4.

(a) We can define
$$
\mathbf{A}=\left[
\begin{matrix}
cos(\Omega_1(0)) &\cdots &cos(\Omega_L(0)) &sin(\Omega_1(0)) &\cdots &sin(\Omega_L(0)) \\
cos(\Omega_1(1)) &\cdots &cos(\Omega_L(1)) &sin(\Omega_1(1)) &\cdots &sin(\Omega_L(1)) \\
\vdots &\cdots &\vdots &\vdots &\cdots &\vdots \\
cos(\Omega_1(T-1)) &\cdots &cos(\Omega_L(T-1)) &sin(\Omega_1(T-1)) &\cdots &sin(\Omega_L(T-1))
\end{matrix} \right]
$$
and
$$
\mathbf{x}=\left[
\begin{matrix}
x_0 \\
\vdots \\
x_{T-1}
\end{matrix} \right],
\mathbf{\beta}=\left[
\begin{matrix}
a_1 \\
\vdots \\
a_L \\
b_1 \\
\vdots \\
b_L
\end{matrix} \right].
$$
Then we have $\mathbf{x}\approx \mathbf{A}\mathbf{\beta}$.

(b) No, the model is nonlinear.
