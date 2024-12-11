import { loadHome } from './home.js';
import { loadComparison } from './comparison.js';
import { loadKMeans } from './kmeans.js';
import { loadDBSCAN } from './dbscan.js';
import { loadAbout } from './about.js';

function createNavBar(): void {
    const navbar = document.getElementById('navbar');
    if (navbar) {
        navbar.innerHTML = `
            <a href="#" id="home-link" aria-current="page">NYC Public Transport Analysis</a>
            <a href="#" id="comparison-link">Comparison</a>
            <a href="#" id="kmeans-link">K-Means</a>
            <a href="#" id="dbscan-link">DBSCAN</a>
            <a href="#" id="about-link">About</a>
        `;

        // Event delegation for navigation links
        navbar.addEventListener('click', (event) => {
            const target = event.target as HTMLElement;
            if (target.tagName === 'A') {
                event.preventDefault();
                const links = navbar.querySelectorAll('a');
                links.forEach((link) => link.removeAttribute('aria-current'));

                target.setAttribute('aria-current', 'page');
                const linkId = target.id;

                // Load appropriate content
                switch (linkId) {
                    case 'home-link':
                        loadHome();
                        break;
                    case 'comparison-link':
                        loadComparison();
                        break;
                    case 'kmeans-link':
                        loadKMeans();
                        break;
                    case 'dbscan-link':
                        loadDBSCAN();
                        break;
                    case 'about-link':
                        loadAbout();
                        break;
                }
            }
        });

        document.addEventListener('keydown', (event) => {
            if (event.key === 'Tab') {
                document.body.classList.add('user-is-tabbing');
            }
        });

        document.addEventListener('mousedown', () => {
            document.body.classList.remove('user-is-tabbing');
        });
    } else {
        console.error('Navbar element not found');
    }
}

function createBottomBar(): void {
    const bottombar = document.getElementById('bottombar');
    if (bottombar) {
        bottombar.innerHTML = `
            COP 3530 Project 
            <img src="assets/images/favorite_24dp.svg" alt="heart icon" id="heart-icon" role="img">
        `;
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