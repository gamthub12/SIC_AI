from sklearn.datasets import make_blobs, make_moons
import matplotlib.pyplot as plt

X1, label1 = make_blobs(n_samples=200, n_features=2, centers=2, cluster_std = 5, random_state=123)
plt.scatter(X1[:,0],X1[:,1], c= label1, alpha=0.7)
plt.title('Dataset #1 : Original')
plt.show()
plt.savefig('session_14/dataset1.png')