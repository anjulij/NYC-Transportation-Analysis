# NYC Transportation Analysis

DBSCAN by Jonathan Soto Ortega, K-Means by Anthony Mezzatesta, and web design and data processing by K. Anjuli Jones

# Description and Motivation
The objective of this project is to identify the bottlenecks in NYC traffic patterns with subway congestion maps. This analysis can lead to more efficient routes.

# Clustering Algorithms to Compare: 
K-Means Clustering is extremely fast and scalable, however, it is limited by data that is unevenly clustered. Density-Based Spatial Clustering of Applications with Noise (DBSCAN) is great for a natural fit and handling noise, however, it is limited by significant density variation. The centroids identified by K-Means will represent potential bottleneck areas, whereas DBSCAN's ability to handle noise may help identify less obvious hotspots.

# Features
The k-means algorithm works by randomly assigning “k” number of centroids in the data, assigning each data point to a nearest centroid, and recalculating the centroid of each cluster. The algorithm converges once all of the clusters don’t change, and hence the bottlenecks in traffic data are identified. On the other hand, the DBSCAN algorithm works by grouping  data points based on distance and a minimum number of points required to form a cluster. The algorithm finishes once all data points have been visited and assigned a cluster  or marked as noise (Karl, 2024). This will allow for bottlenecks to be identified. 

# Data 
MTA Subway hourly ridership  for analysis. OpenStreetMap and MapBox for our map overlay. 
# Tools
Python: for data processing, clustering, and analysis
Libraries: SciPy for statistical analysis and Scikit-Learn for machine learning models. Matplotlib or Plotly for deploying the visualization on the website.
Typescript and Github Pages: to develop and host the interactive visualization of traffic patterns
PostgreSQL: PostGIS with AWS to store the data
Figma: for designing the layout and flow of our website

# Strategy 
Data will be stored via AWS in order to maintain a static data set ensuring reproducibility. We will PostGreSQL  for its geospatial capabilities

Implement DBSCAN and K-Means concurrently
Visualize in a 2d data cluster

Stretch Goals: Allow users to change input based on time of day. Explore algorithms to improve transportation efficiency (min spanning tree)

# How to run

View website at: http://AnthonyMezzatesta.GitHub.io 

To run the website locally:
  - sudo apt update
  - brew update upgrade
  - cd /path/to/main/repo
  - cd website
  - npm install
  - npx tsc
  - python3 -m http.server 8000

View website at: http://localhost:8000/src/main.html#home 

To run dbscan.py or kmeans.py:
Install the necessary things and run:
  - cd data/scripts
  - pip install numpy
  - pip install pandas
  - pip install plotly
  - pip install scikit-learn
  - python3 dbscan.py
  - python3 kmeans.py

For more in-depth logs visit: https://docs.google.com/document/d/1shF7xP5-3gT2tOopyXdo-nvUYgMe50XKBsl7Wzwg-hU/edit?usp=sharing

# References
Karl, T. (2024, February 12). DBSCAN vs. K-Means: A Guide in Python. New Horizons. https://www.newhorizons.com/resources/blog/dbscan-vs-kmeans-a-guide-in-python
