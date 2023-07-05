// dashboard.js

// Function to fetch data from the backend
function fetchData() {
    // Make an AJAX request to your Django backend to fetch the data
    fetch('/dashboard/')
        .then(response => response.json())
        .then(data => {
            // Call a function to update the chart with the new data
            for (var chart in data){
                updateChart(data[chart]);
            }
        })
        .catch(error => {
            console.error('Error:', error);
        });
}

// Function to update the chart with new data
function updateChart(data) {
    // Extract the necessary data from the response
    const config = data.config;
    const canvas_id = data.canvas_id;
    var canvas = document.getElementById(canvas_id);
    var dashboardChart = new Chart(canvas, config);
}

// Fetch data and update the chart
fetchData();
