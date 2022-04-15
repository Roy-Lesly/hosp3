


$(document).ready(function(){

    $('.show-form').click(function(){
        console.log("button add staff clicked")
        $.ajax({
            url: '../../labo/staffCreate',
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

    $('#submit-create-staff').click(function(e){
        e.preventDefault()
        console.log("button submit staff clicked")
        var csrf = document.getElementsByName("csrfmiddlewaretoken")[0].value
        $.ajax({
            url: '../../labo/staffCreate/',
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
                if (res['data'] == 'SAVED') {
                    console.log(res['data'])
                    hideModal();
                    alert('STAFF - ' + $('#id_first_name').val() + ' - SUCCESSFULLY SAVED ')
                } else if (res['data'] == 'NOT SAVED') {
                    hideModal();
                    alert('STAFF - ' + $('#id_first_name').val() + ' - NOT SAVED (Name or Phone May Already Exist)')
                    showModal();
                }
            }

                // hideModal();
        })
    })

    $('#submit-update-staff').click(function(e){
        e.preventDefault()
        console.log("button update staff clicked")
        var csrf = document.getElementsByName("csrfmiddlewaretoken")[0].value
        id = $('#staff_id').val()
        $.ajax({
            url: '../../labo/staffUpdate/' + id,
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

                // hideModal();
        })
    })

    $('#submit-delete-staff').click(function(e){
        var csrf = document.getElementsByName("csrfmiddlewaretoken")[0].value
        e.preventDefault()
        console.log("delete clicked")
        var id = $('#staff_id').val()
        console.log(id)
        $.ajax({
            url: '../../labo/staffDelete/' + id,
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

                // hideModal();
        })
    })

    $('.staff-update').click(function(e){
        e.preventDefault()
        console.log("button update staff clicked")
        var currentRow = $(this).closest('tr');
        var id = currentRow.find('td:eq(0)').html();
        console.log("id: " + id)
        $.ajax({
            url: '../../labo/staffUpdate/' + id,
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
        console.log("button delete staff clicked")
        var currentRow = $(this).closest('tr');
        var id = currentRow.find('td:eq(0)').html();
        console.log("id: " + id)
        $.ajax({
            url: '../../labo/staffDelete/' + id,
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