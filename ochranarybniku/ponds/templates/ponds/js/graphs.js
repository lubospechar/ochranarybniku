var parameter = $( ".parameter option:selected" ).val()
var agg = $( ".agg option:selected" ).val()


var data = {
    labels: [],
    datasets: [{
        label: '',
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



function getData(options={}) {
    $.get("{% url 'fiedler' %}", options, function(get_data) {
        length = get_data.data.length;
        var graph_labels = [];
        var graph_data = [];
        graph_title = get_data.title
        for (i = 0; i < length; i++) {
            graph_labels.push(get_data.labels[i]);
            graph_data.push(get_data.data[i]);
        }
        myChart.config.data.datasets[0].data = graph_data
        myChart.config.data.labels = graph_labels
        myChart.config.data.datasets[0].label = graph_title
        $('.graph_desc').html(graph_title)
        myChart.update()
    });
}


options = {
    pond: {{ pond.pk }},
    parameter: parameter,
    agg: agg,
}

getData(options)

$('#graph_button').click(function() {
    
    var start_date = $('input[name="start_date"]').val()
    
    options = {
        pond: {{ pond.pk }},
        parameter: $(".parameter option:selected").val(),
        start_date: $('input[name="start_date"]').val(),
        end_date: $('input[name="end_date"]').val(),
        agg: $(".agg option:selected").val()
    }
    getData(options)
    
});




