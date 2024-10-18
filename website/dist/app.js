import { loadHome } from './home.js';
import { loadKMeans } from './kmeans.js';
import { loadDBSCAN } from './dbscan.js';
import { loadAbout } from './about.js';
function createNavBar() {
    var _a, _b, _c, _d;
    const navbar = document.getElementById('navbar');
    if (navbar) {
        navbar.innerHTML = `
            <a href="#home" id="home-link">NYC Public Transport Analysis</a>
            <a href="#kmeans" id="kmeans-link">K-Means</a>
            <a href="#dbscan" id="dbscan-link">DBSCAN</a>
            <a href="#about" id="about-link">About</a>
        `;
        (_a = document.getElementById('home-link')) === null || _a === void 0 ? void 0 : _a.addEventListener('click', (e) => {
            e.preventDefault();
            console.log('Home link clicked');
            window.location.hash = 'home';
            loadHome();
        });
        (_b = document.getElementById('kmeans-link')) === null || _b === void 0 ? void 0 : _b.addEventListener('click', (e) => {
            e.preventDefault();
            console.log('KMeans link clicked');
            window.location.hash = 'kmeans';
            loadKMeans();
        });
        (_c = document.getElementById('dbscan-link')) === null || _c === void 0 ? void 0 : _c.addEventListener('click', (e) => {
            e.preventDefault();
            console.log('DBSCAN link clicked');
            window.location.hash = 'dbscan';
            loadDBSCAN();
        });
        (_d = document.getElementById('about-link')) === null || _d === void 0 ? void 0 : _d.addEventListener('click', (e) => {
            e.preventDefault();
            console.log('About link clicked');
            window.location.hash = 'about';
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
function setActiveLink() {
    const currentHash = window.location.hash;
    console.log("Current Hash:", currentHash);
    const links = document.querySelectorAll("nav a");
    links.forEach(link => link.classList.remove("active"));
    const activeLink = document.querySelector(`nav a[href="${currentHash}"]`);
    if (activeLink) {
        console.log("Active Link Found:", activeLink.textContent);
        activeLink.classList.add("active");
    }
    else {
        console.warn("No active link found for:", currentHash);
    }
}
function initializeApp() {
    createNavBar();
    createBottomBar();
    loadHome();
    setActiveLink();
}
document.addEventListener("DOMContentLoaded", () => {
    initializeApp();
    window.addEventListener("hashchange", setActiveLink);
});
