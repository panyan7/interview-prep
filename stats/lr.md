# Linear Regression

## Assumptions

## Least-Squares Estimate

Given $X \in \mathbb{R}^{n \times d}$ and $y \in \R^n$, find $\beta = \arg\min_{\beta \in \R^d} \|X\beta - y\|^2$.

If the features of $X$ are linearly independent, meaning that $X$ has rank $d$, then the closed form formula for $\hat{\beta}$ is
$$
\hat{\beta} = (X^\top X)^{-1}X^\top y.
$$
For Ridge regression, the objective is $\beta = \arg\min_{\beta \in \R^d} \|X\beta-y\|^2 + \lambda \|\beta\|^2$, and the closed form formula is
$$
\hat{\beta}^{\rm ridge} = (X^\top X + \lambda I)^{-1} X^\top y = X^\top (XX^\top + \lambda I)^{-1} y.
$$

Least-squares is the maximum likelihood estimator if we assume the errors follow a Gaussian distribution.

## Maximum Likelihood Estimation

Assume that the error terms are $\varepsilon \sim \mathcal{N}(X\beta, \sigma^2 I)$, we have
$$
\mathcal{L}(\beta; Y) = \frac{1}{\sqrt{2\pi}^n \sigma^n} \exp\left(-\frac{1}{2\sigma^2}(Y-X\beta)^\top (Y - X\beta)\right).
$$
So
$$
\log \mathcal{L}(\beta; Y) = -\frac{n}{2}\log(2\pi) - n \log \sigma - \frac{1}{2\sigma^2}(Y - X\beta)^\top(Y - X\beta)
$$
and
$$
\frac{\partial}{\partial \beta} \log \mathcal{L}(\beta; Y) = \frac{1}{\sigma^2}(X^\top Y - X^\top X \beta) = 0
$$
so we have the maximum likelihood estimator
$$
\beta = (X^\top X)^{-1} X^\top Y.
$$
If the errors are not normally distributed, we should probably be better by using differerent loss functions. For example, if the errors have heavy-tails, we should use robust regression techniques.

## Bias-Variance Tradeoff

We know that
$$
\mathrm{MSE} = \mathrm{bias}^2 + \mathrm{variance}.
$$
The classical linear regression solution (1) has no bias, and the MSE is the variance of (1).

If we use Ridge regression, the bias is $\hat{\beta}^{\rm ridge} - \hat{\beta}$. However, the variance of $\hat{\beta}^{\rm ridge}$ is always less than $\hat{\beta}$.

## Dependent Features

If the features are not linearly independent, there can be multiple expressions for $\hat{\beta}$. One possible way is to solve for the Moore-Penrose pseudo-inverse $X^-$ of $X$, computed by inverting the singular values in SVD, and we can let
$$
\hat{\beta} = X^- y
$$
This is the coefficient with the minimum norm. If the collinearity is just high, this is quite similar to using principle component analysis.

Or, we could use Ridge regression. The matrix $X^\top X + \lambda I$ is always invertible, since for any non-zero vector $v$,
$$
v^\top (X^\top X + \lambda I)v = \|Xv\|^2 + \lambda \|v\|^2 > 0.
$$
Hence $X^\top X + \lambda I$ is positive-definite and has positive eigenvalues, so it is invertible.

In general, when there are highly collinear features, it might cause the matrix to be ill-conditioned, that the condition number $\kappa(X^\top X) = \frac{\lambda_{\max}(X^\top X)}{\lambda_{\min}(X^\top X)}$ is huge, and the model will be very sensitive to noise. We should select features carefully to avoid.

## $R^2$

For simple linear regression, $R^2$ equals $\mathrm{corr}(x, y)$.

## Problems

1. If $y \sim \beta_1 x_1 + \varepsilon_1$ and $y \sim \beta_2 x_2 + \varepsilon_2$, each with $R^2$ of $R_1^2$ and $R_2^2$, then what is the range of $R^2$ for $y \sim \beta_3 x_1 + \beta_4 x_2 + \varepsilon$?

   The range is $\max(R_1^2, R_2^2) \le R^2 \le 1$. The minimum can be achieved when $x_1 = x_2$, or say $x_1 = x_2 + x_3$, where $x_2 \perp x_3$, so $x_3$ is in $\varepsilon_2$ when fitting only using $x_2$.

   The maximum can be achieved when $y = \beta_1 x_1 + \beta_2 x_2$. Notice that this can happen even if $R_1^2 + R_2^2 < 1$, specifically when the correlation between $x_1$ and $x_2$ is very negative.

2.
