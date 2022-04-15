function getCookie(name) {
    var cookieValue = null;
    if (document.cookie && document.cookie != '') {
        var cookies = document.cookie.split(';');
        for (var i = 0; i < cookies.length; i++) {
            var cookie = jQuery.trim(cookies[i]);
            // Does this cookie string begin with the name we want?
            if (cookie.substring(0, name.length + 1) == (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}

var csrf = getCookie('csrftoken');
console.log(csrf)

var now = new Date();


$('#card-exam-modal1').hide();

$('#card-exam-item-modal').hide();
$('#card-exam-item-modal1').hide();

$('#noti').on('click', function() {
    console.log("noti2 clicked")
    $.ajax({
        url: '../../radi/notification_items/',
        type: 'get',
        dataType: 'json',
        success: function(data){
            console.log(data)
            console.log(data["info1"])
            $("#info1").text(data["info1"])
            $("#info2").text(data["info2"])
            $("#info3").text(data["info3"])
            $("#info4").text(data["info4"])
            if (data["cont1"] == 0){
                $("#noti1").hide();
            } else if (data["cont2"] == 0){
                $("#noti2").hide();
            } else if (data["cont3"] == 0){
                $("#noti3").hide();
            } else if (data["cont4"] == 0){
                $("#noti4").hide();
            }
            $("#cont1").text(data["cont1"])
            $("#cont2").text(data["cont2"])
            $("#cont3").text(data["cont3"])
            $("#cont4").text(data["cont4"])

            function fillForm(rowData) {
                var form = $("#id_patient");
                $('#id_patient_modal').val(rowData.un);
            }
        }
    });
});


$('#view_1').on('click', function() {
    $.ajax({
        url: '../../radi/patNoExam/',
        type: 'get',
        dataType: 'json',
        beforeSend: function(){
            $('#modal-noti').modal('show')
        },
        success: function(data){
            $('#modal-noti .modal-content').html(data.html_form);
            console.log(data)
            console.log(data.context.data)
            console.log(data.context)
            var optionRow = '<option value="">---------</option>';
                data.context.category.forEach(function (cat) {
                    optionRow += `<option value="${cat}">${cat}</option>`
                });
                $("#id_category_modal").html(optionRow);
                $('#id_category_modal').on('change', function() {
                    console.log("cat changed")
                    categoryChangeModal();
                });

            var rows = $.map(data.context.data, function(rowData) {
                var row = $("<tr></tr>");
                row.append($('<td class="class1"></td>').html(rowData.sn));
                row.append($('<td class="class1"></td>').html(rowData.un));
                row.append($('<td class="class2"></td>').html(rowData.full_name));
                row.append($('<td class="class2"></td>').html(rowData.address));
                row.append($('<td class="class3"></td>').html(rowData.sex));
                row.append($('<td class="class4"></td>').html(rowData.age));
                row.append($('<td class="class4"></td>').html(rowData.Phone));
                row.append($('<td class="class4"></td>').html(rowData.date_created));

                row.on("click", function() {
                    console.log("row clicked")
                    $('#card-exam-modal1').show();
                    $('#pat-table-modal').hide();
                      fillForm(rowData);
                      });
                return row;
            });
            $("#id_tbody").append(rows);
            $('#card-exam-item-modal').hide();

            function fillForm(rowData) {
                var form = $("#id_patient");
                $('#id_patient_modal').val(rowData.un);
            }
        }
    });
});


$('#view_2').on('click', function() {
    $.ajax({
        url: '../../radi/examNoTest/',
        type: 'get',
        dataType: 'json',
        beforeSend: function(){
            $('#modal-noti').modal('show')
        },
        success: function(data){
            $('#modal-noti .modal-content').html(data.html_form);
            console.log(data)
            console.log(data.context.data)
            console.log(data.context)
            var optionRow = '<option value="">---------</option>';
                data.context.category.forEach(function (cat) {
                    optionRow += `<option value="${cat}">${cat}</option>`
                });
                $("#id_category_modal").html(optionRow);
                $('#id_category_modal').on('change', function() {
                    console.log("cat changed")
                    categoryChangeModal();
                });

            var rows = $.map(data.context.data, function(rowData) {
                var row = $("<tr></tr>");
                row.append($('<td class="class1"></td>').html(rowData.id));
                row.append($('<td class="class1"></td>').html(rowData.bn));
                row.append($('<td class="class2"></td>').html(rowData.full_name));
                row.append($('<td class="class3"></td>').html(rowData.address));
                row.append($('<td class="class3"></td>').html(rowData.ward));
                row.append($('<td class="class4"></td>').html(rowData.sex));
                row.append($('<td class="class4"></td>').html(rowData.age));
                row.append($('<td class="class4"></td>').html(rowData.Phone));
                row.append($('<td class="class4"></td>').html(rowData.date_created));

                row.on("click", function() {
                    console.log("row clicked1")
                    $('#exam-table-modal').hide();
                    $('#card-exam-item-modal').show();
                      fillForm(rowData);
                      });
                return row;
            });
            $("#id_tbody").append(rows);
            $('#card-exam-item-modal').hide();

            function fillForm(rowData) {
                var form = $("#id_patient");
                $('#id_uexam_modal').val(rowData.bn);
            }
        }
    });
});


$('#view_3').on('click', function() {
    $.ajax({
        url: '../../radi/obSexMale/',
        type: 'get',
        dataType: 'json',
        beforeSend: function(){
            $('#modal-noti').modal('show')
        },
        success: function(data){
            $('#modal-noti .modal-content').html(data.html_form);
            console.log(data)
            console.log(data.context.data)
            console.log(data.context)
            var optionRow = '<option value="">---------</option>';
                data.context.category.forEach(function (cat) {
                    optionRow += `<option value="${cat}">${cat}</option>`
                });
                $("#id_category_modal").html(optionRow);
                $('#id_category_modal').on('change', function() {
                    console.log("cat changed")
                    categoryChangeModal();
                });

            var rows = $.map(data.context.data, function(rowData) {
                var row = $("<tr></tr>");
                row.append($('<td class="class1"></td>').html(rowData.id));
                row.append($('<td class="class1"></td>').html(rowData.bn));
                row.append($('<td class="class2"></td>').html(rowData.full_name));
                row.append($('<td class="class3"></td>').html(rowData.address));
                row.append($('<td class="class3"></td>').html(rowData.ward));
                row.append($('<td class="class4"></td>').html(rowData.sex));
                row.append($('<td class="class4"></td>').html(rowData.age));
                row.append($('<td class="class4"></td>').html(rowData.Phone));
                row.append($('<td class="class4"></td>').html(rowData.date_created));

                row.on("click", function() {
                    console.log("row clicked1")
                    $('#exam-table-modal').hide();
                    $('#card-exam-item-modal').show();
                      fillForm(rowData);
                      });
                return row;
            });
            $("#id_tbody").append(rows);
            $('#card-exam-item-modal').hide();

            function fillForm(rowData) {
                var form = $("#id_patient");
                $('#id_uexam_modal').val(rowData.bn);
            }
        }
    });
});


$('#view_4').on('click', function() {
    $.ajax({
        url: '../../radi/skippedNumThis/',
        type: 'get',
        dataType: 'json',
        beforeSend: function(){
            $('#modal-noti').modal('show')
        },
        success: function(data){
            $('#modal-noti .modal-content').html(data.html_form);
            console.log(data)
            console.log(data.context.data)
            console.log(data.context)
            var optionRow = '<option value="">---------</option>';
                data.context.category.forEach(function (cat) {
                    optionRow += `<option value="${cat}">${cat}</option>`
                });
                $("#id_category_modal").html(optionRow);
                $('#id_category_modal').on('change', function() {
                    console.log("cat changed")
                    categoryChangeModal();
                });

            var rows = $.map(data.context.data, function(rowData) {
                var row = $("#missing");
                row.append($('<p class="class1"></p>').html(rowData));
                row.append($('<p class="class1"></p>').html("&nbsp"));

                row.on("click", function() {
                    console.log("row clicked1")
                    $('#exam-table-modal').hide();
                    $('#card-exam-item-modal').show();
                      fillForm(rowData);
                      });
                return row;
            });
            $("#id_tbody").append(rows);
            $('#card-exam-item-modal').hide();

            function fillForm(rowData) {
                var form = $("#id_patient");
                $('#id_uexam_modal').val(rowData.bn);
            }
        }
    });
});


$('#id_book_num_modal').focusout(function() {
    if ($('#id_book_num_modal').val() == "") {
        $('#id_book_num_modal').focus()
    } else {
        var r_n = $('#id_book_num_modal').val()
        console.log(r_n)
        var bn = zeroPad($('#id_book_num_modal').val())
        console.log(bn)
        checkExamNum(bn);
    }
})


$('#submit-uexam-form-modal').on('click', function(e) {
    e.preventDefault();
    if ($('#id_book_num_modal').val() !== "") {
        var bn = zeroPad($('#id_book_num_modal').val())
        console.log($('#id_book_num_modal').val())
        console.log(bn)
        createExam(bn);
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
    if ($("#id_ward_modal").val() !== "") {
        $.ajax({
        type: 'post',
        url: '/radi/u_examcreate/',
        data: {
            csrfmiddlewaretoken: csrf,
            book_num: $('#id_book_num_modal').val(),
            book_num2: bn,
            patient:$('#id_patient_modal').val(),
            ward:$('#id_ward_modal').val(),
            prescriber:$('#id_prescriber_modal').val(),
        },
        success: function(res){
            console.log(res)
            console.log(res['data'])
            if (res['data'] == "SAVED") {
                console.log('saved exam')
                $("#card-exam-modal1").hide()
                $("#card-exam-item-modal1").show()
                $("#id_uexam_modal").val(bn)
                $("#card-exam-item").show()
                alert(bn + " REGISTERED SUCCESSFULLY !!!")
            } else if (res['data'] == "EXIST ALREADY") {
                console.log('duplicate')
                $("#card-exam").hide()
                $("#card-exam-item").show()
                alert(bn + " REGISTERED SUCCESSFULLY !!!")
            } else if (res['data'] == "NOT TRAPPED") {
                console.log('trapped')
                alert($('#id_book_num').val() + " - " + res['data'] + "!!!")
            } else if (res['data'] == "NOT VALID") {
                console.log('not valid')
                alert($('#id_book_num').val() + " - " + res['data'] + "!!!")
            }
        }
    })
    } else {
        alert("SELECT WARD")
    }
    return false;
}


submitExamItem();
function submitExamItem (e) {
    $(document).on('click', '#submit-uexam-item-form-modal', function(e) {
        e.preventDefault();
        console.log("uexam  submit clicked")
        if ($('#id_paid_exam_item_modal').val() !== "" && $.isNumeric($('#id_paid_exam_item_modal').val())) {
            if ($('#id_utype_modal').val() !== null ){
                createExamItemModal();
            } else {
            alert("SELECT TEST")
            }
        } else {
            alert("AMOUNT PAID NOT VALID")
        }
    });
};


function createExamItemModal(){
    console.log("called 1")
    var uexam = $('#id_uexam_modal').val()
    var paid = $('#id_paid_exam_item_modal').val()
    var utype = $('#id_utype_modal').val()

    console.log($('#id_uexam_modal').val())
    console.log($('#id_paid_exam_item_modal').val())
    console.log($('#id_utype_modal').val())
    console.log(csrf)
    $.ajax({
        type: 'post',
        url: '/radi/u_examitemcreate/',
        data: {
            csrfmiddlewaretoken: csrf,
            uexam: uexam,
            paid: paid,
            utype: utype,
        },
        success: function(res){
            console.log(res['data'])
            if (res['data'] == "SAVED") {
                console.log('saved exam')
                alert($('#id_utype_modal').val() + " REGISTERED SUCCESSFULLY !!!")
                $.ajax({
                    url: '../../radi/patCreateModalDetailU/' + uexam,
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
                console.log('duplicate')
                $.ajax({
                    url: '../../regi/patCreateModalDetailU/' + uexam,
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


function categoryChangeModal() {

    $.ajax({
        type: 'post',
        url: '/radi/search_echo_test/',
        data: {
            csrfmiddlewaretoken: csrf,
            category: $('#id_category_modal').val(),
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
                $("#id_utype_modal").html(optionRow);
            }
        }
    })
};


function checkExamNum(bn){
    console.log("log")
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
