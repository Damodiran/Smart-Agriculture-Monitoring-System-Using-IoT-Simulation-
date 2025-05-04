// Function to initialize the line chart
function initializeChart() {
// Chart.js configuration
var ctx = document.getElementById('line-chart').getContext('2d');
var lineChart = new Chart(ctx, {
    type: 'line',
    data: {
        labels: ['00:00', '00:30', '01:00', '01:30', '02:00', '02:30', '03:00', '03:30', '04:00', '04:30', '05:00', '05:30', '06:00', '06:30', '07:00', '07:30', '08:00', '08:30', '09:00', '09:30', '10:00', '10:30', '11:00', '11:30'],
        datasets: [{
            label: 'Temperature (°C)',
            data: [20, 21, 22, 23, 24, 25], // Sample temperature data
            borderColor: 'rgb(255, 99, 132)',
            fill: false
        }, {
            label: 'Humidity (%)',
            data: [50, 55, 60, 65, 70, 75], // Sample humidity data
            borderColor: 'rgb(54, 162, 235)',
            fill: false
        }]
    },
    options: {
        responsive: true,
        scales: {
            yAxes: [{
                ticks: {
                    beginAtZero: true
                }
            }]
        }
    }
});

return lineChart;
}

// Function to update the line chart with new data
function updateChart(lineChart, temperatureData, humidityData) {
// Update line chart data (update only the first dataset for demonstration)
lineChart.data.datasets[0].data.push(temperatureData);
lineChart.data.datasets[1].data.push(humidityData);
lineChart.data.labels.push('...');
lineChart.update();
}

// Sample data for demonstration
var moistureData = 50; // Example: Moisture percentage
var temperatureData = 25; // Example: Temperature in Celsius
var humidityData = 60; // Example: Humidity percentage

// Update data values
document.getElementById('moisture-value').textContent = moistureData + '%';
document.getElementById('temperature-value').textContent = temperatureData + '°C';
document.getElementById('humidity-value').textContent = humidityData + '%';

// Initialize the line chart
var lineChart = initializeChart();

// Simulate updating data values every 20 seconds (for demonstration purposes)
setInterval(function() {
// Update sample data
moistureData = Math.floor(Math.random() * 100); // Random moisture value
temperatureData = Math.floor(Math.random() * 30) + 20; // Random temperature value between 20 and 50
humidityData = Math.floor(Math.random() * 50) + 50; // Random humidity value between 50 and 100

// Update displayed data values
document.getElementById('moisture-value').textContent = moistureData + '%'; 
document.getElementById('temperature-value').textContent = temperatureData + '°C';
document.getElementById('humidity-value').textContent = humidityData + '%';

// Update the line chart with new data
updateChart(lineChart, temperatureData, humidityData);
}, 20000); // Update every 20 seconds
