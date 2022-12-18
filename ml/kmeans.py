import numpy as np


class KMeans:
    def __init__(self, X, k, max_iters=100):
        self.n = X.shape[0]
        self.d = X.shape[1]
        self.X = X
        self.k = k
        C = X[np.random.randint(self.n, size=k),:]
        D = np.float('inf')
        for t in range(max_iters):
            D_prev = D
            D = 0.0
            labels = np.zeros(self.n)
            for i in range(self.n):
                min_d = np.float('inf')
                for j in range(k):
                    dist = np.linalg.norm(X[i,:] - C[j,:])
                    if dist < min_d:
                        min_d = dist
                        labels[i] = j
                D += min_d

            for j in range(k):
                C[j,:] = np.mean(X[labels==j,:], axis=0)

            print(D)
            if abs(D_prev - D) < 1e-6:
                break


if __name__ == '__main__':
    n, d, k = 100, 8, 5
    X = np.random.random((n,d))
    model = KMeans(X, k)

