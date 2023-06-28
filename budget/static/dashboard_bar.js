// dashboard.js

// Function to fetch data from the backend
function fetchData() {
    // Make an AJAX request to your Django backend to fetch the data
    fetch('/dashboard-data-bar/')
        .then(response => response.json())
        .then(data => {
            // Call a function to update the chart with the new data
            updateChart(data);
        })
        .catch(error => {
            console.error('Error:', error);
        });
}

// Function to update the chart with new data
function updateChart(data) {
    // Extract the necessary data from the response
    var x = data.x;
    var y = data.y;
    var canvas_id = data.canvas_id;
    var y_label = data.y_label

    var canvas = document.getElementById(canvas_id);

    // Create the chart
    var dashboardChart = new Chart(canvas, {
        type: 'bar',
        data: {
            labels: x,
            datasets: [{
                label: y_label,
                data: y,
                backgroundColor: 'rgba(75, 192, 192, 0.2)',
                borderColor: 'rgba(75, 192, 192, 1)',
                borderWidth: 1
            }]
        },
        options: {
            // responsive: true,
            // maintainAspectRatio: false,
            plugins: {
                title: {
                display: true,
                text: 'Current Month Spending by Category',
                font: {
                    size: 12
                }
                }
            },
            scales: {
                y: {
                    beginAtZero: true
                }
            }
        }
    });
}

// Fetch data and update the chart
fetchData();
