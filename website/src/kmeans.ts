export function loadKMeans(): void {
    const content = document.getElementById('content');
    if (content) {
        console.log('Loading kmeans content');
        content.innerHTML = `
            <div id="kmeans-content">
                <p class="center-text">K-Means</p>
            </div>
            <div id="blurb-text"></div>
        `;
    } else {
        console.error('Content element not found');
    }
}