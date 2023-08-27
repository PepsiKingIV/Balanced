var ctx = document.getElementById('myChart').getContext('2d');
var myChart = new Chart(ctx, {
    type: 'doughnut',
    data: {
        labels: ['п', 'е', 'д', 'и', 'к'],
        datasets: [{
            data: [27.92, 17.53, 14.94, 26.62, 12.99],
            backgroundColor: ['#FFBA08', '#3772FF', '#136F63', '#D00000', '#5F0F40'],
            borderWidth: 0 ,
            borderColor: '#ddd'
        }]
    },
    options: {
        title: {
            display: true,
            text: 'Доход',
            position: 'top',
            fontSize: 16,
            fontColor: '#fff',
            padding: 20,
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