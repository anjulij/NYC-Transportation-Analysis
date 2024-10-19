import numpy as np
from sklearn.datasets import make_blobs
from sklearn.preprocessing import StandardScaler
from sklearn.cluster import DBSCAN
from sklearn import metrics
import plotly.express as px
import plotly.graph_objects as go

# Generate synthetic data
centers = [[1, 1], [-1, -1], [1, -1]]
X, labels_true = make_blobs(n_samples=750, centers=centers, cluster_std=0.4, random_state=0)

# Scale the data
X = StandardScaler().fit_transform(X)

# Apply DBSCAN
db = DBSCAN(eps=0.3, min_samples=10).fit(X)
labels = db.labels_

# Compute the number of clusters (excluding noise)
n_clusters_ = len(set(labels)) - (1 if -1 in labels else 0)
n_noise_ = list(labels).count(-1)

# Print metrics
print(f"Estimated number of clusters: {n_clusters_}")
print(f"Estimated number of noise points: {n_noise_}")
print(f"Homogeneity: {metrics.homogeneity_score(labels_true, labels):.3f}")
print(f"Completeness: {metrics.completeness_score(labels_true, labels):.3f}")
print(f"V-measure: {metrics.v_measure_score(labels_true, labels):.3f}")
print(f"Adjusted Rand Index: {metrics.adjusted_rand_score(labels_true, labels):.3f}")
print(f"Adjusted Mutual Information: {metrics.adjusted_mutual_info_score(labels_true, labels):.3f}")
print(f"Silhouette Coefficient: {metrics.silhouette_score(X, labels):.3f}")

# Create an interactive plot with Plotly
fig = go.Figure()

unique_labels = set(labels)
for k in unique_labels:
    # Define color and marker properties
    color = 'black' if k == -1 else px.colors.qualitative.Plotly[k % len(px.colors.qualitative.Plotly)]
    marker_size = 14 if k != -1 else 6

    # Mask points belonging to the current cluster
    class_member_mask = (labels == k)

    # Add core points
    core_samples_mask = np.zeros_like(labels, dtype=bool)
    core_samples_mask[db.core_sample_indices_] = True
    xy_core = X[class_member_mask & core_samples_mask]

    fig.add_trace(go.Scatter(
        x=xy_core[:, 0], y=xy_core[:, 1],
        mode='markers',
        marker=dict(size=14, color=color, line=dict(width=2, color='black')),
        name=f'Cluster {k}' if k != -1 else 'Noise'
    ))

    # Add non-core points
    xy_non_core = X[class_member_mask & ~core_samples_mask]
    fig.add_trace(go.Scatter(
        x=xy_non_core[:, 0], y=xy_non_core[:, 1],
        mode='markers',
        marker=dict(size=6, color=color, line=dict(width=1, color='black')),
        showlegend=False
    ))

# Update plot title and layout
fig.update_layout(
    title=f'Estimated number of clusters: {n_clusters_}',
    xaxis_title='Feature 1',
    yaxis_title='Feature 2'
)

# Save the plot to an HTML file
fig.write_html("../website/src/assets/generated_plots/dbscan_clusters.html")

print("Plot saved to dbscan_clusters.html")
