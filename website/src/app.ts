import { loadHome } from './home.js';
import { loadKMeans } from './kmeans.js';
import { loadDBSCAN } from './dbscan.js';
import { loadAbout } from './about.js';


function createNavBar(): void {
    const navbar = document.getElementById('navbar');
    if (navbar) {
        navbar.innerHTML = `
            <a href="#" id="home-link">NYC Public Transport Analysis</a>
            <a href="#" id="kmeans-link">K-Means</a>
            <a href="#" id="dbscan-link">DBSCAN</a>
            <a href="#" id="about-link">About</a>
        `;

        document.getElementById('home-link')?.addEventListener('click', (e) => {
            e.preventDefault();
            console.log('Home link clicked');
            loadHome();
        });

        document.getElementById('kmeans-link')?.addEventListener('click', (e) => {
            e.preventDefault();
            console.log('KMeans link clicked');
            loadKMeans();
        });

        document.getElementById('dbscan-link')?.addEventListener('click', (e) => {
            e.preventDefault();
            console.log('DBSCAN link clicked');
            loadDBSCAN();
        });

        document.getElementById('about-link')?.addEventListener('click', (e) => {
            e.preventDefault();
            console.log('About link clicked');
            loadAbout();
        });
    } else {
        console.error('Navbar element not found');
    }
}
function createBottomBar(): void {
    const bottombar = document.getElementById('bottombar');
    if(bottombar) {
        bottombar.innerHTML = `
            COP 3530 Project 
            <img src="assets/images/favorite_24dp.svg" alt="heart icon" id="heart-icon">`
    } else {
        console.error('Bottom bar element not found');
    }
}
function initializeApp(): void {
    createNavBar();
    createBottomBar();
    loadHome();  
}
initializeApp();
