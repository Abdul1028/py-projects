import pandas as pd
from sklearn.cluster import KMeans
from sklearn.metrics import silhouette_score
import matplotlib.pyplot as plt

# Range of clusters to try
k_values = range(2, 10)

file_path = 'a.csv'  # Replace 'your_dataset.csv' with the actual file path
df = pd.read_csv(file_path)

# Assuming 'Outcome' is the target variable, you can replace it with the actual target column name
X = df.drop('Outcome', axis=1)
y = df['Outcome']

# Silhouette scores for each k
silhouette_scores = []

for k in k_values:
    kmeans = KMeans(n_clusters=k, random_state=42)
    labels = kmeans.fit_predict(X)
    silhouette_scores.append(silhouette_score(X, labels))

# Plot the Silhouette Scores
plt.plot(k_values, silhouette_scores, marker='o')
plt.xlabel('Number of Clusters (k)')
plt.ylabel('Silhouette Score')
plt.title('Silhouette Score for Optimal k')
plt.show()











