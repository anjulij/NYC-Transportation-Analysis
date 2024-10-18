import { loadHome } from './home.js';
import { loadAbout } from './about.js';
function createNavBar() {
    var _a, _b;
    const navbar = document.getElementById('navbar');
    if (navbar) {
        navbar.innerHTML = `
            <a href="#" id="home-link">Home</a>
            <a href="#" id="about-link">About</a>
        `;
        (_a = document.getElementById('home-link')) === null || _a === void 0 ? void 0 : _a.addEventListener('click', (e) => {
            e.preventDefault();
            console.log('Home link clicked');
            loadHome();
        });
        (_b = document.getElementById('about-link')) === null || _b === void 0 ? void 0 : _b.addEventListener('click', (e) => {
            e.preventDefault();
            console.log('About link clicked');
            loadAbout();
        });
    }
    else {
        console.error('Navbar element not found');
    }
}
function createBottomBar() {
    const bottombar = document.getElementById('bottombar');
    if (bottombar) {
        bottombar.innerHTML = `
            COP 3530 Project 
            <img src="assets/images/favorite_24dp.svg" alt="heart icon" id="heart-icon">`;
    }
    else {
        console.error('Bottom bar element not found');
    }
}
function initializeApp() {
    createNavBar();
    createBottomBar();
    loadHome();
}
initializeApp();
