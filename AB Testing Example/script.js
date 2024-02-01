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

