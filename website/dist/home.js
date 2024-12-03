export function loadHome() {
    const content = document.getElementById('content');
    if (content) {
        console.log('Loading home content');
        content.innerHTML = `
            <div id="home-content" style="text-align: center;">
                <h1>Explore NYC's Public Transport Trends</h1>
                <p>Unveiling insights through advanced clustering methods K-Means and DBSCAN.</p>            
                <div id="blurb-text"></div>
            </div>
        `;
    }
    else {
        console.error('Content element not found');
    }
}
