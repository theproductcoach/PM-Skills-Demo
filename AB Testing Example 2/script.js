document.addEventListener('DOMContentLoaded', () => {
    const testButton = document.getElementById('testButton');
    const isBlue = Math.random() < 0.5;

    if (isBlue) {
        testButton.classList.add('blue');
        trackEvent('blue');
    } else {
        testButton.classList.add('green');
        trackEvent('green');
    }

    testButton.addEventListener('click', function handleClick() {
        trackEvent('button clicked', isBlue ? 'blue' : 'green');

        // Add grey class and remove blue/green class
        testButton.classList.add('grey');
        testButton.classList.remove('blue', 'green');

        // Remove click event listener
        testButton.removeEventListener('click', handleClick);
    });
});

function trackEvent(action, color = '') {
    // In a real implementation, this would send data to a server or analytics service.
    console.log(`Event: ${action}, Color: ${color}`);
}

// Initial setup for Chart.js
const ctx = document.getElementById('clickChart').getContext('2d');
const clickChart = new Chart(ctx, {
    type: 'bar',
    data: {
        labels: ['Blue Clicks', 'Blue Impressions', 'Green Clicks', 'Green Impressions'],
        datasets: [{
            label: 'Count',
            data: [0, 0, 0, 0], // Initial data
            backgroundColor: [
                'rgba(54, 162, 235, 0.2)', // Blue Clicks
                'rgba(54, 162, 235, 0.5)', // Blue Impressions
                'rgba(75, 192, 192, 0.2)', // Green Clicks
                'rgba(75, 192, 192, 0.5)'  // Green Impressions
            ],
            borderColor: [
                'rgba(54, 162, 235, 1)',
                'rgba(54, 162, 235, 1)',
                'rgba(75, 192, 192, 1)',
                'rgba(75, 192, 192, 1)'
            ],
            borderWidth: 1
        }]
    },
    options: {
        scales: {
            y: {
                beginAtZero: true
            }
        }
    }
});

// Function to update chart data
function updateChartData(clicksBlue, impressionsBlue, clicksGreen, impressionsGreen) {
    clickChart.data.datasets[0].data = [clicksBlue, impressionsBlue, clicksGreen, impressionsGreen];
    clickChart.update();
}

// Variables to store clicks and impressions
let clicksBlue = 0;
let impressionsBlue = 0;
let clicksGreen = 0;
let impressionsGreen = 0;

// Function to track button clicks and update counters and chart
function trackButtonClick(buttonId, counterId, isBlue) {
    const button = document.getElementById(buttonId);
    const counter = document.getElementById(counterId);

    button.addEventListener('click', () => {
        if (isBlue) {
            clicksBlue++;
            impressionsBlue++;
        } else {
            clicksGreen++;
            impressionsGreen++;
        }

        counter.textContent = `Clicks: ${isBlue ? clicksBlue : clicksGreen}`;
        updateChartData(clicksBlue, impressionsBlue, clicksGreen, impressionsGreen);
    });
}

// Track each button
trackButtonClick('buttonBlue', 'counterBlue', true);
trackButtonClick('buttonGreen', 'counterGreen', false);