export function loadHome(): void {
    const content = document.getElementById('content');
    if (content) {
        console.log('Loading home content');
        content.innerHTML = `
            <div id="home-content">
                <p class="center-text">Home</p>
            </div>
            <div id="blurb-text"></div>
        `;
    } else {
        console.error('Content element not found');
    }
}