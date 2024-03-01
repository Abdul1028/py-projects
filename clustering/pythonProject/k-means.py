import pandas as pd
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler
import seaborn as sns
import matplotlib.pyplot as plt

#

# Convert the data string to a DataFrame
df = pd.read_csv("a.csv")

# Drop the 'Outcome' column
X = df.drop(['Outcome'], axis=1)

# Standardize the features
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

# Choose the number of clusters (you can use the elbow method)
k = 3

# Apply k-means clustering
kmeans = KMeans(n_clusters=k, random_state=42)
df['Cluster'] = kmeans.fit_predict(X_scaled)
print(df['Cluster'])

print(df.head())

# Visualize the clusters with a pair plot
df_vis = df.drop(['Outcome'], axis=1)  # Exclude 'Outcome' column for visualization
sns.pairplot(df_vis, hue='Cluster', palette='viridis')
plt.suptitle('Pair Plot of Clusters', y=1.02)
plt.show()
