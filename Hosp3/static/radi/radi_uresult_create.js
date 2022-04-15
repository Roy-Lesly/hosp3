var searchForm = $("#search-form")  // or var searchForm = document.getElementById("#search-form")
var resultBox = $("#result-box")                // ok
var searchResult = $('.search-results')
var searchFormVal = searchForm.val()            // ok
var searchInput = $("#search-input")            // ok
var csrf = document.getElementsByName("csrfmiddlewaretoken")[0].value    // ok

$('#submit-form').hide()
$('#container-2').hide()
$('#result-box').hide()


$('#id_utype').on('change', function(e) {
    e.preventDefault();
    console.log("type changed")
    console.log($('#id_utype').val())
    $.ajax({
        type: 'post',
        url: '/radi/check_test_exist_in_exam/',
        data: {
            csrfmiddlewaretoken: csrf,
            id_utype: $('#id_utype').val(),
        },
        success: function(res){
            if (res == "TAKEN") {
                alert("Results For This Procedure Exist Already !!!")
            } else if (res == "NOT TAKEN") {
                console.log("No results")
            }
        }
    })
})


$(document).on('click', '#submit-form', function(e) {
    e.preventDefault();
    $.ajax({
        type: 'post',
        url: '/radi/check_test_exist_in_exam/',
        data: {
            csrfmiddlewaretoken: csrf,
            id_utype: $('#id_utype').val(),
        },
        success: function(res){
            if (res == "TAKEN") {
                alert("Results For This Procedure Exist Already !!!")
            } else if (res == "NOT TAKEN") {
                console.log("No results")
                if ($('#id_utype').val() !== "") {
        if ($('#id_staff').val() !== "") {
            if ($('#id_findings').val() !== "") {
                console.log("True")
                console.log($('#id_uexam').val())
                $.ajax({
                    type: 'post',
                    url: '/radi/u_resultcreate/',
                    data: {
                        csrfmiddlewaretoken: csrf,
                        uexam:$('#id_uexam').val(),
                        u_test:$('#id_utype').val(),
                        staff:$('#id_staff').val(),
                        findings:$('#id_findings').val().toUpperCase(),
                        code:$('#id_code').val(),
                    },
                    success: function(res){
                        if (res == "SAVED") {
                            console.log(res)
                            $.ajax({
                                url: '../../radi/resCreateDetailModalU/',
                                type: 'get',
                                dataType: 'json',
                                beforeSend: function(){
                                    $('#modal-noti').modal('show')
                                },
                                success: function(data){
                                    $('#modal-noti .modal-content').html(data.html_form);
                                }
                            });
                        }
                        if (res == "NOT SAVED") {
                            alert("Form Data Not Valid")
                        } else if (res == "EXIST ALREADY") {
                            alert("Echo Test - " + $('#id_utype').val() + " RESULT ALREADY EXIST !!!")
                        }
                    }
                })
            }
            else
                console.log("Fill Findings")
        }
        else
            alert("Select Sonographer (Staff) ?")
    }
                else
                    alert("Select Echo Test")
            }
        }
    })
})


$(document).on('click', '#submit-update-result', function(e) {
    e.preventDefault();
    console.log($('#id_staff').text())
    console.log($('#id_findings').text())
    console.log($('#id_u_test').val())
    console.log($('#id_u_test').text())
    console.log($('#id_uexam').text())
    console.log($('#id_id').text())

    if ($('#id_findings').val() !== "") {
        $.ajax({
            type: 'post',
            url: '../u_resultupdate/' + $('#id_id').val(),
            data: {
                csrfmiddlewaretoken: csrf,
                uexam:$('#id_uexam').val(),
                u_test:$('#id_u_test').val(),
                staff:$('#id_staff').val(),
                paid:$('#id_paid').val(),
                findings:$('#id_findings').val(),
            },
            success: function(res){
                console.log(res)
                if (res == "FINDING UPDATED") {
                    alert("Echo Test - " + $('#id_u_test').text() + " Result Updated!!!")
                } else {
                    alert("Echo Test - " + $('#id_u_test').text() + " Result Not Updated!!!")
                }
            }
        })
    }
    else
        console.log("Enter Findings")
})


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
})


$('#id_uexam').change(function(e) {
    e.preventDefault();
    console.log('book_num changed')
    alert('book_num changed')

    $.ajax({
        type: 'post',
        url: '/radi/search_echo_test/',
        data: {
            csrfmiddlewaretoken: csrf,
            category: $('#id_uexam').val(),
        },
        success: function(res){
            if (res == "") {
                console.log("No results")
            } else {
                var optionRow = '<option value="">---------</option>';
                res.forEach(function (object) {
                    object.forEach(function (item) {
                        optionRow += `<option value="${item.id}">${item.type_name}</option>`
                    });
                });
                $("#id_ltype").html(optionRow);
            }
        }
    })
})


$('#id_code').on('keyup', function(e) {
    $.ajax({
        type: 'post',
        url: '/radi/validate_code/',
        data: {
            csrfmiddlewaretoken: csrf,
            code: $('#id_code').val(),
            staff: $('#id_staff').val(),
        },
        success: function(res){
            console.log(res)
            if (res == "VALID") {
                $('#submit-form').show()
            } else {
                $('#submit-form').hide()
            }
        }
    });
});


$('#search-input').on('keyup', function(e){
    sendSearchInputValue(e.target.value)
});


var sendSearchInputValue = (searchText) => {
    qt = $('#query-type').val()
    if (searchText.length > 3){
        $("#table-output").innerHTML = ""
        $('#result-box').show();
        fetch("../../radi/search_echo_exam/", {
            body: JSON.stringify({
                searchText: searchText,
                queryType: qt
            }),
            method: "POST",
        })
        .then((res) => res.json())
        .then((data) => {

            console.log(data)

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
                    row.append($('<td class="class1"></td>').html(rowData.book_num));
                    row.append($('<td class="class1"></td>').html(rowData.ys));
                    row.append($('<td class="class2"></td>').html(rowData.full_name));
                    row.append($('<td class="class3"></td>').html(rowData.age));
                    row.append($('<td class="class4"></td>').html(rowData.sex));
                    row.append($('<td class="class4"></td>').html(rowData.Address));
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

                $(".table").append(rows);

                function fillForm(rowData) {
                    var form = $("#id_patient");
                    $('#id_uexam').val(rowData.book_num);
                    getTestItems(rowData.book_num);

                }

            }
        });

    }else{
        $('#result-box').hide();
    }
}


function getTestItems(data) {
    console.log("here")
    console.log(data)
    $.ajax({
        type: 'post',
        url: "../../radi/search_echo_test/",
        data: {
            csrfmiddlewaretoken: csrf,
            book_num: data
        },
        success: function(res){
            if (res[1] == "VALID") {
                console.log(res[0])
                console.log(res[0][0]['utype'])
                console.log(res[0][1])
                var optionRow = '<option value="">---------</option>';
                res[0].forEach(function (object) {
                    optionRow += `<option value="${object['id']}">${object["utype"]}</option>`
                });
                $("#id_utype").html(optionRow);
                console.log(optionRow)
                console.log('succeeded')
                $('#submit-form').show()
            } else if (res[1] == "NON VALID") {
                console.log(res[1])
                //$('#submit-form').hide()
            }
        }
    });
}

// ====================== writing result ==========================
$("#res_form").hide();
$("#heada2").hide();
$(document).on('click', '#btn-yes', function(e) {
    e.preventDefault();
    $("#res_confirm").hide();
    $("#res_form").show();
    $("#heada1").hide();
    $("#heada2").show();
});


$(document).on('click', '.result-form-type', function(e) {
    $('#modal-noti').modal("hide");
    e.preventDefault();
    console.log("form selected")
    console.log($(this).val())
    console.log($(this).val() + " form selected")
    $.ajax({
        type: 'post',
        url: '/radi/write_results/',
        data: {
            csrfmiddlewaretoken: csrf,
            uexam: $('#id_uexam').val(),
            utype: $('#id_utype').val(),
            staff: $('#id_staff').val(),
            form_type: $(this).val(),
        },
        success: function(res){
            console.log(res)
            //window.location.href = "../../radi/test/"
            if (res["state"] == "SUCCESS") {
                console.log("Success State !!!")
                $('#container-1').empty();
                $('#container-1').hide();
                $('#container-2').show()
                $('#container-2 .row').html(res.html_form);
            } else {
                console.log("Not Successfull State")
                if ($('#id_utype').val() !== "") {
        if ($('#id_staff').val() !== "") {
            if ($('#id_findings').val() !== "") {
                console.log("True")
                console.log($('#id_uexam').val())
                $.ajax({
                    type: 'post',
                    url: '/radi/u_resultcreate/',
                    data: {
                        csrfmiddlewaretoken: csrf,
                        uexam:$('#id_uexam').val(),
                        u_test:$('#id_utype').val(),
                        staff:$('#id_staff').val(),
                        findings:$('#id_findings').val().toUpperCase(),
                        code:$('#id_code').val(),
                    },
                    success: function(res){
                        if (res == "SAVED") {
                            console.log(res)
                            $.ajax({
                                url: '../../radi/resCreateDetailModalU/',
                                type: 'get',
                                dataType: 'json',
                                beforeSend: function(){
                                    $('#modal-noti').modal('show')
                                },
                                success: function(data){
                                    $('#modal-noti .modal-content').html(data.html_form);
                                }
                            });
                        }
                        if (res == "NOT SAVED") {
                            alert("Form Data Not Valid")
                        } else if (res == "EXIST ALREADY") {
                            alert("Echo Test - " + $('#id_utype').val() + " RESULT ALREADY EXIST !!!")
                        }
                    }
                })
            }
            else
                console.log("Fill Findings")
        }
        else
            alert("Select Sonographer (Staff) ?")
    }
                else
                    alert("Select Echo Test")
            }
        }
    })
})


$(document).on('click', '#submit-obs-form', function(e) {
    e.preventDefault();
    $.ajax({
        type: 'post',
        url: '/radi/generate_report/',
        data: {
            csrfmiddlewaretoken: csrf, form_type: "OBSTETRIC",
            sn: $('#id_sn').val(), un: $('#id_un').val(), book_num: $('#id_book_num').val(),
            full_name: $('#id_full_name').val(), address: $('#id_address').val(),
            sex: $('#id_sex').val(), staff: $('#id_staff').val(), age: $('#id_age').val(),
            phone: $('#id_phone').val(), presc: $('#id_presc').val(), date_created: $('#id_date_created').val(),
            indic: $('#id_indic').val(), lmp: $('#id_lmp').val(),

            numfet: $('#id_numfet').val(), presen: $('#id_presen').val(), fhr: $('#id_fhr').val(),
            fetmov1: $('#id_fetmov1').val(), fetmov2: $('#id_fetmov2').val(),
            afi1: $('#id_afi1').val(), appearance: $('#id_appearance').val(),
            afi2: $('#id_afi2').val(), afi3: $('#id_afi3').val(),

            gs1: $('#id_gs1').val(), crl1: $('#id_crl1').val(), bpd1: $('#id_bpd1').val(),
            hc1: $('#id_hc1').val(), ac1: $('#id_ac1').val(), fl1: $('#id_fl1').val(),

            gs2: $('#id_gs2').val(), crl2: $('#id_crl2').val(), bpd2: $('#id_bpd2').val(),
            hc2: $('#id_hc2').val(), ac2: $('#id_ac2').val(), fl2: $('#id_fl2').val(),

            gs3: $('#id_gs3').val(), crl3: $('#id_crl3').val(), bpd3: $('#id_bpd3').val(),
            hc3: $('#id_hc3').val(), ac3: $('#id_ac3').val(), fl3: $('#id_fl3').val(),

            ga1: $('#id_ga1').val(), ga2: $('#id_ga2').val(), edd: $('#id_edd').val(),
            efwa1: $('#id_efwa1').val(), efwa2: $('#id_efwa2').val(),
            efwb1: $('#id_efwb1').val(), efwb2: $('#id_efwb2').val(),

            fetnorm1: $('#id_fetnorm1').val(), fetnorm2: $('#id_fetnorm2').val(),
            placen1: $('#id_placen1').val(), placen2: $('#id_placen2').val(),
            placen3: $('#id_placen3').val(), placen4: $('#id_placen4').val(),
            addcom1: $('#id_addcom1').val(), addcom2: $('#id_addcom3').val(), addcom3: $('#id_addcom3').val(),
            bps1: $('#id_bps1').val(), bps2: $('#id_bps2').val(), bps3: $('#id_bps3').val(), bps4: $('#id_bps4').val(), bps5: $('#id_bps5').val(), bpst: $('#id_bpst').val(),

            imp1: $('#id_imp1').val(), imp2: $('#id_imp2').val(), imp3: $('#id_imp3').val(), imp4: $('#id_imp4').val(),
        },
        success: function(res){
            console.log(res)
            if (res["state"] == "SUCCESS") {
                console.log("Results Generated !!!")
                alert("Results Generated !!!")
                window.location.href = "../../radi/u_resultcreate/"
            } else {
                console.log("Not Successfully Generated")
            }
        }
    })
});


$(document).on('change', '#id_numfet', function(e) {
    e.preventDefault();
    console.log('Num Fet changed')
    $('#imp-line-2').hide(); $('#imp-line-3').hide(); $('#imp-line-4').hide();
    $('#add-imp2').hide(); $('#add-imp3').hide(); $('#add-imp4').hide();
    $('#clear2').hide(); $('#clear3').hide(); $('#clear4').hide(); $('#clear5').hide();
    $('#addcom2').hide(); $('#addcom3').hide(); $('#com2').hide(); $('#com3').hide();
    $('#clear-com2').hide(); $('#clear-com3').hide(); $('#clear-all-com').hide();
    if ($('#id_numfet').val() == 01) {
        $('#fetus-b').hide();
        $('#fetus-c').hide();
        $('#efw2').hide();
    } else if ($('#id_numfet').val() == 02) {
        $('#fetus-b').show();
        $('#fetus-c').hide();
        $('.efw2').show();
    } else if ($('#id_numfet').val() == 03) {
        $('#fetus-b').show();
        $('#fetus-c').show();
        $('.efw2').show();
    } else if ($('#id_numfet').val() == ">3") {
        $('#fetus-b').show();
        $('#fetus-c').show();
        $('.efw2').show();
    }
})


$(document).on('click', '#id_fhr', function(e) {
    e.preventDefault();
    $('#imp-line-2').hide(); $('#imp-line-3').hide(); $('#imp-line-4').hide();
    $('#add-imp2').hide(); $('#add-imp3').hide(); $('#add-imp4').hide();
    $('#clear2').hide(); $('#clear3').hide(); $('#clear4').hide(); $('#clear5').hide();
    $('#addcom2').hide(); $('#addcom3').hide(); $('#com2').hide(); $('#com3').hide();
    $('#clear-com2').hide(); $('#clear-com3').hide(); $('#clear-all-com').hide();
    if ($('#id_numfet').val() == 01) {
        $('#fetus-b').hide();
        $('#fetus-c').hide();
        $('.efw2').hide();
    } else if ($('#id_numfet').val() == 02) {
        $('#fetus-b').show();
        $('#fetus-c').hide();
        $('.efw2').show();
    } else if ($('#id_numfet').val() == 03) {
        $('#fetus-b').show();
        $('#fetus-c').show();
        $('.efw2').show();
    } else if ($('#id_numfet').val() == ">3") {
        $('#fetus-b').show();
        $('#fetus-c').show();
        $('.#efw2').show();
    }
});


// =============== Additional Comment Buttons ===================
$(document).on('click', '#addcom2', function(e) {
    e.preventDefault();
    console.log("clicked")
    $('#com2').show();
    $('#addcom2').hide();
});


$(document).on('click', '#addcom3', function(e) {
    e.preventDefault();
    console.log("clicked")
    $('#com3').show();
    $('#addcom3').hide();
    $('#clear-com2').hide();
});


$(document).on('click', '#clear-com2', function(e) {
    e.preventDefault();
    console.log("c-com2")
    $('#com2').hide(); $('#com2').val('');
    $('#clear-com2').hide();
    $('#addcom3').hide();
    $('#addcom2').show();
});


$(document).on('click', '#clear-com3', function(e) {
    e.preventDefault();
    console.log("c-com3")
    $('#com3').hide(); $('#com3').val("");
    $('#clear-com3').hide();
    $('#addcom3').show();
});


$(document).on('keyup', '#com1', function(e) {
    e.preventDefault();
    console.log("clicked")
    $('#addcom2').show();
});


$(document).on('keyup', '#com2', function(e) {
    e.preventDefault();
    console.log("clicked")
    $('#addcom3').show();
    $('#clear-com2').show();
});


$(document).on('keyup', '#com3', function(e) {
    e.preventDefault();
    console.log("key up com3")
    $('#clear-com3').show();
});

// ===============  Impression Buttons ==========================
$(document).on('click', '#add-imp1', function(e) {
    e.preventDefault();
    console.log("clicked")
    $('#imp-line-2').show();
    $('#add-imp2').show();
    $('#clear2').show();
    $('#add-imp1').hide();
});


$(document).on('click', '#add-imp2', function(e) {
    e.preventDefault();
    console.log("clicked")
    $('#imp-line-3').show();
    $('#add-imp3').show();
    $('#clear2').hide();
    $('#clear3').show();
    $('#add-imp2').hide();
});


$(document).on('click', '#add-imp3', function(e) {
    e.preventDefault();
    console.log("clicked")
    $('#imp-line-4').show();
    $('#add-imp3').hide();
    $('#clear3').hide();
    $('#clear4').show();
    $('#clear5').show();
    $('#add-imp4').show();
});


$(document).on('click', '#clear2', function(e) {
    e.preventDefault();
    console.log("clicked")
    $('#imp-line-2').hide();
    $('#clear2').hide();
    $('#add-imp1').show();
    $('#add-imp2').hide();
});


$(document).on('click', '#clear3', function(e) {
    e.preventDefault();
    console.log("clicked")
    $('#imp-line-3').hide();
    $('#clear3').hide();
    $('#add-imp2').show();
    $('#add-imp3').hide();
});


$(document).on('click', '#clear4', function(e) {
    e.preventDefault();
    console.log("clicked")
    $('#imp-line-4').hide();
    $('#clear4').hide();
    $('#clear5').hide();
    $('#add-imp3').show();
});


$(document).on('click', '#clear5', function(e) {
    e.preventDefault();
    console.log("clicked")
    $('#imp-line-2').hide();
    $('#imp-line-3').hide();
    $('#imp-line-4').hide();
    $('#add-imp1').show();
    $('#clear4').hide();
    $('#clear5').hide();
});