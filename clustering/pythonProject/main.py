import pandas as pd
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans, AgglomerativeClustering
from sklearn.metrics import silhouette_score
from sklearn.preprocessing import StandardScaler


# Convert the data string to a DataFrame
df = pd.read_csv("a.csv")

# Remove the 'Outcome' column
X = df.drop('Outcome', axis=1)

# Standardize the features
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

# K-means clustering
k_values = range(2, 10)
silhouette_scores = []

for k in k_values:
    kmeans = KMeans(n_clusters=k, random_state=42)
    kmeans.fit(X_scaled)
    labels = kmeans.labels_
    silhouette_scores.append(silhouette_score(X_scaled, labels))

# Elbow method
plt.figure(figsize=(10, 5))
plt.subplot(1, 2, 1)
plt.plot(k_values, silhouette_scores)
plt.show()