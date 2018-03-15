## Solution to Homework 05

Name: Chen Shen

NetID: cs5236

### 1.

(a) First, let
$$
\mathbf{A}=\left[
\begin{matrix}
1 &x_{11} &\cdots &x_{1d} \\
1 &x_{21} &\cdots &x_{2d} \\
\vdots &\cdots &\cdots &\vdots \\
1 &x_{n1} &\cdots &x_{nd}
\end{matrix} \right].
$$
Then we have $\mathbf{z}=\mathbf{A}\mathbf{w}$, where
$$
z_i=w_0+\sum_{j=1}^dw_jx_{ij}.
$$
So if we let
$$
g(\mathbf{z})=\sum_{i=1}^ng_i(z_i),
$$
where
$$
g_i(z_i)=\left[y_i-\frac{1}{z_i}\right]^2
$$
Then we will have $J(\mathbf{w})=g(\mathbf{A}\mathbf{w})$.

(b) The gradient of $g(\mathbf{z})$ is
$$
\nabla_{\mathbf{z}} g(\mathbf{z})= \left[
\begin{matrix}
g_1'(z_1), &\cdots, &g_n'(z_n)
\end{matrix} \right]^\top,
$$
where 
$$
g_i'(z_i)=-\frac{1}{z_i^2}\left[y_i-(-\frac{1}{z_i})\right]
$$
Based on the forward-backward rule,
$$
\nabla_{\mathbf{w}}J(\mathbf{w})=\mathbf{A}^\top\nabla_{\mathbf{z}} g(\mathbf{z}),
$$
where
$$
\mathbf{z}=\mathbf{A}\mathbf{w}
$$

(c)
$$
\mathbf{w}^{k+1}=\mathbf{w}^k-\alpha\nabla_{\mathbf{w}}f(\mathbf{w}^k)
$$

(d)     

```{.python .numberLines}
n = X.shape[0]
A = np.column.stack((np.ones(n), X))
z = A.dot(w)
yerr = y - 1 / z
J = np.sum(yerr ** 2)

ggrad = -yeer / (z ** 2)
Jgrad = A.T.dot(ggrad)
```

### 2.

(a)
$$
\nabla J(\mathbf{w})=\left[
\begin{matrix}
\frac{\partial J}{\partial w_1} &\frac{\partial J}{\partial w_2}
\end{matrix} \right]^\top
=\left[
\begin{matrix}
b_1w_1 &b_2w_2
\end{matrix} \right]^\top
$$

(b)
$$
\mathbf{w}^*=0
$$

(c)
$$
\mathbf{w}^{k+1}=\mathbf{w}^k-\alpha\nabla J(\mathbf{w}^k)
$$
$$
\Rightarrow wi^{k+1}=wi^k\alpha b_iw_ik=\rho_iw_i^k
$$

(d) In order to obtain $\mathbf{w}^k\rightarrow\mathbf{w}^*$, we should have
$$
\begin{aligned}
&|1-b_i\alpha|<1 \\
\Rightarrow& \alpha < \frac{2}{b_i}
\end{aligned}
$$
where $i=1,2$.

(e)
For $\alpha=2/(b_1+b_2)$, we have
$$
\rho_1=1-b_1\alpha=\frac{b_2-b_1}{b_2+b_1},
\rho_2=1-b_2\alpha=\frac{b_1-b_2}{b_1+b_2}
$$
Let $C=\frac{b_2-b_1}{b_2+b_1}$, then we have $|\rho_i|=C$ $(i=1,2)$.     
Since $K=\frac{b_2}{b_1}$, there is $C=\frac{K-1}{K+1}$.         
Based on the previous problems, $w_i^k=\rho_i^kw_i^0$, i.e. $|w_i^k|=C|w_i^0|$.   
Thus,
$$
||w^k||^2=|w_1^k|^2+|w_2^k|^2=C^{2k}\left[|w_1^0|^2+|w_2^0|^2\right]=C^{2k}||\mathbf{w}^0||^2
$$


### 3.

(a)
$$
z_i=\mathbf{x}_i^\top\mathbf{P}\mathbf{x}_i
=\sum_{j,k}x_{ij}x_{ik}P_{jk}
$$
So
$$
\frac{\partial z_i}{\partial P_{jk}}=x_{ij}x_{ik}
$$
Thus, 
$$
\nabla_\mathbf{p}z_i=\left[x_{ij}x_{ik}\right]=\mathbf{x}_i\mathbf{x}_i^\top
$$

(b)
$$
\nabla_\mathbf{p}J(\mathbf{P})=\nabla_{z_i}J\nabla_\mathbf{p}z_i
=\sum_{i=1}^n\left[\frac{1}{y_i}-\frac{1}{z_i}\right]\mathbf{x}_i\mathbf{x}_i^\top
$$

(c)     

```{.python .numberLines}
n = X.shape[0]
z = np.zeros(n)
for i in range(n):
    z[i] = np.dot(X[i,:], np.dot(P, X[i,:]))

J = np.sum(z/y - np.log(z))
g = 1/y - 1/z

Jgrad = np.zeros((n,n))
for i in range(n):
    xi = X[i,:]
    Jgrad += g[i] * xi[:,None] * xi[None,:]
```

(d)     

```{.python .numberLines}
n = X.shape[0]
z = np.sum(XP*X, axis=1)

J = np.sum(z/y - np.log(z))
g = 1/y - 1/z

GX = g[:,None] * X
Jgrad = np.dot(X.T, GX)
```

### 4.

(a) First, we have
$$
J_1(\mathbf{w}_1)=J(\mathbf{w}_1,\hat{\mathbf{w}}_2)
$$
$$
\begin{aligned}
\frac{\partial J_1}{\partial w_{1j}}
&=\frac{\partial J(\mathbf{w}_1,\hat{\mathbf{w}}_2)}{\partial w_{1j}} \\
&=\left.\frac{\partial J(\mathbf{w}_1,\mathbf{w}_2)}{\partial w_{1j}}\right|_{\mathbf{w}_2=\hat{\mathbf{w}}_2}
+\sum_k \left.\frac{\partial J(\mathbf{w}_1,\mathbf{w}_2)}{\partial w_{2k}}\right|_{\mathbf{w}_2=\hat{\mathbf{w}}_2}\frac{\partial w_{2k}}{\partial w_{1j}}
\end{aligned}
$$
Also we have
$$
\left.\nabla_{\mathbf{w}_2}J(\mathbf{w}_1,\mathbf{w}_2)\right|_{\mathbf{w}_2=\hat{\mathbf{w}}_2}=0
$$
Thus, 
$$
\left.\frac{\partial J(\mathbf{w}_1,\mathbf{w}_2)}{\partial w_{2k}}\right|_{\mathbf{w}_2=\hat{\mathbf{w}}_2}=0
$$
So
$$
\frac{\partial J_1}{\partial w_{1j}}=\left.\frac{\partial J(\mathbf{w}_1,\mathbf{w}_2)}{\partial w_{1j}}\right|_{\mathbf{w}_2=\hat{\mathbf{w}}_2}
$$
In conclusion,
$$
\nabla_{\mathbf{w}_1}J_1(\mathbf{w}_1)=\left.\nabla_{\mathbf{w}_1}J(\mathbf{w}_1,\mathbf{w}_2)\right|_{\mathbf{w}_2=\hat{\mathbf{w}}_2}
$$

(b) In this problem, we can treat $\mathbf{a}$ as a constant.       
Let 
$$
\hat{\mathbf{y}}=\left[
\begin{matrix}
\hat{y}_1 &\cdots &\hat{y}_n 
\end{matrix}\right]^\top,
$$
where
$$
\hat{y}_i=\sum_{j=1}^db_je^{-a_jx_i},
$$
and
$$
\mathbf{A}=\left[
\begin{matrix}
e^{-a_1x_1} &\cdots &e^{-a_dx_1} \\
\vdots &\cdots &\vdots \\
e^{-a_1x_n} &\cdots &e^{-a_dx_n}
\end{matrix} \right].
$$
Also we have $\hat{\mathbf{y}}=\mathbf{A}\mathbf{b}$.   
Thus,
$$
\hat{\mathbf{b}}=(\mathbf{A}^\top\mathbf{A})^{-1}\mathbf{A}^\top\mathbf{y}.
$$

(c)
$$
\nabla_\mathbf{a}J(\mathbf{a}, \mathbf{b})
=\left[
\begin{matrix}
\frac{\partial J(\mathbf{a}, \mathbf{b})}{\partial a_1}
&\cdots
&\frac{\partial J(\mathbf{a}, \mathbf{b})}{\partial a_d}
\end{matrix}
\right]^\top,
$$
where
$$
\frac{\partial J(\mathbf{a}, \mathbf{b})}{\partial a_j}
=\sum_{i=1}^n\frac{\partial(y_i-\hat{y}_i)^2}{\partial a_j}
=-2\sum_{i=1}^n\partial(y_i-\hat{y}_i)\frac{\partial \hat{y}_i}{\partial a_j}
=2\sum_{i=1}^n\partial(y_i-\hat{y}_i)b_jx_ie^{-a_jx_i}
$$.
