# NYC-Transportation-Analysis

# Description and Motivation
The objective of this project is to identify the bottlenecks in NYC traffic patterns and overlay the taxi, bus, and subway congestion maps. This analysis can lead to more efficient bus/taxi routes and/or help users decide on the most efficient mode of transportation. 

Clustering Algorithms to Compare: 
K-Means Clustering is extremely fast and scalable, however, it is limited by data that is unevenly clustered. Density-Based Spatial Clustering of Applications with Noise (DBSCAN) is great for a natural fit and handling noise, however, it is limited by significant density variation. The centroids identified by K-Means will represent potential bottleneck areas, whereas DBSCAN's ability to handle noise may help identify less obvious hotspots.

# Features
The k-means algorithm works by randomly assigning “k” number of centroids in the data, assigning each data point to a nearest centroid, and recalculating the centroid of each cluster. The algorithm converges once all of the clusters don’t change, and hence the bottlenecks in traffic data are identified. On the other hand, the DBSCAN algorithm works by grouping  data points based on distance and a minimum number of points required to form a cluster. The algorithm finishes once all data points have been visited and assigned a cluster  or marked as noise (Karl, 2024). This will allow for bottlenecks to be identified. 

# Data 
NYC Taxi Fare Dataset,  New York City Bus Data, and NYS NYC Transit Subway Entrance and Exit Data for analysis. OpenStreetMap and MapBox for our map overlay. 

# Tools
Python: for data processing, clustering, and analysis
Libraries: SciPy for statistical analysis and Scikit-Learn for machine learning models. Matplotlib or Plotly for deploying the visualization on the website.
Typescript, React.js, and Github Pages: to develop and host the interactive visualization of traffic patterns
Figma: for designing the layout and flow of our website

# Strategy 
Data will be stored via Git Large File Storage in order to maintain a static data set ensuring reproducibility.
Process our data either using PostGIS for its geospatial capabilities or Time Series Database for focusing on temporal analysis
Implement DBSCAN and K-Means concurrently
Explore algorithms to improve transportation efficiency.
Visualize in a 2d data cluster and if time permits, a 3d representation will be created
Allow users to change input based on time of day

# Distribution of Responsibilities and Roles
We will follow an agile approach to manage and track progress. Tasks will be broken down into sprints. Git will be used for version control. For the first sprint we’ll split the tasks into DBSCAN, K-Means, and web design. We’ll assign issues that come up to different team members so that everyone is familiar with the code. 
