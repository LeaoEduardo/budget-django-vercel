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
    const type = data.type;
    const canvas_id = data.canvas_id;
    var canvas = document.getElementById(canvas_id);
    switch (type) {
        case 'bar':
            const x = data.x;
            const y = data.y;
            const y_label = data.y_label
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
            break;
        case 'doughnut':
            var dashboardChart = new Chart(canvas, {
                type: 'bar',
                data: {
                    labels: [
                      'Red',
                      'Blue',
                      'Yellow'
                    ],
                    datasets: [{
                      label: 'My First Dataset',
                      data: [300, 50, 100],
                      backgroundColor: [
                        'rgb(255, 99, 132)',
                        'rgb(54, 162, 235)',
                        'rgb(255, 205, 86)'
                      ],
                      hoverOffset: 4
                    }]
                  };
                
                
                
                {
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
            break;
        // Add more cases as needed
        default:
            console.log("Chart type not available")
            break;
    }
}

// Fetch data and update the chart
fetchData();
