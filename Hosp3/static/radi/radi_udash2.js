
call()


function call() {
    $.ajax({
        url: "../echo_tests_stats_2_this_year/",
        type: "GET",
        data: {},
        method: "GET",
        success: function (res) {
            //console.log(res[0])
            console.log(res[1])
            //res = res[0]
            statsValues1(res[0]);
            statsValues2(res[1]);
        },
        complete: function() {
            setTimeout(call, 10000);
        },
        error: function (res) {
        }
    });
}


function statsValues1(data){
    var title = [], title_value = []
    var mthly_title = [], mthly_title_value = []
    var qtly_name = [], mthly_name = []
    var qtly_list = [], mthly_list = [], test_month = []
    console.log(data)
    $.each(data, function(key, value){              // OK
        title.push(key)
        title_value.push(value)
    });
    $.each(title_value[2], function(key, value){    // OK
        mthly_title.push(key)
        mthly_title_value.push(value)
    });
    console.log(mthly_title)

}

function statsValues2(data){
    console.log(data)
    var title = [], title_value = []
    var mthly_title = [], mthly_title_value = []
    var test_name = [], test_name_value = []
    var age_title = [], age_title_value = []
    var sex_title = [], male_list = [], female_list = []
    var sex_title_value = [], male_list_value = [], female_list_value = []
    sex_title.push(male_list)
    sex_title_value.push(male_list)
    sex_title.push(female_list)
    sex_title_value.push(female_list)
    sex = ['MALE', 'FEMALE']

    $.each(data, function(key, value){                  // OK
        title.push(key)
        title_value.push(value)
    });
    console.log(title)
    $.each(title_value[2], function(key, value){        // OK
        test_name.push(key)
        test_name_value.push(value)
    });
    console.log(test_name)
    var w = 0;
    $.each(test_name_value[w], function(key, value){    // OK
        age_title.push(key)
        age_title_value.push(value)
        w++;
    });
    var w = 0;
    $.each(age_title_value, function() {                // OK
        $('.a' + (w+1)).html(age_title[w])
        var x = 0;
        $.each(age_title_value[w],function(key, value) {
            sex_title_value[x].push(value)
            x++;
        });
        w++;
    });
    console.log(age_title)
    console.log(male_list)
    console.log(female_list)
    console.log(sex_title_value)
    var q = 1;
    console.log(test_name)
    console.log(title)
    $.each(test_name, function(key, value){
        $('#test_' + q.toString()).html(test_name[q-1]);
        //console.log('#test_' + q.toString())
        q++
    })
    $('.s1').html('M');
    $('.s2').html('F');

    var n = 0;
    $.each(title, function(key, value){
        $('.' + title[n]).html(title[n])
        n++;
    });

    console.log(data[title[0]])
    var q = 1;
    elt2= [1,2]
    elt3 = [1,2,3]
    elt5 = [1,2,3,4,5]
    elt12 = [1,2,3,4,5,6,7,8,9,10,11,12]
    $.each(elt2, function(key, value){
        //$('.a' + q.toString()).html(age_title[q-1]);
        //console.log('a' + q.toString())
        var w = 1;
        $.each(title, function(key, value){
            $('' + w.toString()).html(test_name[q-1]);
            var x = 1;
            $.each(test_name, function(){
                $('.a' + x.toString()).html(age_title[x-1]);
                $('' + w.toString()).html(test_name[q-1]);
                var y = 1;
                $.each(age_title, function(){
                    $('' + w.toString()).html(test_name[q-1]);
                    var z = 1;
                    $.each(sex, function(){
                        $('#test_' + w.toString() + '_' + x.toString() + '_' + y.toString() + '_' + z.toString()).html(data[title[w-1]][test_name[x-1]][age_title[y-1]][sex[z-1]]);
                        z++;
                    });
                    y++;
                });
                x++;
            });
            w++;
        });
        q++;
    })
}