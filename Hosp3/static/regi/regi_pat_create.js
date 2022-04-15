


$("#result-box").hide();
$('#submit-form').hide();
$(document).ready(function(){

    $('#id_sex').change(function(e){
        $('#submit-form').show();
    })

    $('#submit-form').click(function(e){
        e.preventDefault()
        console.log("patient create button clicked")
        var csrf = document.getElementsByName("csrfmiddlewaretoken")[0].value
        $.ajax({
            url: '../../regi/regiCreate/',
            type: 'post',
            data: {
                csrfmiddlewaretoken: csrf,
                reg_num:$('#id_reg_num').val(),
                first_name:$('#id_first_name').val(),
                last_name:$('#id_last_name').val(),
                full_name:$('#id_full_name').val(),
                address:$('#id_address').val(),
                sex:$('#id_sex').val(),
                dob:$('#id_dob').val(),
                age: 0,
                Phone:$('#id_Phone').val(),
            },
            success: function(res){
                //$('#modal-staff .modal-content').html(data.html_form);
                if (res['data'] == 'SAVED') {
                    alert('PATIENT - ' + $('#id_first_name').val() + ' - SUCCESSFULLY SAVED ')
                    $('#submit-form').hide();
                    $('#id_reg_num').val('');
                    $('#id_first_name').val('');
                    $('#id_last_name').val('');
                    $('#id_address').val('');
                    $('#id_sex').val('');
                    $('#id_dob').val('');
                    $('#id_Phone').val('');
                } else if (res['data'] == 'NOT SAVED') {
                    alert('PATIENT - ' + $('#id_first_name').val() + ' - NOT SAVED (Data Not Valid)')
                } else if (res['data'] == "REG NUM EXIST ALREADY") {
                    alert('PATIENT - ' + $('#id_first_name').val() + ' - NOT SAVED (REG NUM EXIST ALREADY)')
                } else if (res['data'] == "FULL NAME EXIST ALREADY") {
                    alert($('#id_first_name').val() + " and "+ $('#id_first_name').val() + ' (EXIST ALREADY)')
                } else if (res['data'] == "PHONE EXIST ALREADY") {
                    alert('NOT SAVED - CHECK PHONE !!! (EXIST ALREADY or INVALID)')
                } else if (res['data'] == "INVALID PHONE NUMBER") {
                    alert("INVALID PHONE NUMBER (length should be 9 Numbers)")
                }
            }
        });
    });

    $('.update-patient').click(function(){
        //e.preventDefault();
        console.log("button edit pat clicked")
        var currentRow = $(this).closest('tr');
        var id = currentRow.find('td:eq(0)').html();
        console.log(id)
        $.ajax({
            url: '../../regi/regiUpdate/' + id,
            type: 'get',
            dataType: 'json',
            beforeSend: function(){
                showModal();
            },
            success: function(data){
                $('#modal-patient .modal-content').html(data.html_form);
            }
        });
    });

    $('#submit-update-patient').click(function(e){
        e.preventDefault()
        console.log("button update staff clicked")
        var csrf = document.getElementsByName("csrfmiddlewaretoken")[0].value
        var id = $('#id_patient_sn').val()
        console.log(id)
        $.ajax({
            url: '../../regi/regiUpdate/' + id,
            type: 'post',
            dataType: 'json',
            data: {
                csrfmiddlewaretoken: csrf,
                reg_num:$('#id_reg_num').val(),
                first_name:$('#id_first_name').val(),
                last_name:$('#id_last_name').val(),
                full_name:$('#id_full_name').val(),
                address:$('#id_address').val(),
                sex:$('#id_sex').val(),
                dob:$('#id_dob').val(),
                age:0,
                Phone:$('#id_Phone').val(),
                title:$('#id_title').val(),
            },
            success: function(res){
                if (res['data'] == 'UPDATED') {
                    console.log(res['data'])
                    hideModal();
                    alert('PATIENT - ' + $('#id_first_name').val() + ' - SUCCESSFULLY UPDATED ')
                } else if (res['data'] == 'NOT UPDATED') {
                    hideModal();
                    alert('PATIENT - ' + $('#id_first_name').val() + ' - CANNOT UPDATE')
                    showModal();
                } else if (res['data'] == 'INVALID PHONE NUMBER') {
                    hideModal();
                    alert('CANNOT UPDATE (INVALID PHONE NUMBER) - length must be 9 Numbers')
                    showModal();
                }
            }

                // hideModal();
        })
    })

});

function showModal(){
    $('#modal-patient').modal('show')
}

function hideModal(){
    $('#modal-patient').modal('hide')
}

// =========== Search_Patient and display in searchResult div ==========
var sendSearchInputValue = (searchText) => {
    qt = $('#query-type').val()
    if (searchText.length > 3){
        $("#table-output").innerHTML = ""
        $('#result-box').show();
        fetch("../search_patient/", {
            body: JSON.stringify({
                searchText: searchText,
                queryType: qt
            }),
            method: "POST",
        })
        .then((res) => res.json())
        .then((data) => {

            if (data.length===0){
                $("#result-box").removeClass('not-visible')
                $("#table-body").empty().html("No Results Found !!!")

            }else{
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
                      $('#result-box').hide();
                    });

                return row;
                });

                $(".table").append(rows);

                function fillForm(rowData) {
                    var form = $("#id_patient");
                    $('#id_sn').val(rowData.sn);
                    $('#id_full_name').val(rowData.full_name);
                    $('#id_phone').val(rowData.Phone);
                    $('#id_address').val(rowData.address);
                    $('#id_age').val(rowData.age);
                }

            }
        });

    }else{
        $('#result-box').hide();
    }
}

$(document).on('keyup', '#search-input', function(e){
    sendSearchInputValue(e.target.value)
});

