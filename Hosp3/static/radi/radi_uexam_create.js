var url =window.location.href         // ok
var csrf = document.getElementsByName("csrfmiddlewaretoken")[0].value    // ok

$('#result-box').hide();
$('#submit-uexam-form').hide();
$("#submit-uexam-item-form").hide()
$("#card-exam-item").hide()


search();
submitExamItem();
categoryChange();
displayCreateExam();
displayCreateEchoTest();

var now = new Date();


var sendSearchInputValue = (searchText) => {        // searchText = e.target.value
    qt = $('#query-type').val()
    if (searchText.length > 3){
        $('#table-output').innerHTML = ""
        $('#result-box').show();
        fetch("../search_echo_patient/", {
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
                    row.append($('<td class="class1"></td>').html(rowData.un));
                    row.append($('<td class="class1"></td>').html(rowData.sn));
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
                    });

                return row;
                });

                $("#result-table").append(rows);

                function fillForm(rowData) {
                    $('#result-box').hide();
                    $('#id_patient').val(rowData.un);
                }

            }
        });

    }else{
        $('#result-box').hide();
    }
}


$(document).on('click', '#submit-update-exam', function(e) {
    e.preventDefault();
    console.log($('#id_patient').val())
    console.log($('#id_pres').val())
    console.log($('#id_uexam').val())
    console.log($('#id_uexam2').val())
    console.log($('#id_ward').val())

    if ($('#id_ex').val() !== "") {
        $.ajax({
            type: 'post',
            url: '../u_examupdate/' + $('#id_uexam').val(),
            data: {
                csrfmiddlewaretoken: csrf,
                book_num:$('#id_uexam').val(),
                book_num2:$('#id_uexam2').val(),
                prescriber:$('#id_pres').val(),
                ward:$('#id_ward').val(),
                patient:$('#id_patient').val(),
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


function search(e) {
    return $("#search-exam").on('keyup', function(e){
        sendSearchInputValue(e.target.value)
    });
};


$('#id_book_num').focusout(function() {
    console.log("bn2")
    if ($('#id_book_num').val() !== "") {
        var bn = zeroPad($('#id_book_num').val())
        checkExamNum(bn);
    } else {
        $('#id_book_num').focus()
        console.log("empty Book num field")
    }
})


$('#id_paid_exam_item').focusout(function() {
    if ($('#id_paid_exam_item').val() == "") {
        alert("Empty Paid field")
        $('#id_paid_exam_item').focus();
    } else if ($('#id_paid_exam_item').val().length < 4) {
        alert("Not Valid Paid Amount")
    } else if (!$.isNumeric($('#id_paid_exam_item').val())) {
        alert("Not Valid Paid Amount")
    }
})


$('#submit-uexam-form').on('click', function(e) {
    e.preventDefault();
    if ($('#id_book_num').val() !== "") {
        var bn = zeroPad($('#id_book_num').val())
        console.log($('#id_book_num').val())
        console.log(bn)
        checkRegNum2(bn);
    } else {
        alert("Enter Book Number")
    }

});


function zeroPad(r_n) {
    var zero = 5 - r_n.toString().length + 1;
    var res = Array(+(zero > 0 && zero)).join("0") + r_n
    return 'U' + res + '_' + (now.getFullYear()).toString().slice(2, 4);
}


function createExam(bn) {
    $.ajax({
        type: 'post',
        url: '/radi/u_examcreate/',
        data: {
            csrfmiddlewaretoken: csrf,
            book_num: $('#id_book_num').val(),
            book_num2: bn,
            patient:$('#id_patient').val(),
            ward:$('#id_ward').val(),
            prescriber:$('#id_prescriber').val().toUpperCase(),
        },
        success: function(res){
            console.log(res)
            console.log(res['data'])
            if (res['data'] == "SAVED") {
                console.log('saved exam')
                $("#card-exam").hide()
                $("#id_uexam").val(res['info'][0])
                $("#card-exam-item").show()
                alert(res['info'][0] + " REGISTERED SUCCESSFULLY !!!")
            } else if (res['data'] == "EXIST ALREADY") {
                console.log('duplicate')
                $("#card-exam").hide()
                $("#id_uexam").val(res['info'][0])
                $("#card-exam-item").show()
                alert(res['info'][0] + " REGISTERED SUCCESSFULLY !!!")
            } else if (res['data'] == "NOT TRAPPED") {
                console.log('trapped')
                alert($('#id_book_num').val() + " - " + res['data'] + "!!!")
            } else if (res['data'] == "NOT VALID") {
                console.log('not valid')
                alert($('#id_book_num').val() + " - " + res['data'] + "!!!")
            }
        }
    })
    return false;
}


function submitExamItem (e) {
    $(document).on('click', '#submit-uexam-item-form', function(e) {
        e.preventDefault();
        console.log("uexam  submit clicked")
        if ($('#id_paid_exam_item').val() !== "" && $.isNumeric($('#id_paid_exam_item').val())) {
            sendForm2();
        } else {
            alert("AMOUNT PAID NOT VALID")
        }
    });
};


function sendForm2 () {
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


function displayCreateExam(e) {
    $('#id_ward').on('change', function(e) {
        e.preventDefault();
        console.log('ward changed')
        $('#submit-uexam-form').show();
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


function checkExamNum(bn){
    $.ajax({
        type: 'post',
        url: '/radi/checkBookNum/',
        data: {
            csrfmiddlewaretoken: csrf,
            book_num: bn,
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


function checkRegNum2(bn){
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
                createExam(bn);
            } else if (res == "TAKEN") {
                console.log('taken')
                alert('REG NUMBER USED ALREADY')
            }
        }
    })
}