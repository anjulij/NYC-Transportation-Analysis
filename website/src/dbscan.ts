export function loadDBSCAN(): void {
    console.log("Initializing DBSCAN content loader");

    function loadClusterPlot() {
        console.log("Attempting to load DBSCAN cluster plot");

        const content = document.getElementById('content');
        if (!content) {
            console.error("Error: Container element with id 'content' not found.");
            return;
        }

        // Create the iframe element
        const iframe = document.createElement('iframe');
        iframe.src = './assets/generated_plots/dbscan_Monday.html?theme=dark'; 
        iframe.width = '100%';
        iframe.height = '100%';
        iframe.style.border = 'none'; // Optional: Remove iframe border for a cleaner look

        // Ensure the parent container has a defined size
        content.style.width = '100%'; 
        content.style.height = '600px';

        // Clear existing content and append the iframe
        content.innerHTML = '';
        content.appendChild(iframe);

        console.log("Successfully embedded DBSCAN plot in an iframe.");
    }

    loadClusterPlot();
}