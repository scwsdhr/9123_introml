## Solution to Homework 1

Name: Chen Shen

NetID: cs5236

### 1.

(a) For example, GPA.

(b) It is discrete-valued.

(c) For instance, the students' GPA in high school and the rank of their high schools.

(d) Yes, a linear model is reasonable. Besides, there should be a positive correlation.

### 2.

(a) The sample means are

$$
\bar{x} = \frac{1}{5}\sum_{i=1}^5 x_i = 2
$$

$$
\bar{y} = \frac{1}{5}\sum_{i=1}^5 y_i = 6
$$

(b) The sample variances and co-variances are

$$
s_x^2 = \frac{1}{5}\sum_{i=1}^5 (x_i-\bar{x})^2 = 2
$$

$$
s_y^2 = \frac{1}{5}\sum_{i=1}^5 (y_i-\bar{y})^2 = 37.2
$$

$$
s_{xy} = \frac{1}{5}\sum_{i=1}^5 (x_i-\bar{x})(y_i-\bar{y}) = 8
$$

(c) The least squares parameters are

$$
\beta_1 = \frac{s_{xy}}{s_x^2} = 4
$$

$$
\beta_0 = \bar{y} - \beta_1\bar{x} = -2
$$

(d) The predicted value at $x=2.5$ is

$$
\hat{y} = \beta_0 + \beta_1 x |_{x=2.5} = -2 + 4 \cdot 2.5 = 8
$$

### 3.

(a) In the following fomula, $z_0$ and $\alpha$ appear linearly.

$$
\ln(z(t)) = \ln(z_0e^{-\alpha t}) = \ln z_0 - \alpha t
$$

(b) Let $y = \ln(z(t))$, $\beta_0 = \ln z_0$, $\beta_1 = -\alpha$ and $x = t$. Then we can rewrite the fomula as 

$$
y = \beta_0 + \beta_1 x
$$

where

$$
\bar{x} = \frac{1}{N}\sum_{i=1}^N x_i,~
\bar{y} = \frac{1}{N}\sum_{i=1}^N y_i
$$

$$
s_x^2 = \frac{1}{N}\sum_{i=1}^N (x_i-\bar{x})^2,~
s_y^2 = \frac{1}{N}\sum_{i=1}^N (y_i-\bar{y})^2
$$

$$
s_{xy} = \frac{1}{N}\sum_{i=1}^N (x_i-\bar{x})(y_i-\bar{y})
$$

$$
\beta_1 = \frac{s_{xy}}{s_x^2},~
\beta_0 = \bar{y} - \beta_1\bar{x}
$$

(c) The code could be

    ```{.python .numberLines}
    # Define x and y
    x = t
    y = np.log(z)

    # Compute variance and covariance
    sxx = np.var(x)
    sxy = np.cov(np.append(x, x.mean()), np.append(y, y.mean()))[0][1]

    # Compute the least squares parameters
    b1 = sxy / sxx
    b0 = y.mean() - b1 * x.mean()

    # Compute alpha and z0 in the original fomula
    alpha = -b1
    z0 = exp(b0)
    ```

### 4.

(a) The cost function is 

$$
\mathrm{RSS}(\beta) = \sum_{i=1}^N(y_i-\beta x_i)^2
$$

(b) The $\beta$ should be

$$
\begin{aligned}
&\frac{\partial\mathrm{RSS}(\beta)}{\partial\beta}=\sum_{i=1}^N2(y_i-\beta x_i)(-x_i)=0 \\
&\Longrightarrow -\sum_{i=1}^Nx_iy_i + \beta\sum_{i=1}^Nx_i^2 = 0 \\
&\Longrightarrow \beta = \frac{\sum\limits_{i=1}^Nx_iy_i}{\sum\limits_{i=1}^Nx_i^2}
\end{aligned}
$$
