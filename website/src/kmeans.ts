export function loadKMeans(): void {
    console.log("Initializing K-Means content loader");

    function loadKMeansPlot() {
        console.log("Attempting to load K-Means plot");

        const content = document.getElementById('content');
        if (!content) {
            console.error("Error: Container element with id 'content' not found.");
            return;
        }

        // Create the iframe element
        const iframe = document.createElement('iframe');
        iframe.src = './assets/generated_plots/kmeans_Monday.html?theme=dark'; 
        iframe.width = '100%';
        iframe.height = '100%';
        iframe.style.border = 'none';

        // Ensure the parent container has a defined size
        content.style.width = '100%'; 
        content.style.height = '600px';

        // Clear existing content and append the iframe
        content.innerHTML = '';
        content.appendChild(iframe);

        console.log("Successfully embedded K-Means plot in an iframe.");
    }

    loadKMeansPlot();
}