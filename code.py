code
# Import necessary libraries
import pandas as pd
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt

# Read the data from CSV file into a DataFrame
data = pd.read_csv('/content/drive/MyDrive/K-mean/mango2.csv')

# Get the column names of the DataFrame
co = data.columns
print(co)

# Display the first few rows of the DataFrame
data.head()

# Select features for clustering ('A', 'B', 'C', 'C.1')
X = data[['A', 'B', 'C', 'C.1']]

# Set the number of clusters
n_clusters = 3

# Create a KMeans model with the specified number of clusters
kmeans = KMeans(n_clusters=n_clusters, random_state=42)

# Fit the KMeans model to the data
kmeans.fit(X)

# Add a new column 'Cluster' to the DataFrame with cluster labels
data['Cluster'] = kmeans.labels_

# Create a scatter plot to visualize the clusters and centroids
plt.scatter(X['A'], X['B'], c=data['Cluster'], cmap='viridis')
plt.scatter(kmeans.cluster_centers_[:, 0], kmeans.cluster_centers_[:, 1], c='red', marker='x', s=200, label='Centroids')
plt.xlabel('GreenMangoLength')
plt.ylabel('GreenMangoWidth')
plt.title('K-Means Clustering')
plt.legend()
plt.show()

# Additional code assuming 'df' is used (incorrect, should be 'data')
# Assume df is your DataFrame
X = df[['A', 'B']]

# Try different values of K
for k in range(2, 6):
    # Create KMeans model
    kmeans = KMeans(n_clusters=k, random_state=42)
    
    # Fit the model
    kmeans.fit(X)
    
    # Create a new column in the DataFrame to store cluster assignments
    df[f'Cluster_{k}'] = kmeans.labels_

    # Plot the clusters
    plt.scatter(X['A'], X['B'], c=df[f'Cluster_{k}'], cmap='viridis')
    plt.scatter(kmeans.cluster_centers_[:, 0], kmeans.cluster_centers_[:, 1], c='red', marker='x', s=200, label='Centroids')
    plt.xlabel('GreenMangoLength')
    plt.ylabel('GreenMangoWidth')
    plt.title(f'K-Means Clustering with {k} Clusters')
    plt.legend()
    plt.show()
