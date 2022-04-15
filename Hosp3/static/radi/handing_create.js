

$(document).ready(function(){
    $('.show-form').click(function(){

        $.ajax({
            url: '../../radi/handingCreate',
            type: 'get',
            dataType: 'json',
            beforeSend: function(){
                $('#modal-handing').modal('show')
            },
            success: function(data){
                $('#modal-handing .modal-content').html(data.html_form);
            }
        });
    });

    $('#submit-create-handing').click(function(e){
        console.log("handing clicked")
        console.log($('#id_shift').val())       // ok
        console.log($('#id_statistics').val())  // ok
        console.log($('#id_lines').val())       // ok
        console.log($('#id_state1').val())      // ok
        console.log($('#id_state2').val())      // ok
        console.log($('#id_state3').val())      // ok
        console.log($('#id_state4').val())      // ok
        console.log($('#id_state5').val())      // ok
        console.log($('#id_state6').val())      // ok
        console.log($('#id_machine1').val())    // ok
        console.log($('#id_machine2').val())    // ok
        console.log($('#id_machine3').val())    // ok
        console.log($('#id_device1').val())     // ok
        console.log($('#id_device2').val())     // ok
        console.log($('#id_device3').val())     // ok
        console.log($('#id_department').val())     // ok
        console.log($('#id_staff').val())     // ok
        console.log($('#id_remarks').val())     // ok
        e.preventDefault()
        var csrf = document.getElementsByName("csrfmiddlewaretoken")[0].value
        $.ajax({
            url: '../../radi/handingCreate/',
            type: 'post',
            dataType: 'json',
            data: {
                csrfmiddlewaretoken: csrf,
                shift: $('#id_shift').val(),
                statistics: $('#id_statistics').val(),
                lines: $('#id_lines').val(),
                state1: $('#id_state1').val(),
                state2: $('#id_state2').val(),
                state3: $('#id_state3').val(),
                state4: $('#id_state4').val(),
                state5: $('#id_state5').val(),
                state6: $('#id_state6').val(),
                machine1: $('#id_machine1').val(),
                machine2: $('#id_machine2').val(),
                machine3: $('#id_machine3').val(),
                device1: $('#id_device1').val(),
                device2: $('#id_device2').val(),
                device3: $('#id_device3').val(),
                other1: $('#id_other1').val(),
                other2: $('#id_other2').val(),
                other3: $('#id_other3').val(),
                department:  $('#id_department').val(),
                staff: $('#id_staff').val(),
                remarks: $('#id_remarks').val(),
            },
            success: function(res){
                if (res['data'] == 'SAVED') {
                    console.log(res['data'])
                    hideModal();
                    alert('HANDING - ' + $('#id_shift').val() + ' - SUCCESSFUL')
                } else if (res['data'] == 'NOT SAVED') {
                    hideModal();
                    alert('HANDING - ' + $('#id_shift').val() + ' - NOT SAVED (check parameters)')
                    showModal();
                }
            }
        })
    })

    $('#submit-update-staff').click(function(e){
        e.preventDefault()
        var csrf = document.getElementsByName("csrfmiddlewaretoken")[0].value
        id = $('#staff_id').val()
        $.ajax({
            url: '../../radi/staffUpdate/' + id,
            type: 'post',
            dataType: 'json',
            data: {
                csrfmiddlewaretoken: csrf,
                first_name:$('#id_first_name').val(),
                last_name:$('#id_last_name').val(),
                full_name:$('#id_full_name').val(),
                address:$('#id_address').val(),
                sex:$('#id_sex').val(),
                dob:$('#id_dob').val(),
                age:$('#id_age').val(),
                Phone:$('#id_Phone').val(),
                title:$('#id_title').val(),
                beforeSend: showModal(),
            },
            success: function(res){
                if (res['data'] == 'UPDATED') {
                    console.log(res['data'])
                    hideModal();
                    alert('STAFF - ' + $('#id_first_name').val() + ' - SUCCESSFULLY UPDATED ')
                } else if (res['data'] == 'NOT SAVED') {
                    hideModal();
                    alert('STAFF - ' + $('#id_first_name').val() + ' - CANNOT UPDATE')
                    showModal();
                }
            }
        })
    })

    $('#submit-delete-staff').click(function(e){
        var csrf = document.getElementsByName("csrfmiddlewaretoken")[0].value
        e.preventDefault()
        var id = $('#staff_id').val()
        console.log(id)
        $.ajax({
            url: '../../radi/staffDelete/' + id,
            type: 'post',
            dataType: 'json',
            data: {
                csrfmiddlewaretoken: csrf,
                id: $('#staff_id').val()
            },
            success: function(res){
                if (res['data'] == 'DELETED') {
                    console.log(res['data'])
                    hideModal();
                    alert('STAFF - ' + $('#staff_name').val() + ' - SUCCESSFULLY DELETED ')
                } else if (res['data'] == 'NOT DELETED') {
                    hideModal();
                    alert('STAFF - ' + $('#staff_name').val() + ' - CANNOT DELETED')
                    showModal();
                }
            }
        })
    })

    $('.staff-update').click(function(e){
        e.preventDefault()
        var currentRow = $(this).closest('tr');
        var id = currentRow.find('td:eq(0)').html();
        console.log("id: " + id)
        $.ajax({
            url: '../../radi/staffUpdate/' + id,
            type: 'get',
            dataType: 'json',
            beforeSend: function(){
                $('#modal-staff').modal('show')
            },
            success: function(data){
                $('#modal-staff .modal-content').html(data.html_form);
            }
        });
    });

    $('.staff-delete').click(function(e){
        e.preventDefault()
        var currentRow = $(this).closest('tr');
        var id = currentRow.find('td:eq(0)').html();
        console.log("id: " + id)
        $.ajax({
            url: '../../radi/staffDelete/' + id,
            type: 'get',
            dataType: 'json',
            beforeSend: function(){
                $('#modal-staff').modal('show')
            },
            success: function(data){
                $('#modal-staff .modal-content').html(data.html_form);
            }
        });
    });

})

function showModal(){
    $('#modal-staff').modal('show')
}

function hideModal(){
    $('#modal-staff').modal('hide')
}