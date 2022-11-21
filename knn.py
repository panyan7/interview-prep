import numpy as np
from collections import Counter
from sklearn.neighbors import KNeighborsClassifier


class MyKNN:
    def __init__(self, X, Y, k):
        self.X = X
        self.Y = Y
        self.n = X.shape[0]
        self.k = k

    def predict(self, Z):
        m = Z.shape[0]
        labels = np.zeros(m)
        for j in range(m):
            d = np.zeros(n)
            for i in range(n):
                d[i] = np.linalg.norm(X[i,:] - Z[j,:], 2)
            idx = np.argsort(d)
            label = Counter(Y[idx[:k]])
            # most_common returns a list of most common n (element, count)
            labels[j] = label.most_common(1)[0][0]
        return labels


if __name__ == '__main__':
    n, d, m, k = 100, 8, 4, 5
    X = np.random.random((n,d))
    Y = np.random.randint(2, size=n)
    Z = np.random.random((m, d))
    model = KNN(X, Y, k)
    labels = model.predict(Z)
    print(labels)
    model_ref = KNeighborsClassifier(n_neighbors=k)
    model_ref.fit(X, Y)
    labels_ref = model_ref.predict(Z)
    print(labels_ref)
