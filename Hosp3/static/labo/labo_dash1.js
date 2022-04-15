
call()


function call() {
    $.ajax({
        url: "../labo_tests_stats_this_year/",
        type: "GET",
        data: {},
        method: "GET",
        success: function (res) {
            res = res[0]
            statsValues1(res);
        },
        complete: function() {
            setTimeout(call, 20000);
        },
        error: function (res) {
        }
    });
}


function statsValues1(data){
    var title = []
    var test_name = [], test_year = []
    var test = [], qtly_title = [], mthly_title = []
    var qtly_name = [], mthly_name = []
    var qtly_list = [], mthly_list = [], test_month = []
    console.log(data)
    $.each(data, function(key, value){              // OK
        title.push(key)
    });
    $.each(data[title[0]], function(key, value){    // OK
        test_name.push(key)
        test_year.push(value)
    });
    $.each(data[title[1]], function(key, value){    // OK
        qtly_title.push(value)
    });
    $.each(data[title[2]], function(key, value){    // monthly titles []
        mthly_title.push(value)
    });
    $.each(qtly_title[0], function(key, value){    // quarterly name ['jan_mar', 'apr_jun', ...]
        qtly_name.push(key)
    });
    $.each(mthly_title[0], function(key, value){    // monthly name ['jan', 'feb', ...]
        mthly_name.push(key)
    });
    $.each(qtly_title, function(key, value){
        var i = []
        $.each(value, function(key, value){
            i.push(value)
        });
        qtly_list.push(i)                           // OK
    });
    $.each(mthly_title, function(key, value){
        var j = []
        $.each(value, function(key, value){
            j.push(value)
        });
        mthly_list.push(j)                           // OK
    });

    //console.log(test_year)
    //console.log(test_month)
    console.log(qtly_title)
    console.log(mthly_title)
    console.log(qtly_name)
    console.log(mthly_name)
    console.log(qtly_list)
    console.log(mthly_list)
    console.log(test_name)
    var i = 1, j = 0
    $.each(test_name, function(){
        $('#test_' + (i).toString()).html(test_name[j]);
        i++;
        j++;
    });

    var w = 1, y = 0;
    $.each(test_name, function(){
        var x = 1, z = 0;
        $.each(mthly_list[0], function(){
            $('#test_' + w.toString() + '_' + x.toString()).html(mthly_list[y][z]);
            x++;
            z++;
        });
        w++;
        y++;
    });
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