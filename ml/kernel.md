# Kernel Methods
This part is adapted from *The Elements of Statistical Learning, 5.8 Regularization and Reproducing Kernel Hilbert Spaces*.

We consider the space $\mathcal{H}_K$ of functions 
$$f(x) = \sum_{i=1}^\infty \alpha_i K(x, y_i)$$
where $K$ is some positive-semidefinite kernel.

It can be shown with some functional analysis that the solution to
$$\min_{f \in \mathcal{H}_K} \sum_{i=1}^N L(y_i, f(x_i)) + \lambda \|f\|_{\mathcal{H}_K}^2$$
is finite-dimensional and has the form
$$f(x) = \sum_{i=1}^N \alpha_i K(x, x_i).$$
The kernel satisfy $\langle K(\cdot,x_i), K(\cdot,x_j)\rangle_{\mathcal{H}_K} = K(x_i, x_j)$ by the *reproducing property* of $\mathcal{H}_K$, so the penalty term becomes
$$\sum_{i=1}^N \sum_{j=1}^N K(x_i, x_j) \alpha_i \alpha_j$$
The problem reduces to finding
$$\min_{\alpha} L(y, K\alpha) + \lambda \alpha^\top K\alpha$$
where $K$ is the matrix of $K(x_i, x_j)$, which is the kernel regression problem.
