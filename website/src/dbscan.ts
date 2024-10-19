export function loadDBSCAN(): void {
    console.log("Loading DBSCAN content");

    async function loadClusterPlot() {
        try {
            const response = await fetch('/src/assets/generated_plots/dbscan_clusters.html');
            const plotHtml = await response.text();
  
            const content = document.getElementById('content');
            if (content) {
                content.innerHTML = plotHtml;
            } else {
                console.error('Content element not found');
            }
        } catch (error) {
            console.error("Error loading the cluster plot:", error);
        }
    }
    loadClusterPlot();
}