# Random Incidence: Bus Interval Problem

## Exponential Distribution

The exponential distribution is memoryless: 
$$
\mathbb{E}[X - t \mid X \ge t] = \frac{\int_t^\infty \lambda (u-t) e^{-\lambda u}~du}{e^{-\lambda t}} = \frac{e^{-\lambda t} \int_0^\infty \lambda u e^{-\lambda u}~du}{e^{-\lambda t}} = \mathbb{E}[X].
$$


## Any Continuous Distribution

Suppose the distribution for the interval between bus arrival time has pdf $f(x)$.  Then, let $Y$ be the length of the interval that when we arrive. We make the claim that $g(y) \propto yf(y)$. This is because 
