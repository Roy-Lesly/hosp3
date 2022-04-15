//var csrf   = document.getElementsByName("csrfmiddlewaretoken")[0].value    // ok
var csrf = $("[name=csrfmiddlewaretoken]").val()//[0].value    // ok
var months = ["JANUARY", "FEBUARY", "MARCH", "APRIL", "MAY", "JUNE","JULY", "AUGUST", "SEPTEMBER", "OCTOBER", "NOVEMBER", "DECEMBER"]


call()


function call() {
    $.ajax({
        url: "../echo_tests_stats_1_this_year/",
        type: "GET",
        data: {},
        method: "GET",
        success: function (res) {
            //console.log(res)
            console.log(res[0])
            //res = res[0]
            statsValues1(res[0]);
            //statsValues2(res[1]);
        },
        complete: function() {
            setTimeout(call, 60000);
        },
        error: function (res) {
        }
    });
}


function statsValues1(data){
    var title = [], title_value = []
    var mthly_title = [], mthly_title_value = []
    var test_name = [], test_name_value = [], test_name_list = []
    var test_values_list = []
    var dic = {}

    //console.log(data)
    $.each(data, function(key, value){              // OK
        title.push(key)
        title_value.push(value)
    });
    //console.log(title)
    //console.log(title_value)
    var i = 0;
    $.each(title_value[0], function(key, value){    // OK
        test_name.push(key)
        test_values_list.push(test_name[i])
        i++;
    });
    console.log(test_name)
    console.log(test_values_list)

    $.each(title_value[2], function(key, value){    // OK
        test_name_value.push(value)
        var key = []
        test_name_list.push(key)
    });
    console.log(test_name_value)
    var w = 0;
    $.each(test_name_value, function(){    // OK
        dic[test_values_list[w]] = []
        var x = 0;
        $.each(test_name_value[w], function(key, value){
            dic[test_values_list[w]].push(value)
            x++;
        })
        w++;
    });
    console.log(dic)
    var p = 1;
    $.each(test_values_list, function(){
        $('#test_' + p.toString()).html(test_values_list[p-1]);
        p++;
    })
    var q = 0;
    $.each(dic, function(){
        var r = 1;
        $.each(dic[test_values_list[q]], function(){
            $('#test_' + (q+1).toString() + '_' + r.toString()).html(dic[test_values_list[q]][r-1]);
            r++;
        });
        q++;
    });
}


// ============== PRINTING BUTTONS =================
$('#this_month_stats_btn').on('click', function(e){
    console.log("button1")
    e.preventDefault()
    thisMonthStats();
});


$('#last_month_stats_btn').on('click', function(e){
    console.log("button2")
    e.preventDefault()
    lastMonthStats();
});


$('#this_year_stats_btn').on('click', function(e){
    console.log("button3")
    e.preventDefault()
    thisYearStats();
});


$('#last_year_stats_btn').on('click', function(e){
    console.log("button4")
    e.preventDefault()
    lastYearStats();
});


$('#gen_stats').on('click', function(e){
    e.preventDefault()
    if ($('#stats_month').val() != "") {
        if ($('#stats_year').val() != "") {
            generateStats();
        } else
            alert("Enter Year For Statistics");
    } else
        alert("Select Month For Statistics");

});


function thisMonthStats(){
    console.log("called")
    $.ajax({
        url: '../../radi/u_this_month_stats/',
        type: "GET",
        data: {},
        method: "GET",
        success: function (res) {
            if (res == "NOT TAKEN") {
                createRegisPat(rn);
                console.log('not taken')
            } else if (res == "TAKEN") {
                console.log('taken')
                alert('REG NUMBER USED ALREADY')
            }
        }
    })
}


function generateStats(){
    console.log("Generate Stats Clicked")
    console.log($('#stats_month').val())
    console.log($('#stats_year').val())
    $.ajax({
        type: 'post',
        url: '/radi/u_gen_stats/',
        data: {
            csrfmiddlewaretoken: csrf,
            month:$('#stats_month').val(),
            year:$('#stats_year').val(),
        },
        success: function(res){
            console.log(res)
            if (res['data'] == "SAVED") {
                $('#card-patient').hide()
                $("#card-exam").show()
                $("#id_patient").val(res['patient'][0])
                $("#id_book_num").val(res['patient'][2])
                alert(res['patient'][2] + " REGISTERED SUCCESSFULLY !!!")
                console.log('upat-form submitted')
            } else {
                console.log(res)
                alert($('#stats_year').val() + " " + $('#stats_month').val() + " - " + res + "!!!")
            }
        }
    })
    return false;
}