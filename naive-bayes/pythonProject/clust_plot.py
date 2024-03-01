import pandas as pd
from sklearn.cluster import KMeans
from sklearn.metrics import silhouette_score
import matplotlib.pyplot as plt
import seaborn as sns

# Range of clusters to try
k_values = range(2, 10)

file_path = 'a.csv'  # Replace 'your_dataset.csv' with the actual file path
df = pd.read_csv(file_path)

# Features to use
features = ['Pregnancies', 'Glucose', 'BloodPressure', 'SkinThickness', 'Insulin', 'BMI', 'DiabetesPedigreeFunction', 'Age']

# Assuming 'Outcome' is the target variable, you can replace it with the actual target column name
X = df[features].head(50)
y = df['Outcome']

# Silhouette scores and cluster assignments for each k
silhouette_scores = []
cluster_assignments = []

kmeans = KMeans(n_clusters=3, random_state=42)
labels = kmeans.fit_predict(X)
silhouette_scores.append(silhouette_score(X, labels))
cluster_assignments.append(labels)

cluster_labels = kmeans.cluster_centers_

# Choose the optimal number of clusters based on the maximum silhouette score
optimal_k =  3

# Plot the 2D Scatter Plot with Cluster Assignments
plt.figure(figsize=(8, 6))

sns.scatterplot(x=features[0], y=features[1], hue=cluster_labels, palette='viridis', data=df.head(100))
plt.title(f'2D Scatter Plot with Cluster Assignments for k={optimal_k}')
plt.xlabel(features[0])
plt.ylabel(features[1])


plt.show()
