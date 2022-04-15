


call()


function call() {
    $.ajax({
        url: "../echo_exams_stats_0_this_month/",
        type: "GET",
        data: {},
        method: "GET",
        success: function (res) {
            console.log(res)
            stats_0_1(res);
            statsValues1(res);
        },
        complete: function() {
        },
        error: function (res) {
        }
    });
}


function stats_0_1(data) {
    console.log(data)
    var d1 = [], d2 = []
    $.each(data, function(key, value){
        d1.push(key)
        d2.push(value)
    })
    console.log(d2.length-3)
    var chart_p = new CanvasJS.Chart("daily-bar-chart", {
        title:{
            text: "Echography Daily Statistics For This Month"
        },
        data: [{
            type: "column",
            dataPoints: [],
        },{
            type: "line",
            dataPoints: [],
        }]
    });


    function updateChart() {
        var dps = chart_p.options.data[0].dataPoints;
        var dps2 = chart_p.options.data[1].dataPoints;
        for (var i = 0; i < d2.length-3; i++) {
            // chart_color = d1[i] <= 2 ? "#FC2500" : d1[i] >= 3 ? "#FB6010" : d1[i] >= 6 ? "#AB8E23" : d1[i] >= 9 ? "#6B8E23" : null;
            chart_color = "#6B8E23"
            chart_color2 = "#1A1A1A"
            dps[i] = {label: d1[i] , y: d2[i], color: chart_color};
            dps2[i] = {label: d1[i] , y: d2[i]/2, color: chart_color2};
        }
        chart_p.options.data[0].dataPoints = dps;
        chart_p.render();
    };

    updateChart();

}


function statsValues1(data){
    var days = []; var counts = []
    $.each(data, function(key, value){
        counts.push(value)
        days.push(key)
    })
    console.log(data)
    console.log(days)
    console.log(counts)
    var i = 0; var j = 0;
    $.each(counts, function(){
        $('#'+days[i]).html(counts[i]);
        if (counts[i] != 0){
            j++;
        }
        i++;
    })
    var i = 0; var k = 1; var j = 0;
    $.each(counts[counts.length - 1], function(){
        $('#A'+ k).html(counts[counts.length - 1][i]);
        if (counts[counts.length - 1][i] != 0){
            j++;
        }
        i++; k++;
    })
    console.log(counts[counts.length - 1])
    console.log(j)
    $('#AT').html(counts[counts.length - 1][counts.length - 3]);
    $('#tot').html(data["tot"]);
    $('#tdays').html(j-1);
    $('#av').html((data["tot"]/(j-1)).toFixed(1));
    $('#id_month').html(data["month"]);
}


function chart2(data_month2) {
    var d1 = [], d2 = []
    $.each(data_month2, function(key, value){
        d1.push(key)
        d2.push(value)
    })
    var chart_e = new CanvasJS.Chart("exam-bar-chart", {
        title:{
            text: "Echography Monthly New Exams Statistics"
        },
        data: [{
            type: "column",
            dataPoints: [],
        }]
    });


    function updateChart() {
        var dps = chart_e.options.data[0].dataPoints;
        for (var i = 0; i < 12; i++) {
            chart_color = d1[i] <= 2 ? "#FC2500" : d1[i] >= 3 ? "#FB6010" : d1[i] >= 6 ? "#AB8E23" : d1[i] >= 9 ? "#6B8E23" : null;
            dps[i] = {label: d1[i] , y: d2[i], color: chart_color};
        }
        chart_e.options.data[0].dataPoints = dps;
        chart_e.render();
    };

    updateChart();

}


function statsValues2(data){
    var values = [], qtly = [], mthly = [], d_year = []
    $.each(data, function(key, value){
        d_year.push(key)
        values.push(value)
    })
    $.each(values[1], function(key, value){
        qtly.push(value)
    })
    $.each(values[2], function(key, value){
        mthly.push(value)
    })
    var year = values[0]
    $('#year-total').html(year);
    $('#month-total').html('Adjust!!!');
    $('#e-mth01').html(mthly[0]);
    $('#e-mth02').html(mthly[1]);
    $('#e-mth03').html(mthly[2]);
    $('#e-mth04').html(mthly[3]);
    $('#e-mth05').html(mthly[4]);
    $('#e-mth06').html(mthly[5]);
    $('#e-mth07').html(mthly[6]);
    $('#e-mth08').html(mthly[7]);
    $('#e-mth09').html(mthly[8]);
    $('#e-mth10').html(mthly[9]);
    $('#e-mth11').html(mthly[10]);
    $('#e-mth12').html(mthly[11]);
}