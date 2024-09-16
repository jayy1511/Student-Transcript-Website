document.addEventListener('DOMContentLoaded', function() {
    
    function formatDate(date) {
        const options = { year: 'numeric', month: 'short', day: 'numeric', hour: 'numeric', minute: 'numeric', second: 'numeric', timeZoneName: 'short' };
        return new Date(date).toLocaleDateString('en-US', options);
    }

    const currentDate = new Date();

    const lastUpdatedElement = document.getElementById('lastUpdatedDate');
    lastUpdatedElement.textContent = formatDate(currentDate);
});
