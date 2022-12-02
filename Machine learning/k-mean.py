
import numpy as np
from sklearn.cluster import KMeans

data =np.array([[3,3],
                [8,5],
                [4,4],
                [2,4],
                [7,7],
                [5,8],
                [3,5],
                [4,8],
                [6,9],
                [9,6],
                ])

kmeans = KMeans(n_clusters=2)
kmeans.fit(X)