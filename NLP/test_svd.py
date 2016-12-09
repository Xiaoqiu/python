#奇异值分解 SVD : 将矩阵降维,分解
import numpy as np
import matplotlib.pyplot as plt
la = np.linalg
words = ['I', 'like', 'enjoy',
         'deep', 'learning', 'NLP', 'flying', '.']
X = np.array([[0, 2, 1, 0, 0, 0, 0, 0],
              [2, 0, 0, 1, 0, 1, 0, 0],
              [1, 0, 0, 0, 0, 0, 1, 0],
              [0, 1, 0, 0, 1, 0, 0, 0],
              [0, 0, 0, 1, 0, 0, 0, 1],
              [0, 1, 0, 0, 0, 0, 0, 1],
              [0, 0, 1, 0, 0, 0, 0, 1],
              [0, 0, 0, 0, 1, 1, 1, 0]])
U, s, Vh = la.svd(X, full_matrices=False)
x = np.arange(-0.8, 0.8, 0.01)
y = np.arange(-0.8, 0.8, 0.01)
plt.plot(x, y)
print(U.shape)

for i in range(len(words)):
#取U的第一列和第二列,词出现的频率,显示距离为词的相似性
    plt.text(U[i, 0], U[i, 1], words[i])
plt.show()