import numpy as np
from sklearn.linear_model import LinearRegression, Ridge


class MyLinearRegression:
    def __init__(self, X, y, alpha=0):
        self.n = X.shape[0]
        self.d = X.shape[1]
        self.X = np.hstack((X, np.ones((self.n,1))))
        reg_term = alpha * np.eye(self.d+1)
        reg_term[-1,-1] = 0
        self.b = np.linalg.pinv(self.X.T @ self.X + reg_term) @ self.X.T @ y

    def predict(self, Z):
        Z = np.hstack((Z, np.ones((Z.shape[0], 1))))
        y = Z @ self.b
        return y


if __name__ == '__main__':
    n, m, d = 100, 4, 8
    alpha = 1
    X = np.random.random((n, d))
    y = np.random.random((n, 1))
    Z = np.random.random((m, d))
    model = MyLinearRegression(X, y, alpha=alpha)
    labels = model.predict(Z)
    print(labels)

    if alpha > 0:
        model_ref = Ridge(alpha=alpha, solver='svd')
    else:
        model_ref = LinearRegression()
    model_ref.fit(X, y)
    labels_ref = model_ref.predict(Z)
    print(labels_ref)

