from scipy.cluster.hierarchy import dendrogram, linkage
import matplotlib.pyplot as plt
import pandas as pd

# Convert the data string to a DataFrame
df = pd.read_csv("a.csv")

# Drop the 'Outcome' column
X = df.drop(['Outcome'], axis=1)
# Calculate linkage matrix using Ward linkage
linkage_matrix = linkage(X, method='ward')

# Plot the dendrogram
plt.figure(figsize=(12, 8))
dendrogram(linkage_matrix, orientation='top', distance_sort='descending', show_leaf_counts=True)
plt.title('Hierarchical Clustering Dendrogram')
plt.xlabel('Sample Index')
plt.ylabel('Distance')
plt.show()