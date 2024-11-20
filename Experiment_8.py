import numpy as np
import matplotlib.pyplot as plt
from sklearn.decomposition import PCA
from sklearn.datasets import load_iris

# Load a sample dataset
data = load_iris()
X = data.data  # Feature matrix
y = data.target  # Labels

# Instantiate the PCA model
pca = PCA(n_components=2)  # Reduce to 2 dimensions

# Fit and transform the data
X_reduced = pca.fit_transform(X)

# Explained variance ratio to understand variance captured by each component
explained_variance = pca.explained_variance_ratio_
print("Explained Variance Ratio:", explained_variance)

# Plot the reduced data
plt.figure(figsize=(8, 6))
scatter = plt.scatter(X_reduced[:, 0], X_reduced[:, 1], c=y, cmap='viridis')
plt.xlabel('Principal Component 1')
plt.ylabel('Principal Component 2')
plt.colorbar(scatter, label='Classes')
plt.title('PCA on Iris Dataset')
plt.show()
