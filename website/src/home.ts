export function loadHome(): void {
    const content = document.getElementById('content');
    if (content) {
        console.log('Loading home content');
        content.innerHTML = `
            <div id="home-content" style="text-align: center;">
                <h1>Explore MTA Subway Trends</h1>
                    <p>Unveiling insights through advanced clustering methods K-Means and DBSCAN.</p> 
                    <p>Every Monday in 2022</p>            
                <div id="blurb-text"></div>
            </div>
        `;
    } else {
        console.error('Content element not found');
    }
}
