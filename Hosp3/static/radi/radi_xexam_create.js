var url =window.location.href         // ok
var csrf = document.getElementsByName("csrfmiddlewaretoken")[0].value    // ok

$('#result-box').hide();
$('#submit-uexam-form').hide();
$("#submit-uexam-item-form").hide()
$("#card-exam-item").hide()


search();
submitExam();
submitExamItem();
categoryChange();
displayCreateExam();
displayCreateEchoTest();


var sendSearchInputValue = (searchText) => {        // searchText = e.target.value
    qt = $('#query-type').val()
    if (searchText.length > 3){
        $('#table-output').innerHTML = ""
        $('#result-box').show();
        fetch("../search_xray_patient/", {
            body: JSON.stringify({
                searchText: searchText,
                queryType: qt
            }),
            method: "POST",
        })
        .then((res) => res.json())
        .then((data) => {

            if (data.length===0){
                $('#result-box').removeClass('not-visible')
                $('#result-table-body').empty().html("No Results Found !!!")

            }else{
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


function search (e) {
    return $("#search-exam").on('keyup', function(e){
        sendSearchInputValue(e.target.value)
    });
};


function submitExam (e) {
    $(document).on('click', '#submit-xexam-form', function(e) {
        e.preventDefault();
        console.log("xexam  submit clicked")
        console.log($('#id_paid_exam').val())
        sendForm1();
    });
};


function submitExamItem (e) {
    $(document).on('click', '#submit-xexam-item-form', function(e) {
        e.preventDefault();
        console.log("xexam  submit clicked")
        sendForm2();
    });
};


function sendForm1 () {

    $.ajax({
        type: 'post',
        url: '/radi/x_examcreate/',
        data: {
            csrfmiddlewaretoken: csrf,
            book_num:$('#id_book_num').val(),
            patient:$('#id_patient').val(),
            ward:$('#id_ward').val(),
            prescriber:$('#id_prescriber').val(),
            paid:$('#id_paid_exam').val(),
        },
        success: function(res){
            console.log(res)
            console.log(res['data'])
            if (res['data'] == "SAVED") {
                console.log('saved exam')
                $("#card-exam").hide()
                $("#id_xexam").val(res['info'][0])
                $("#card-exam-item").show()
                alert(res['info'][0] + " REGISTERED SUCCESSFULLY !!!")
            } else if (res['data'] == "DUPLICATE") {
                console.log('duplicate')
                $("#card-exam").hide()
                $("#id_xexam").val(res['info'][0])
                $("#card-exam-item").show()
                alert(res['info'][0] + " REGISTERED SUCCESSFULLY !!!")
            } else if (res['data'] == "NOT VALID") {
                console.log('not valid')
                alert($('#id_book_num').val() + " - " + res['data'] + "!!!")
            } else {
                console.log('not saved')
                alert($('#id_book_num').val() + " - " + res['data'] + "!!!")
            }
        }
    })
    return false;
}


function sendForm2 () {
    if ($('input[name=book_num2]').val() !== "") {
        if ($('input[name=paid-exam-item]').val() !== "") {
            console.log($('input[name=paid-exam-item]').val())
            if ($('#ltype').val() !== "") {
                $.ajax({
                    type: 'post',
                    url: '/radi/x_examitemcreate/',
                    data: {
                        csrfmiddlewaretoken: csrf,
                        uexam:$('#id_xexam').val(),
                        utype:$('#id_xtype').val(),
                        paid:$('input[name=paid-exam-item]').val(),
                    },
                    success: function(res){
                        console.log(res['data'])
                        if (res['data'] == "SAVED") {
                            console.log('saved exam')
                            alert($('#id_xtype').val() + " REGISTERED SUCCESSFULLY !!!")
                            alert("REGISTER NEXT PROCEDURE !!!")
                            $("#submit-xexam-item-form").hide()
                        } else if (res['data'] == "DUPLICATE") {
                            console.log('duplicate')
                            $("#submit-xexam-item-form").hide()
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
                alert("Enter Xray Test")
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
            url: '/radi/search_xray_test/',
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
                    $("#id_xtype").html(optionRow);
                }
            }
        })
    });
};


function displayCreateExam(e) {
    $('#id_ward').on('change', function(e) {
        e.preventDefault();
        console.log('ward changed')
        $('#submit-xexam-form').show();
    });
};


function displayCreateEchoTest(e) {
    $('#id_xtype').on('change', function(e) {
        e.preventDefault();
        $('#submit-xexam-item-form').show();
    });
};
