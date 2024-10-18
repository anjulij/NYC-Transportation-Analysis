export function loadDBSCAN(): void {
    const content = document.getElementById('content');
    if (content) {
        console.log('Loading dbscan content');
        content.innerHTML = `
            <div id="dbscan-content">
                <p class="center-text">Density-Based Spatial Clustering of Applications with Noise
                </p>
            </div>
            <div id="blurb-text"></div>
        `;
    } else {
        console.error('Content element not found');
    }
}