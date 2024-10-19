export function loadDBSCAN(): void {
    console.log("Loading DBSCAN content");

    async function loadClusterPlot() {
        try {
            console.log('Loading cluster plot');
            //const response = await fetch('/src/assets/generated_plots/dbscan_clusters.html');
            //const plotHtml = await response.text();
  
            const content = document.getElementById('content');
            if (content) {
                //console.log('innerHTML assigned to plotHtml');
                content.innerHTML = `<iframe src="/src/assets/generated_plots/dbscan_clusters.html" style="width: 100%; height: 100%; border: none;"></iframe>`;
            } else {
                console.error('Content element not found');
            }
        } catch (error) {
            console.error("Error loading the cluster plot:", error);
        }
    }
    loadClusterPlot();
}