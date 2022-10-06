var data = {
    labels: [],
    datasets: [{
        label: 'pH',
        backgroundColor: 'rgb(255, 99, 132)',
        borderColor: 'rgb(255, 99, 132)',
        data: [],
    }]
};

var config = {
    type: 'line',
    data: data,
};

var myChart = new Chart(document.getElementById('myChart'), config);



function getData(option=1) {
    $.get("{% url 'ph' %}", {option: option}, function(get_data) {
        length = get_data.data.length;
        var graph_labels = [];
        var graph_data = [];
        for (i = 0; i < length; i++) {
            graph_labels.push(get_data.labels[i]);
            graph_data.push(get_data.data[i]);
        }
        myChart.config.data.datasets[0].data = graph_data
        myChart.config.data.labels = graph_labels
        myChart.update()
    });
}


getData()

$('button').click(function() {
    var option = $('input').val()
    console.log(option)
    getData(option)
});


