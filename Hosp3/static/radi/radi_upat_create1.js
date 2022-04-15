var csrf = document.getElementsByName("csrfmiddlewaretoken")[0].value    // ok
var searchForm = $("#search-form")  // or var searchForm = document.getElementById("#search-form")
var resultBox = $("#result-box")                // ok
var searchResult = $('.search-results')
var searchFormVal = searchForm.val()            // ok
var searchInput = $("#search-input")            // ok


displayCreateExam();
displayCreateEchoTest();
displayCreateNewUpat();
queryPlaceHolder();


$("#result-box").hide()
$("#card-patient").hide()
$("#card-exam").hide()
$("#card-exam2").hide()
$("#card-exam-item").hide()
$("#submit-uexam-form").hide()
$("#submit-uexam-item-form").hide()
$("#new-upat").hide()

var now = new Date();


$('#search-input').on('keyup', function(e){
    console.log("Typing ...")
    sendSearchInputValue(e.target.value)
});


$('#btn_reg_pat').click(function(){
    console.log("touched")
    $.ajax({
        url: '../../regi/patCreateModalU/',
        type: 'get',
        dataType: 'json',
        beforeSend: function(){
            showModal();
        },
        success: function(data){
            $('#modal-noti .modal-content').html(data.html_form);
        }
    });
});


$('#submit-modal-create-pat').click(function(e){
    e.preventDefault()
    if ($('#id_reg_num_reg').val() !== "") {
        var rn = zeroPad($('#id_reg_num_reg').val())
        checkRegNum2(rn);
    }
});


function zeroPad(r_n) {
    var zero = 5 - r_n.toString().length + 1;
    var res = Array(+(zero > 0 && zero)).join("0") + r_n
    return 'U' + res + '_' + (now.getFullYear()).toString().slice(2, 4);
}


$('#submit-upat-form').click(function(e){
    e.preventDefault()
    createPatient();
});


$('#id_reg_num_reg').focusout(function() {
    console.log('focusin reg num')
    if ($('#id_reg_num_reg').val() !== "") {
        var rn = zeroPad($('#id_reg_num_reg').val())
        console.log(rn)
        checkRegNum(rn);
    } else {
        $('#id_reg_num_reg').focus()
        console.log("empty reg num field")
    }
})


$('#id_first_name_reg').keyup(function() {
    console.log('focusin first name')
    if ($('#id_first_name_reg').val() !== "") {
        var rn = zeroPad($('#id_reg_num_reg').val())
        console.log(rn)
        checkRegNum(rn);
    } else {
        $('#id_first_name').focus();
    }
})


$('#id_last_name_reg').focusout(function() {
    if ($('#id_last_name_reg').val() == "") {
        console.log("Last Name Empty => Ok")
    } else {
        console.log("Last Name not Empty => Ok")
    }
})


$('#id_address_reg').focusout(function() {
    if ($('#id_address_reg').val() == "") {
        $('#id_address_reg').focus();
    } else {
        console.log("Address Not Empty => OK")
    }
})


$('#id_sex').focusout(function() {
    if ($('#id_sex').val() == "") {
        $('#id_sex').focus();
    } else {
        console.log("Sex Not Empty => OK")
    }
})


$('#id_dob_reg').focusout(function() {
    if ($('#id_dob_reg').val() == "") {
        $('#id_dob_reg').focus();
    } else {
        var q = $('#id_dob_reg').val();
        var dob = new Date(q);
        var age = Math.floor((now - dob)/(60 * 60 * 24 * 365.2 * 1000));
        var age1 = (now - dob)/(60 * 60 * 24 * 365.18 * 1000);
        var age2 = Math.ceil(((now - dob)/(60 * 60 * 24 * 365.18 * 1000)) - 0.9235680594412599);
        return $('#id_age_reg').val(age2);
    }
})


$('#submit-uexam-form').on('click', function(e) {
    $("#submit-uexam-form").hide()
    e.preventDefault();
    createExam();
});


$('#submit-uexam-form2').on('click', function(e) {
    $("#submit-uexam-form2").hide()
    e.preventDefault();
    console.log($('#id_book_num2').val())

    var bn = zeroPad($('#id_book_num2').val())
    console.log(bn)
    createExam2(bn);
});


$('#submit-uexam-item-form').on('click', function(e) {
    $("#submit-uexam-item-form").hide()
    e.preventDefault();
    if ($('#id_paid_exam_item').val() !== "" && $.isNumeric($('#id_paid_exam_item').val())) {
        createExamItem(e);
    }
});


$('#id_category').on('change', function(e) {
    e.preventDefault();
    categoryChange();
});


$('#id_book_num2').on('change', function() {
    $("#submit-uexam-form2").show()
});


$('#id_book_num2').focusout(function() {
    console.log('focusin reg num')
    if ($('#id_book_num2').val() !== "") {
        var bn = zeroPad($('#id_book_num2').val())
        console.log(bn)
        checkBookNum(bn);
    } else {
        $('#id_reg_num_reg').focus()
        console.log("empty reg num field")
    }
})


$('#id_utype').on('change', function() {
    $("#submit-uexam-item-form").show()
});


$('#id_paid_exam_item').focusout(function() {
    if ($('#id_paid_exam_item').val() == "") {
        alert("Empty Paid field")
        //$('#id_paid_exam_item').focus();
    } else if ($('#id_paid_exam_item').val().length < 4) {
        alert("Not Valid Paid Amount")
    } else if (!$.isNumeric($('#id_paid_exam_item').val())) {
        alert("Not Valid Paid Amount")
    }
})


function createRegisPat(rn){
    console.log("createRegisPat")
    var fn = $('#id_first_name_reg').val()
    var full_name = fn + " " + $('#id_last_name_reg').val();
    if (fn !== ''){
        checkFullNum(full_name, rn);
    } else {
        alert("Enter First Name") }
}


$(document).on('click', '#submit-update-patient', function(e) {
    e.preventDefault();
    console.log($('#id_first_name').val())
    console.log($('#id_reg_num').val().slice(1,6))
    console.log($('#id_last_name').val())
    console.log($('#id_address').val())
    console.log($('#id_uexam2').val())
    console.log($('#id_phone').val())
    console.log($('#id_dob').val())

    if ($('#id_ex').val() !== "") {
        $.ajax({
            type: 'post',
            url: '../patUpdate/' + $('#id_sn').val(),
            data: {
                csrfmiddlewaretoken: csrf,
                sn:$('#id_sn').val(),
                reg_num:$('#id_reg_num').val().slice(1,6),
                reg_num2:$('#id_reg_num').val(),
                first_name:$('#id_first_name').val(),
                last_name:$('#id_last_name').val(),
                address:$('#id_address').val(),
                sex:$('#id_sex').val(),
                Phone:$('#id_phone').val(),
                dob:$('#id_dob').val(),
            },
            success: function(res){
                console.log(res)
                if (res == "EXAM UPDATED") {
                    alert("Patient - " + $('#id_full_name').text() + " Patient Updated!!!")
                } else {
                    alert("Patient - " + $('#id_full_name').text() + "Patient Not Updated!!!")
                }
            }
        })
    }
    else
        console.log("Enter Book Number")
})


function createPatient(){
    console.log("CREATING UPATIENT ...")
    console.log("sn: " + $('#id_sn').val())
    $.ajax({
        type: 'post',
        url: '/radi/u_patcreate/',
        data: {
            csrfmiddlewaretoken: csrf,
            patient:$('#id_sn').val(),
        },
        success: function(res){
            console.log(res)
            console.log(res["data"])
            if (res['data'] == "SAVED") {
                $('#card-patient').hide()
                $("#card-exam").show()
                $("#id_patient").val(res['patient'][0])
                $("#id_book_num").val(res['patient'][2])
                console.log(res["patient"])
            } else if (res['data'] == "DUPLICATE") {
                //sconsole.log($('#id_sn').val() + " - " + res["data"] + "!!!")
            }
        }
    })
    return false;
}


function createExam(){
    console.log("CREATING EXAM ...")
    console.log("patient: " + $('#id_patient').val())
    console.log("book_num: " + $('#id_book_num').val())
    console.log("ward: " + $('#id_ward').val())
    console.log("prescriber: " + $('#id_prescriber').val())

    $.ajax({
        type: 'post',
        url: '/radi/u_examcreate/',
        data: {
            csrfmiddlewaretoken: csrf,
            book_num:$('#id_book_num').val(),
            book_num2:$('#id_book_num').val(),
            patient:$('#id_patient').val(),
            ward:$('#id_ward').val(),
            prescriber:$('#id_prescriber').val(),
        },
        success: function(res){
            console.log(res['data'])
            if (res['data'] == "SAVED") {
                //console.log('saved exam')
                $("#card-exam").hide()
                $("#id_uexam").val(res['info'][0])
                $("#card-exam-item").show()
            } else if (res['data'] == "DUPLICATE") {
                //console.log('Duplicate')
            } else if (res['data'] == "ALREADY SAVED") {
                //console.log('Already Saved')
            } else if (res['data'] == "NOT VALID") {
                //console.log('not valid form')
            }
        }
    })
    return false;
}


function createExam2(bn){
    console.log("CREATING EXAM 2 ...")
    console.log("patient: " + $('#id_patient').val())
    console.log("patient2: " + $('#id_patient2').val())
    console.log("book_num: " + $('#id_book_num').val())
    console.log("book_num2: " + $('#id_book_num2').val())
    console.log("ward: " + $('#id_ward').val())
    console.log("ward2: " + $('#id_ward2').val())
    console.log("prescriber: " + $('#id_prescriber').val())
    console.log("prescriber2: " + $('#id_prescriber2').val())
    //var bn = zeroPad($('#id_book_num2').val())
    console.log(bn)
    var check = checkBookNum1(bn)
    console.log(check)
    if (check == "TAKEN") {
        focusin($("#id_book_num2"))
    } else if (check == "NOT TAKEN") {
        console.log(bn + " OK")
        $.ajax({
            type: 'post',
            url: '/radi/u_examcreate/',
            data: {
                csrfmiddlewaretoken: csrf,
                book_num: $('#id_book_num2').val(),
                book_num2:bn,
                patient:$('#id_patient2').val(),
                ward:$('#id_ward2').val(),
                prescriber:$('#id_prescriber2').val(),
                //paid:$('#id_paid_uexam2').val(),
            },
            success: function(res){
                console.log(res)
                console.log(res['data'])
                if (res['data'] == "SAVED") {
                    console.log('saved exam')
                    $("#card-exam2").hide()
                    $("#id_uexam").val(bn)
                    $("#card-exam-item").show()
                    //alert(bn + " REGISTERED SUCCESSFULLY !!!")
                    alert("uexam created")
                } else if (res['data'] == "DUPLICATE") {
                    console.log('duplicate')
                    $("#card-exam").hide()
                    $("#id_uexam").val(bn)
                    $("#card-exam-item").show()
                    alert(bn + " REGISTERED SUCCESSFULLY !!!")
                } else if (res['data'] == "NOT VALID") {
                    console.log('not valid')
                    alert($('#id_book_num2').val() + " - " + res['data'] + "!!!")
                } else if (res['data'] == "TRAPPED"){
                    console.log('trapped')
                    alert($('#id_book_num2').val() + " - " + 'EXIST ALREADY' + "!!!")
                }
            }
        })
    }
     
    return false;
}


function createExamItem(){
    console.log("book_num: " + $('#id_uexam').val())
    console.log("UExamItem: " + $('#id_utype').val())
    console.log("paid: " + $('#id_paid_exam_item').val())

    $.ajax({
        type: 'post',
        url: '/radi/u_examitemcreate/',
        data: {
            csrfmiddlewaretoken: csrf,
            uexam: $('#id_uexam').val(),
            paid: $('#id_paid_exam_item').val(),
            utype: $('#id_utype').val(),
        },
        success: function(res){
            console.log(res['data'])
            if (res['data'] == "SAVED") {
                alert($('#id_utype').val() + " REGISTERED SUCCESSFULLY !!!")
                $.ajax({
                    url: '../../radi/patCreateModalDetailU/' + $('#id_uexam').val(),
                    type: 'get',
                    dataType: 'json',
                    beforeSend: function(){
                        $('#modal-reg-pat').modal('show')
                    },
                    success: function(data){
                        $('#modal-reg-pat .modal-content').html(data.html_form);
                    }
                });
                alert("REGISTER NEXT PROCEDURE !!!")
            } else if (res['data'] == "DUPLICATE") {
                /*$.ajax({
                    url: '../../regi/patCreateModalDetailU/' + $('#id_uexam').val(),
                    type: 'get',
                    dataType: 'json',
                    beforeSend: function(){
                        $('#modal-reg-pat').modal('show')
                    },
                    success: function(data){
                        $('#modal-reg-pat .modal-content').html(data.html_form);
                    }
                });*/
                //alert("REGISTER NEXT PROCEDURE !!!")
            } else if (res['data'] == "TRAPPED") {
                console.log('trapped')
                alert("PROCEDURE EXIST ALREADY !!!")
            } else if (res['data'] == "EXIST ALREADY") {
                console.log('exist already')
                alert("PROCEDURE EXIST ALREADY !!!")
            } else if (res['data'] == "NOT VALID") {
                console.log('not valid')
                alert("PROCEDURE DATA NOT VALID !!!")
            }
        }
    })
    return false;
}


function displayCreateExam(e) {
    $('#id_ward').on('change', function(e) {
        e.preventDefault();
        //console.log('ward changed')
        $('#submit-uexam-form').show();
    });
};


function displayCreateEchoTest(e) {
    $('#id_utype').on('change', function(e) {
        e.preventDefault();
        $('#submit-uexam-item-form').show();
    });
};


function displayCreateNewUpat(e) {
    $("#submit-uexam-item-form").on('click', function(e) {
        e.preventDefault();
        $('#new-upat').show();
    });
};


function categoryChange() {
    $.ajax({
        type: 'post',
        url: '/radi/search_echo_test/',
        data: {
            csrfmiddlewaretoken: csrf,
            category: $('#id_category').val(),
        },
        success: function(res){
            //console.log(res)
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
};


function showModal(){
    $('#modal-noti').modal('show')
}


function hideModal(){
    $('#modal-noti').modal('hide')
}


function checkFullNum(full_name, rn){
    console.log(full_name)
    $.ajax({
        type: 'post',
        url: '/radi/checkFullName/',
        data: {
            csrfmiddlewaretoken: csrf,
            full_name: full_name,
        },
        success: function(res){
            if (res == "NOT TAKEN") {
                console.log('not taken')
                if ($('#id_address_reg').val() !== ''){
                    if ($('#id_sex').val() != ''){
                        if ($('#id_dob_reg').val() != ''){
                            console.log($('#id_phone_reg').val())
                            if ($("#id_phone_reg").val() == ""){
                                var p_n = "001" + Math.random().toString().slice(5, 11)
                                console.log(p_n)
                            } else {
                                var p_n = $("#id_phone_reg").val()	
                            }
                            //if ($('#id_phone_reg').val().length != '9'){ //&& $.isNumeric($('#id_phone_reg').val()) && $('#id_phone_reg').val().length == 9){
                                $('#id_phone_reg').show();

                                console.log("CREATING PATIENT ...")
                                console.log("rn: " + $('#id_reg_num_reg').val())
                                console.log("rn_padded: " + rn)
                                console.log("fn: " + $('#id_first_name_reg').val())
                                console.log("ln: " + $('#id_last_name_reg').val())
                                console.log("address: " + $('#id_address_reg').val())
                                console.log("sex: " + $('#id_sex_reg').val())
                                console.log("dob: " + $('#id_dob_reg').val())
                                console.log("age: " + $('#id_age_reg').val())
                                console.log("phone: " + $('#id_phone_reg').val())

                                $.ajax({
                                        url: '../../regi/patCreateModalU/',
                                        type: 'post',
                                        dataType: 'json',
                                        data: {
                                            csrfmiddlewaretoken: csrf,
                                            reg_num: $('#id_reg_num_reg').val(),
                                            reg_num2: rn,
                                            first_name:$('#id_first_name_reg').val(),
                                            last_name:$('#id_last_name_reg').val(),
                                            full_name:'x',
                                            address:$('#id_address_reg').val(),
                                            sex:$('#id_sex').val(),
                                            dob:$('#id_dob_reg').val(),
                                            age:0,
                                            //Phone:$('#id_phone_reg').val(),
					                        Phone: p_n,
                                        },
                                        success: function(res){
                                            console.log(res['data'])
                                            if (res['data'] == 'SAVED') {
                                                console.log(res['patient'])
                                                $("#card-test").hide()
                                                $("#card-exam").hide()
                                                $("#search-box").hide()
                                                $("#result-box").hide()
                                                $("#card-patient").show()
                                                hideModal();
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
                                            } else if (res['data'] == 'FORM INVALID') {
                                                hideModal();
                                                alert(res['data'] + " - Fields May Be Empty !!! (CHECK - Name / Phone / Address)")
                                                showModal();
                                            }
                                        }
                                    });
                            //} else {
                              //  alert("Enter Valid Phone Number") }
                        } else {
                            alert("Enter Date of Birth") }
                    } else {
                        alert("Select Sex") }
                } else {
                    alert("Enter Address") }
            } else if (res == "TAKEN") {
                console.log('taken')
                alert('FIRST AND LAST NAME USED ALREADY')
            }
        }
    })
}


function checkRegNum(rn){
    $.ajax({
        type: 'post',
        url: '/radi/checkRegNum/',
        data: {
            csrfmiddlewaretoken: csrf,
            reg_num: rn,
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


function checkRegNum2(rn){
    console.log($('#id_reg_num_reg').val())
    $.ajax({
        type: 'post',
        url: '/radi/checkRegNum/',
        data: {
            csrfmiddlewaretoken: csrf,
            reg_num: rn,
            reg_num2: rn,
        },
        success: function(res){
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


function checkBookNum(bn){
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
                // createRegisPat(rn);
            } else if (res == "TAKEN") {
                console.log('taken')
                alert('REG NUMBER USED ALREADY')
            }
        }
    })
}


function checkBookNum1(bn){
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
                // createRegisPat(rn);
                return "NOT TAKEN"
            } else if (res == "TAKEN") {
                console.log('taken')
                alert('REG NUMBER USED ALREADY')
                return "TAKEN"
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
            $("#search-input").attr("placeholder", "9 Digits")
            $("#search-input").attr("maxlength", "9")
        } else if (qt == "un"){
            $("#search-input").attr("placeholder", "e.g 00261 or 00265-22")
            $("#search-input").attr("maxlength", "8")
        } else if (qt == "fn"){
            $("#search-input").attr("placeholder", "Full Name")
            $("#search-input").attr("maxlength", "20")
        } else if (qt == "sn"){
            $("#search-input").attr("placeholder", "e.g 22020001")
            $("#search-input").attr("maxlength", "8")
        }
    });
};


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
                console.log(data)
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
                        $('#card-test').hide();
                        $('#search-box').hide();
                        $('#result-box').hide();
                        $("#card-exam").hide()
                        $.ajax({
                            type: 'post',
                            url: '/radi/u_patcreate/',
                            data: {
                                csrfmiddlewaretoken: csrf,
                                patient:rowData.sn
                            },
                            success: function(res){
                                console.log(res)
                                if (res["data"] == "EXIST ALREADY") {
                                    $('#card-patient').hide()
                                    $("#card-exam").hide()
                                    $("#card-exam2").show()
                                    $("#id_patient").val(res['patient'])
                                } else if (res['data'] == "DUPLICATE") {
                                    $('#card-patient').hide()
                                    $("#card-exam").hide()
                                    $("#card-exam2").show()
                                    $("#id_patient").val(res['patient'])
                                } else if (res['data'] == "SAVED") {
                                    $('#card-patient').hide()
                                    $("#card-exam").hide()
                                    $("#card-exam2").show()
                                    $('#id_patient2').val(res['patient'][0]);
                                    $('#id_book_num2').val(res['patient'][2]);
                                } else if (res['data'] == "ONLY PAT EXIST") {
                                    $('#card-patient').show()
                                    $("#card-exam").hide()
                                    $("#card-exam2").hide()
                                    //$('#id_patient2').val(res['patient'][0]);
                                } else if (res['data'] == "PAT and UPAT EXIST") {
                                    $('#card-patient').hide()
                                    $("#card-exam").hide()
                                    $("#card-exam2").show()
                                    $('#id_patient2').val(res['patient'][0]);
                                    $('#id_book_num2').val(res['patient'][2]);
                                } 
                            }
                        });
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

                }
            };
        });        

    }else{
        $('#result-box').hide();
    }
}