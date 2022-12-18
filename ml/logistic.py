import numpy as np
from sklearn.linear_model import LogisticRegression


class MyLogisticRegression:
    def __init__(self, X, y, num_iters=100, lr=1):
        self.n = X.shape[0]
        self.d = X.shape[1]
        self.X = np.hstack((X, np.ones((self.n, 1))))
        self.fit(self.X, y, num_iters=num_iters, lr=lr)

    def fit(self, X, y, num_iters=100, lr=0.01):
        self.w = np.random.random((self.d+1, 1))
        for t in range(num_iters):
            self.w -= lr * self.grad(self.w, X, y)

    def logistic(self, z):
        return 1.0 / (1.0 + np.exp(-z))

    def f(self, w, X, y):
        h = self.logistic(X @ w)
        return np.sum(- y * np.log(h) - (1 - y) * np.log(1 - h)) / self.n

    def grad(self, w, X, y):
        h = self.logistic(X @ w)
        g = X.T @ (h - y) / self.n
        return g

    def predict(self, Z):
        Z = np.hstack((Z, np.ones((Z.shape[0], 1))))
        return self.logistic(Z @ self.w)


if __name__ == '__main__':
    n, m, d = 100, 4, 8
    alpha = 1
    X = np.random.random((n, d))
    y = np.random.randint(2, size=(n,1))
    Z = np.random.random((m, d))
    model = MyLogisticRegression(X, y)
    labels = model.predict(Z)
    print(labels)

    model_ref = LogisticRegression()
    model_ref.fit(X, y)
    labels_ref = model_ref.predict(Z)
    print(labels_ref)

