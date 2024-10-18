export function loadAbout(): void {
    const content = document.getElementById('content');
    if (content) {
        console.log('Loading about content');
        content.innerHTML = `
            <div id="about-content">
                <p class="center-text">About</p>
            </div>
            <div id="blurb-text"></div>
        `;
    } else {
        console.error('Content element not found');
    }
}