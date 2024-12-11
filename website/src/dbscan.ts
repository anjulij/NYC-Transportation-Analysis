export function loadDBSCAN(): void {
    console.log("Initializing DBSCAN content loader");

    function loadClusterPlot(): void {
        console.log("Attempting to load DBSCAN plot");

        const content = document.getElementById('content');
        if (!content) {
            console.error("Error: Container element with id 'content' not found.");
            return;
        } 

        // Create a separate container for the plot
        content.innerHTML = '';
        const plotContainer = document.createElement('div');
        plotContainer.setAttribute('role', 'region');
        plotContainer.setAttribute('aria-label', 'DBSCAN Plot');
        plotContainer.id = 'plot-container';
        plotContainer.style.width = '100%';
        plotContainer.style.height = '600px';
        content.appendChild(plotContainer);

        const times = ['8', '9', '10', '11', '12', '13', '14', '15', '16', '17', '18'];

        // Generates plots for a specific time
        function generatePlots(time: string): void {
            console.log(`Generating plot for ${time}:00`);

            if (!content) {
                console.error("Error: Content element is null when generating plots.");
                return;
            }

            const plotContainer = document.getElementById('plot-container');
            if (!plotContainer) {
                console.error("Error: Plot container is null when generating plots.");
                return;
            }
            
            // Create and configure a new iframe
            const iframe = document.createElement('iframe');
            iframe.src = `./assets/generated_plots/dbscan/dbscan_${time}.html`;
            iframe.width = '100%';
            iframe.height = '100%';
            iframe.style.border = 'none';

            // Clear existing content and append the new iframe
            plotContainer.innerHTML = '';
            plotContainer.appendChild(iframe);
        }

        // Creates buttons for each time slot and binds event listeners
        function createButtons(): void {
            if (!content) {
                console.error("Error: Content element is null when generating plots.");
                return;
            }

            const buttonContainer = document.createElement('div');
            buttonContainer.classList.add('button-container');
            buttonContainer.setAttribute('role', 'group')
            buttonContainer.setAttribute('aria-label', 'Buttons for selecting time');

            console.log("Creating buttons for time slots...");
            times.forEach(time => {
                const button = document.createElement('button');
                button.setAttribute('role', 'button');
                button.setAttribute('aria-label', `Select ${time}:00`);
                button.textContent = `${time}:00`;
                button.onclick = () => generatePlots(time);
                buttonContainer.appendChild(button);
            });
            // Add the new button container
            content.appendChild(buttonContainer);
        }

        // Initialize the first plot and create buttons
        generatePlots(times[0]);
        createButtons();
    }

    loadClusterPlot();
}