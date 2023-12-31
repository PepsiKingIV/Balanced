function loadJson(selector) {
    return JSON.parse(document.querySelector(selector).getAttribute('data-json'));
  }
  

window.onload = function () {
    const xValues = ["Italy", "France", "Spain", "USA", "Argentina"];
    const yValues = [55, 49, 44, 24, 15];
    const barColors = ["red", "green","blue","orange","brown"];


    new Chart("Chart_1", {
    type: 'doughnut',
    data: {
        labels: ['П', 'е', 'д', 'ик'],
        datasets: [{
            data: [1, 1, 1, 2],
            backgroundColor: ['#D00000', '#FFBA08', '#136F63', '#3772FF'],
            borderWidth: 5 ,
            borderColor: '#000'
        }]
    },
    options: {
        title: {
            display: true,
            text: 'Доходы',
            position: 'top',
            fontSize: 16,
            fontColor: '#fff',
            padding: 20
        },
        legend: {
            display: true,
            position: 'bottom',
            labels: {
                boxWidth: 20,
                fontColor: '#fff',
                padding: 15
            }
        },
        tooltips: {
            enabled: false
        },
        plugins: {
            datalabels: {
                color: '#fff',
                textAlign: 'center',
                font: {
                    lineHeight: 1.6
                },
                formatter: function(value, ctx) {
                    return ctx.chart.data.labels[ctx.dataIndex] + '\n' + value + '%';
                }
            }
        }
    }
});
new Chart("Chart_2", {
    type: 'doughnut',
    data: {
        labels: ['П', '1', '2', '3'],
        datasets: [{
            data: [1.3, 0.5, 2, 2],
            backgroundColor: ['#D00000', '#FFBA08', '#136F63', '#3772FF'],
            borderWidth: 5 ,
            borderColor: '#000'
        }]
    },
    options: {
        title: {
            display: true,
            text: 'Доходы',
            position: 'top',
            fontSize: 16,
            fontColor: '#fff',
            padding: 20
        },
        legend: {
            display: true,
            position: 'bottom',
            labels: {
                boxWidth: 20,
                fontColor: '#fff',
                padding: 15
            }
        },
        tooltips: {
            enabled: false
        },
        plugins: {
            datalabels: {
                color: '#fff',
                textAlign: 'center',
                font: {
                    lineHeight: 1.6
                },
                formatter: function(value, ctx) {
                    return ctx.chart.data.labels[ctx.dataIndex] + '\n' + value + '%';
                }
            }
        }
    }
});}
const DATA_COUNT = 7;
const labels = [];
for (let i = 0; i < DATA_COUNT; ++i) {
  labels.push(i.toString());
}

new Chart("Chart_3", {
    type: 'line',
    data: {
        labels: debitlabels,
        datasets: [{
            label: 'Доход',
            data: debitData,
            borderColor: "#3772FF",
            fill: false,
            cubicInterpolationMode: 'monotone',
            tension: 0.4
          }]
    },
    options: {
        responsive: true,
        plugins: {
            title: {
              display: true,
              text: 'Chart.js Line Chart - Cubic interpolation mode'
            },
          },
        interaction: {
            intersect: false,
        },
        scales: {
            x: {
                display: true,
                title: {
                    display: true
                }
            },
            y: {
                display: true,
                title: {
                display: true,
                text: 'Value'
                },
                suggestedMin: -10,
                suggestedMax: 200
            }
        }
    }
});

new Chart("Chart_4", {
    type: 'line',
    data: {
        labels: creditlabels,
        datasets: [{
            label: 'Расход',
            data: creditData,
            borderColor: "#3772FF",
            fill: false,
            cubicInterpolationMode: 'monotone',
            tension: 0.4
          }]
    },
    options: {
        responsive: true,
        plugins: {
            title: {
              display: true,
              text: 'Chart.js Line Chart - Cubic interpolation mode'
            },
          },
        interaction: {
            intersect: false,
        },
        scales: {
            x: {
                display: true,
                title: {
                    display: true
                }
            },
            y: {
                display: true,
                title: {
                display: true,
                text: 'Value'
                },
                suggestedMin: -10,
                suggestedMax: 200
            }
        }
    }
});

