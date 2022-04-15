var url =window.location.href         // ok
var searchForm = $("#search-form")  // or var searchForm = document.getElementById("#search-form")
var resultBox = $("#result-box")                // ok
var searchResult = $('.search-results')
var searchFormVal = searchForm.val()            // ok
var searchInput = $("#search-input")            // ok
var csrf = document.getElementsByName("csrfmiddlewaretoken")[0].value    // ok

displayCreateExam();
displayCreateEchoTest();

$("#result-box").hide()
$("#card-exam").hide()
$("#card-exam2").hide()
$("#card-exam-item").hide()
$("#submit-xexam-form").hide()
$("#submit-xexam-item-form").hide()

var now = new Date();


$('#search-input').on('keyup', function(e){
    sendSearchInputValue(e.target.value)
});


$('#btn_reg_pat').click(function(){
    console.log("touched")
    $.ajax({
        url: '../../regi/patCreateModalX/',
        type: 'get',
        dataType: 'json',
        beforeSend: function(){
            $('#modal-reg-pat').modal('show')
        },
        success: function(data){
            $('#modal-reg-pat .modal-content').html(data.html_form);
        }
    });
});


$('#submit-modal-create-pat').click(function(e){
    e.preventDefault()
    var csrf = document.getElementsByName("csrfmiddlewaretoken")[0].value
    console.log($('#id_reg_num_reg').val())
    console.log($('#id_reg_num_reg2').val())
    var reg_num2 = zeroPad($('#id_reg_num_reg').val())
    createRegisPat(reg_num2);
});

function zeroPad(r_n) {
    var zero = 5 - r_n.toString().length + 1;
    var res = Array(+(zero > 0 && zero)).join("0") + r_n
    return 'X' + res + '_' + (now.getFullYear()).toString().slice(2, 4);
}


$('#submit-xpat-form').on('click', function(e) {
    e.preventDefault();
    createPatient(e);
});


$('#submit-xexam-form').on('click', function(e) {
    $("#submit-xexam-form").hide()
    e.preventDefault();
    console.log($('#id_paid_xexam').val())
    createExam(e);
});


$('#submit-xexam-form-2').on('click', function(e) {
    $("#submit-xexam-form2").hide()
    e.preventDefault();
    console.log($('#id_paid_xexam2').val())
    var reg_num2 = zeroPad($('#id_book_num2').val())
    createExam2(reg_num2);
});


$('#submit-xexam-item-form').on('click', function(e) {
    $("#submit-xexam-item-form").hide()
    e.preventDefault();
    createExamItem(e);
});


$('#id_category').on('change', function(e) {
    e.preventDefault();
    categoryChange();
});


function createRegisPat(reg_num2){
    $.ajax({
        url: '../../regi/patCreateModalX/',
        type: 'post',
        dataType: 'json',
        data: {
            csrfmiddlewaretoken: csrf,
            reg_num: $('#id_reg_num_reg').val(),
            reg_num2: reg_num2,
            first_name:$('#id_first_name_reg').val(),
            last_name:$('#id_last_name_reg').val(),
            full_name:'x',
            address:$('#id_address_reg').val(),
            sex:$('#id_sex').val(),
            dob:$('#id_dob_reg').val(),
            age:0,
            Phone:$('#id_phone_reg').val(),
        },
        success: function(res){
            if (res['data'] == 'SAVED') {
                console.log(res['data'])
                console.log(res['patient'])
                $("#card-test").hide()
                $("#card-exam").hide()
                $("#search-box").hide()
                $("#result-box").hide()
                $("#card-patient").show()
                hideModal();
                alert('Patient -' + res['patient'][1] + ' - SUCCESSFULLY SAVED ')
                $('#id_sn').val(res['patient'][0])
                $('#id_full_name_p').val(res['patient'][1])
                $('#id_phone_p').val(res['patient'][4])
                $('#id_address_p').val(res['patient'][2])
                $('#id_age_p').val(res['patient'][3])
            } else if (res['data'] == 'EXIST ALREADY') {
                hideModal();
                alert('Patient - ' + $('#id_reg_num_reg').val() + ' - EXIST ALREADY (Check Reg_num or Phone May)')
                showModal();
            } else if (res['data'] == 'NOT SAVED') {
                hideModal();
                alert('Patient - ' + $('#id_first_name').val() + ' - NOT SAVED (Name or Phone May Already Exist)')
                showModal();
            }
        }
    })
}


function createPatient(){
    console.log($('#id_sn').val())
    $.ajax({
        type: 'post',
        url: '/radi/x_patcreate/',
        data: {
            csrfmiddlewaretoken: csrf,
            patient:$('#id_sn').val(),
        },
        success: function(res){
            console.log(res)

            if (res['data'] == "SAVED") {
                $('#card-patient').hide()
                $("#card-exam").show()
                $("#id_patient").val(res['patient'][0])
                $("#id_book_num").val(res['patient'][2])
                //$("#id_phone_p").val(res['patient'][3])
                alert(res['patient'][2] + " REGISTERED SUCCESSFULLY !!!")
                console.log('xpat-form submitted')
            } else if (res['data'] == "TRAPPED") {
                console.log(res)
                //alert(res['patient'][2] + " DUPLICATE !!!")
            } else if (res['data'] == "NOT SAVED") {
                console.log(res)
                alert(res['patient'][2] + " NOT SAVED !!!")
                alert($('#id_sn').val() + " - " + res + "!!!")
            } else if (res['data'] == "EXIST ALREADY") {
                console.log(res)
            }
        }
    })
    return false;
}


function createExam(){
    $.ajax({
        type: 'post',
        url: '/radi/x_examcreate/',
        data: {
            csrfmiddlewaretoken: csrf,
            book_num:$('#id_book_num').val(),
            patient:$('#id_patient').val(),
            ward:$('#id_ward').val(),
            prescriber:$('#id_prescriber').val(),
            paid:$('#id_paid_xexam').val(),
        },
        success: function(res){
            console.log(res)
            console.log(res['info'][1])
            if (res['data'] == "SAVED") {
                console.log(res['info'][1])
                $("#id_xexam_p").val(res['info'][0])
                $('#card-test').hide()
                $('#card-patient').hide()
                $("#card-exam").hide()

                $("#card-exam-item").show()
                alert(res['info'][0] + " REGISTERED SUCCESSFULLY !!!")
            } else if (res['data'] == "DUPLICATE") {
                console.log(res['info'][1])
            } else if (res['data'] == "NOT VALID") {
                console.log(res['info'][1])
            } else if (res['data'] == "EXIST ALREADY") {
                console.log(res['info'][1])
            } else {
                console.log(res)
            }
        }
    })
    return false;
}


function createExam2(reg_num2){
    $.ajax({
        type: 'post',
        url: '/radi/x_examcreate/',
        data: {
            csrfmiddlewaretoken: csrf,
            book_num:reg_num2,
            patient:$('#id_patient2').val(),
            ward:$('#id_ward2').val(),
            prescriber:$('#id_prescriber2').val(),
            paid:$('#id_paid_xexam2').val(),
        },
        success: function(res){
            console.log(res)
            console.log(res['data'])
            console.log(res['info'])
            if (res['data'] == "SAVED") {
                console.log('saved exam')
                $("#id_xexam_p").val(res['info'][0])
                $("#card-exam2").hide()
                $("#card-exam-item").show()
                alert(res['info'][0] + " REGISTERED SUCCESSFULLY !!!")
            } else if (res['data'] == "DUPLICATE") {
                console.log('duplicate')
                console.log(res['info'][0] + " EXIST ALREADY !!!")
            } else if (res['data'] == "NOT VALID") {
                console.log('not valid')
                alert($('#id_book_num').val() + " - " + res['data'] + "!!!")
            } else if (res['data'] == "EXIST ALREADY") {
                console.log('not saved')
            } else {
                console.log(res)
            }
        }
    })
    return false;
}


function zeroPad2(r_n) {
    var zero = 5 - r_n.toString().length + 1;
    var res = Array(+(zero > 0 && zero)).join("0") + r_n
    return 'X' + res + '_' + (now.getFullYear()).toString().slice(2, 4);
}


function createExamItem(){
    $.ajax({
        type: 'post',
        url: '/radi/x_examitemcreate/',
        data: {
            csrfmiddlewaretoken: csrf,
            xexam:$('#id_xexam_p').val(),
            paid:$('#id_paid_exam_item').val(),
            xtype:$('#id_xtype').val(),
        },
        success: function(res){
            console.log(res['data'])
            if (res['data'] == "SAVED") {
                console.log('saved exam')
                alert($('#id_xtype').val() + " REGISTERED SUCCESSFULLY !!!")
                alert("REGISTER NEXT PROCEDURE !!!")
            } else if (res['data'] == "DUPLICATE") {
                console.log('duplicate')
                alert("REGISTER NEXT PROCEDURE !!!")
            } else if (res['data'] == "TRAPPED") {
                console.log('trapped')
            } else if (res['data'] == "EXIST ALREADY") {
                alert("EXIST ALREADY !!!")
            }
        }
    })
    return false;
}


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


function categoryChange() {
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
};


function showModal(){
    $('#modal-reg-pat').modal('show')
}

function hideModal(){
    $('#modal-reg-pat').modal('hide')
}

var sendSearchInputValue = (searchText) => {
    qt = $('#query-type').val()
    if (searchText.length > 3){
        $("#table-output").innerHTML = ""
        $('#result-box').show();
        fetch("../../regi/search_patient/", {
            body: JSON.stringify({
                searchText: searchText,
                queryType: qt
            }),
            method: "POST",
        })
        .then((res) => res.json())
        .then((data) => {

            //console.log(data)

            if (data.length===0){
                $("#div_no_data").show()
                $("#table-body").html('')
                $("#result-box").removeClass('not-visible')

            }else{
                $("#div_no_data").hide()
                $("#result-box").removeClass('not-visible')
                $("#table-body").html('')
                var i = 0;
                var rows = $.map(data[0], function(rowData) {
                    var row = $("<tr></tr>");
                    row.append($('<td class="class1"></td>').html(rowData.sn));
                    row.append($('<td class="class1"></td>').html(rowData.reg_num));
                    row.append($('<td class="class2"></td>').html(rowData.full_name));
                    row.append($('<td class="class3"></td>').html(rowData.address));
                    row.append($('<td class="class4"></td>').html(rowData.age));
                    row.append($('<td class="class4"></td>').html(rowData.sex));
                    row.append($('<td class="class4"></td>').html(rowData.Phone));
                    row.append($('<td class="class4"></td>').html(rowData.date_created));

                    row.on("click", function() {
                      fillForm(rowData);
                      $('#search-box').hide();
                      $('#card-test').hide();
                      $('#card-patient').hide();
                      $('#result-box').hide();
                      $("#card-exam").hide()
                      $("#card-exam2").show()
                    });

                return row;
                });

                $(".table").append(rows);

                function fillForm(rowData) {
                    var form = $("#id_patient");
                    $('#id_sn').val(rowData.sn);
                    $('#id_full_name_p').val(rowData.full_name);
                    $('#id_phone_p').val(rowData.Phone);
                    $('#id_address_p').val(rowData.address);
                    $('#id_age_p').val(rowData.age);
                    $.ajax({
                           type: 'post',
                           url: '/radi/u_patcreate/',
                           data: {
                               csrfmiddlewaretoken: csrf,
                               csrfmiddlewaretoken: csrf,
                               patient:rowData.sn
                           },
                           success: function(res){
                               console.log(res)
                               console.log(res['patient'])
                               console.log(res['patient'][0])
                               $('#id_patient').val(res['patient'][0]);
                               $('#id_patient2').val(res['patient'][0]);

                              }
                           });
                }

            }
        });

    }else{
        $('#result-box').hide();
    }
}