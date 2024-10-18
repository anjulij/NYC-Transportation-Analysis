import { loadHome } from './home.js';
import { loadKMeans } from './kmeans.js';
import { loadDBSCAN } from './dbscan.js';
import { loadAbout } from './about.js';
function createNavBar() {
    var _a, _b, _c, _d;
    const navbar = document.getElementById('navbar');
    if (navbar) {
        navbar.innerHTML = `
            <a href="#" id="home-link">Home</a>
            <a href="#" id="kmeans-link">K-Means</a>
            <a href="#" id="dbscan-link">DBSCAN</a>
            <a href="#" id="about-link">About</a>
        `;
        (_a = document.getElementById('home-link')) === null || _a === void 0 ? void 0 : _a.addEventListener('click', (e) => {
            e.preventDefault();
            console.log('Home link clicked');
            loadHome();
        });
        (_b = document.getElementById('kmeans-link')) === null || _b === void 0 ? void 0 : _b.addEventListener('click', (e) => {
            e.preventDefault();
            console.log('KMeans link clicked');
            loadKMeans();
        });
        (_c = document.getElementById('dbscan-link')) === null || _c === void 0 ? void 0 : _c.addEventListener('click', (e) => {
            e.preventDefault();
            console.log('DBSCAN link clicked');
            loadDBSCAN();
        });
        (_d = document.getElementById('about-link')) === null || _d === void 0 ? void 0 : _d.addEventListener('click', (e) => {
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
