var url =window.location.href         // ok
var csrf = document.getElementsByName("csrfmiddlewaretoken")[0].value    // ok

$('#result-box').hide();
$("#submit-uexam-item-form").hide()
$("#card-exam-item").hide()


search();
submitExamItem();
categoryChange();
displayCreateEchoTest();
queryPlaceHolder();

var now = new Date();


var sendSearchInputValue = (searchText) => {        // searchText = e.target.value
    qt = $('#query-type').val()
    if (searchText.length > 3){
        $('#table-output').innerHTML = ""
        $('#result-box').show();
        fetch("../search_echo_exam/", {
            body: JSON.stringify({
                searchText: searchText,
                queryType: qt
            }),
            method: "POST",
        })
        .then((res) => res.json())
        .then((data) => {

            if (data.length===0){
                $('#card-test').hide()
                $('#result-box').removeClass('not-visible')
                $('#result-table-body').empty().html("No Results Found !!!")

            }else{
                $('#card-test').hide()
                $('#result-box').removeClass('not-visible')
                $('#result-table-body').html('')
                var i = 0;
                var rows = $.map(data[0], function(rowData) {
                    var row = $("<tr></tr>");
                    row.append($('<td class="class1"></td>').html(rowData.sn));
                    row.append($('<td class="class1"></td>').html(rowData.un));
                    row.append($('<td class="class1"></td>').html(rowData.bn));
                    row.append($('<td class="class1"></td>').html(rowData.full_name));
                    row.append($('<td class="class3"></td>').html(rowData.age));
                    row.append($('<td class="class4"></td>').html(rowData.sex));
                    row.append($('<td class="class4"></td>').html(rowData.address));
                    row.append($('<td class="class4"></td>').html(rowData.Phone));
                    row.append($('<td class="class4"></td>').html(rowData.date_created));

                    row.on("click", function() {
                      fillForm(rowData);
                      $('#result-box').hide();
                      $('#card-search').hide();
                      $('#card-test').hide();
                      $('#card-exam-item').show();
                    });

                return row;
                });

                $("#result-table").append(rows);

                function fillForm(rowData) {
                    $('#result-box').hide();
                    $('#id_uexam').val(rowData.bn);
                }

            }
        });

    }else{
        $('#result-box').hide();
    }
}


function search(e) {
    return $("#search-exam").on('keyup', function(e){
        sendSearchInputValue(e.target.value)
    });
};


function submitExamItem (e) {
    $(document).on('click', '#submit-uexam-item-form', function(e) {
        e.preventDefault();
        console.log("uexam  submit clicked")
        if ($('#id_paid_exam_item').val() !== "" && $.isNumeric($('#id_paid_exam_item').val())) {
            createExamItem();
        } else {
            alert("AMOUNT PAID NOT VALID")
        }
    });
};


function createExamItem () {
    if ($('input[name=book_num2]').val() !== "") {
        if ($('input[name=paid-exam-item]').val() !== "") {
            console.log($('input[name=paid-exam-item]').val())
            if ($('#ltype').val() !== "") {
                $.ajax({
                    type: 'post',
                    url: '/radi/u_examitemcreate/',
                    data: {
                        csrfmiddlewaretoken: csrf,
                        uexam:$('#id_uexam').val(),
                        utype:$('#id_utype').val(),
                        paid:$('input[name=paid-exam-item]').val(),
                    },
                    success: function(res){
                        console.log(res['data'])
                        if (res['data'] == "SAVED") {
                            console.log('saved exam')
                            alert($('#id_utype').val() + " REGISTERED SUCCESSFULLY !!!")
                            alert("REGISTER NEXT PROCEDURE !!!")
                            $("#submit-uexam-item-form").hide()
                        } else if (res['data'] == "DUPLICATE") {
                            console.log('duplicate')
                            $("#submit-uexam-item-form").hide()
                            alert("REGISTER NEXT PROCEDURE !!!")
                        } else if (res['data'] == "TRAPPED") {
                            console.log('trapped')
                        } else if (res['data'] == "EXIST ALREADY") {
                            alert("EXIST ALREADY !!!")
                        }
                    }
                });
            }
            else
                alert("Enter Lab Test")
        }
        else
            alert("Enter Lab Test Amount")
    }
    else
        alert("Enter Book Num")
};


$(document).on('click', '#submit-update-exam-item', function(e) {
    e.preventDefault();
    console.log($('#id_uexam').val())
    console.log($('#id_utype').val())
    console.log($('#id_paid').val())
    console.log($('#id_id').val())

    if ($('#id_ex').val() !== "") {
        $.ajax({
            type: 'post',
            url: '../u_examitemupdate/' + $('#id_id').val(),
            data: {
                csrfmiddlewaretoken: csrf,
                uexam:$('#id_uexam').val(),
                paid:$('#id_paid').val(),
                utype:$('#id_utype').val(),
            },
            success: function(res){
                console.log(res)
                if (res == "EXAM UPDATED") {
                    alert("Echo Exam - " + $('#id_ex').text() + " Exam Updated!!!")
                } else {
                    alert("Echo Exam - " + $('#id_ex').text() + " Result Not Updated!!!")
                }
            }
        })
    }
    else
        console.log("Enter Book Number")
})


function categoryChange(e) {
    $('#id_category').on('change', function(e) {
        e.preventDefault();

        $.ajax({
            type: 'post',
            url: '/radi/search_echo_test/',
            data: {
                csrfmiddlewaretoken: csrf,
                category: $('#id_category').val(),
            },
            success: function(res){
                console.log(res)
                if (res == "") {
                    console.log("No results")
                } else {
                    var optionRow = '<option value="">---------</option>';
                    res.forEach(function (object) {
                        object.forEach(function (item) {
                            optionRow += `<option value="${item.id}">${item.type_name}</option>`
                        });
                    });
                    $("#id_utype").html(optionRow);
                }
            }
        })
    });
};


function displayCreateEchoTest(e) {
    $('#id_utype').on('change', function(e) {
        e.preventDefault();
        $('#submit-uexam-item-form').show();
    });
};


function checkRegNum(bn){
    $.ajax({
        type: 'post',
        url: '/radi/checkRegNum/',
        data: {
            csrfmiddlewaretoken: csrf,
            reg_num: bn,
        },
        success: function(res){
            if (res == "NOT TAKEN") {
                console.log('not taken')
            } else if (res == "TAKEN") {
                console.log('taken')
                alert('REG NUMBER USED ALREADY')
            }
        }
    })
}


function queryPlaceHolder(e) {
    $('#query-type').on('change', function() {
        var qt = $('#query-type').val()
        console.log('Query changed')
        console.log(qt)
        if (qt == "Phone"){
            $("#search-exam").attr("placeholder", "9 Digits")
            $("#search-exam").attr("maxlength", "9")
        } else if (qt == "book_num"){
            $("#search-exam").attr("placeholder", "e.g 3210 or U03210")
            $("#search-exam").attr("maxlength", "8")
        }
    });
};