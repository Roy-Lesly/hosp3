
call()


function call() {
    $.ajax({
        url: "../labo_pats_this_year/",
        type: "GET",
        data: {},
        method: "GET",
        success: function (res) {
            var data_month_p = res[0]['monthly']
            var data_this = res[0]
            statsValues1(data_this);
            chart1(data_month_p);
        },
        complete: function() {
            $.ajax({
                url: "../labo_exams_this_year/",
                type: "GET",
                data: {},
                method: "GET",
                success: function (res) {
                    var data_month_e = res[0]['monthly']
                    var data_this = res[0]
                    statsValues2(data_this);
                    chart2(data_month_e);
                },
                complete: function() {
                    setTimeout(call, 10000);
                },
                error: function (res) {
                }
            });
        },
        error: function (res) {
        }
    });
}


function chart1(data_month1) {
    var d1 = [], d2 = []
    $.each(data_month1, function(key, value){
        d1.push(key)
        d2.push(value)
    })

    var chart_p = new CanvasJS.Chart("pat-bar-chart", {
        title:{
            text: "Laboratory Monthly New Patients Statistics"
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
        for (var i = 0; i < 12; i++) {
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


function chart2(data_month2) {
    var d1 = [], d2 = []
    $.each(data_month2, function(key, value){
        d1.push(key)
        d2.push(value)
    })
    var chart_e = new CanvasJS.Chart("exam-bar-chart", {
        title:{
            text: "Laboratory Monthly New Exams Statistics"
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


function statsValues1(data){
    var values = [], qtly = [], mthly = []
    $.each(data, function(key, value){
        //d_year.push(key)
        values.push(value)
    })
    $.each(values[1], function(key, value){
        qtly.push(value)
    })
    $.each(values[2], function(key, value){
        mthly.push(value)
    })
    console.log(data)
    console.log(qtly)
    console.log(mthly)
    console.log(values)
    var year = values[0]

    $('#year-total').html(year);
    $('#month-total').html('Adjust!!!');
    $('#quarter1-total').html(qtly[0]);
    $('#quarter2-total').html(qtly[1]);
    $('#quarter3-total').html(qtly[2]);
    $('#quarter4-total').html(qtly[3]);
    $('#p-mth01').html(mthly[0]);
    $('#p-mth02').html(mthly[1]);
    $('#p-mth03').html(mthly[2]);
    $('#p-mth04').html(mthly[3]);
    $('#p-mth05').html(mthly[4]);
    $('#p-mth06').html(mthly[5]);
    $('#p-mth07').html(mthly[6]);
    $('#p-mth08').html(mthly[7]);
    $('#p-mth09').html(mthly[8]);
    $('#p-mth10').html(mthly[9]);
    $('#p-mth11').html(mthly[10]);
    $('#p-mth12').html(mthly[11]);
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