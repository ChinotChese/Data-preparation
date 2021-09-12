from __future__ import print_function
import matplotlib.pyplot as plt
import numpy as np

np.random.seed(11)

means = [[2, 2], [8, 3], [3, 6]]
cov = [[1, 0], [0, 1]]
N = 500
X0 = np.random.multivariate_normal(means[0], cov, N)
X1 = np.random.multivariate_normal(means[1], cov, N)
X2 = np.random.multivariate_normal(means[2], cov, N)

X = np.concatenate((X0, X1, X2), axis=0)


def kmeans_display3(X, clusters):
    X0 = np.array([X[i] for i in clusters[0]])
    X1 = np.array([X[i] for i in clusters[1]])
    X2 = np.array([X[i] for i in clusters[2]])

    plt.plot(X0[:, 0], X0[:, 1], 'b^', markersize=4, alpha=.8)
    plt.plot(X1[:, 0], X1[:, 1], 'go', markersize=4, alpha=.8)
    plt.plot(X2[:, 0], X2[:, 1], 'rs', markersize=4, alpha=.8)

    plt.axis('equal')
    plt.plot()
    plt.show()


def kmeans_display2(X, clusters):
    X0 = np.array([X[i] for i in clusters[0]])
    X1 = np.array([X[i] for i in clusters[1]])

    plt.plot(X0[:, 0], X0[:, 1], 'b^', markersize=4, alpha=.8)
    plt.plot(X1[:, 0], X1[:, 1], 'go', markersize=4, alpha=.8)

    plt.axis('equal')
    plt.plot()
    plt.show()


def kmeans_display4(X, clusters):
    X0 = np.array([X[i] for i in clusters[0]])
    X1 = np.array([X[i] for i in clusters[1]])
    X2 = np.array([X[i] for i in clusters[2]])
    X3 = np.array([X[i] for i in clusters[3]])

    plt.plot(X0[:, 0], X0[:, 1], 'b^', markersize=4, alpha=.8)
    plt.plot(X1[:, 0], X1[:, 1], 'go', markersize=4, alpha=.8)
    plt.plot(X2[:, 0], X2[:, 1], 'rs', markersize=4, alpha=.8)
    plt.plot(X3[:, 0], X3[:, 1], 'y+', markersize=4, alpha=.8)

    plt.axis('equal')
    plt.plot()
    plt.show()


def init_centroids(X, K):
    return X[np.random.choice(X.shape[0], K, replace=False)]


def create_clusters(X, centroids, K):
    cluster = [[] for i in range(K)]
    for idx, point in enumerate(X):
        closest_centroid = np.argmin(np.sqrt(np.sum((point - centroids) ** 2, axis=1)))
        cluster[closest_centroid].append(idx)
    return cluster


def update_centroids(X, clusters, K):
    centroids = np.zeros((K, X.shape[1]))
    for inx, cluster in enumerate(clusters):
        new_centroid = np.mean(X[cluster], axis=0)
        centroids[inx] = new_centroid
    return centroids


def converged(centroids, new_centroids):
    return set([tuple(a) for a in centroids]) == set([tuple(a) for a in new_centroids])


def kmeans(X, K):
    centroids = init_centroids(X, K)
    it = 0
    while True:
        clusters = create_clusters(X, centroids, K)
        new_centroids = update_centroids(X, clusters, K)
        if converged(centroids, new_centroids):
            break
        centroids = new_centroids
        it += 1
    return centroids, clusters, it


centroids3, clusters3, it3 = kmeans(X, 3)
kmeans_display3(X, clusters3)

centroids2, clusters2, it2 = kmeans(X, 2)
kmeans_display2(X, clusters2)

centroids4, clusters4, it4 = kmeans(X, 4)
kmeans_display4(X, clusters4)