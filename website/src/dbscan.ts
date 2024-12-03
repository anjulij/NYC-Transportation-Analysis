export function loadDBSCAN(): void {
    console.log("Loading DBSCAN content");

    async function loadClusterPlot() {
        console.log('Loading cluster plot');
        const content = document.getElementById('content');
        if (content) {
            try {
                const response = await fetch('./assets/generated_plots/dbscan_clusters.html');
                if (response.ok) {
                    const htmlContent = await response.text();
                    content.innerHTML = htmlContent;
                } else {
                    console.error('Failed to load DBSCAN plot:', response.statusText);
                }
            } catch (error) {
                console.error('Error fetching DBSCAN plot:', error);
            }
        } else {
            console.error('Content element not found');
        }
    }
    loadClusterPlot();
}