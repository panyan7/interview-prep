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

## Bias-Variance Tradeoff

We know that
$$
\mathrm{MSE} = \mathrm{bias}^2 + \mathrm{variance}.
$$
The classical linear regression solution (1) has no bias, and the MSE is the variance of (1).

If we use Ridge regression, the bias is $\hat{\beta}^{\rm ridge} - \hat{\beta}$. However, the variance of $\hat{\beta}^{\rm ridge}$ is always less than $\hat{\beta}$.

## Dependent Features

If the features are not linearly independent, there can be multiple expressions for $\hat{\beta}$. One possible way is to solve for the Moore-Penrose pseudo-inverse $X^-$ of $X$, and we can let
$$
\hat{\beta} = X^- y
$$
This is the coefficient with the minimum norm.

Or, we could use Ridge regression. The matrix $X^\top X + \lambda I$ is always invertible, since for any non-zero vector $v$,
$$
v^\top (X^\top X + \lambda I)v = \|Xv\|^2 + \lambda \|v\|^2 > 0.
$$
Hence $X^\top X + \lambda I$ is positive-definite and has positive eigenvalues, so it is invertible.