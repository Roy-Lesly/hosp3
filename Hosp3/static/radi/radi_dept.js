
$(document).ready(function(){

    $('.show-form').click(function(){
        console.log("button add dept clicked")
        $.ajax({
            url: '../../radi/deptCreate',
            type: 'get',
            dataType: 'json',
            beforeSend: function(){
                $('#modal-dept').modal('show')
            },
            success: function(data){
                $('#modal-dept .modal-content').html(data.html_form);
            }
        });
    });

    $('#submit-create-dept').click(function(e){
        e.preventDefault()
        console.log("button submit dept clicked")
        alert($('#id_name').val())
        console.log($('#id_name').val())
        var csrf = document.getElementsByName("csrfmiddlewaretoken")[0].value
        $.ajax({
            url: '../../radi/deptCreate/',
            type: 'post',
            dataType: 'json',
            data: {
                csrfmiddlewaretoken: csrf,
                name:$('#id_name').val(),
                beforeSend: showModal(),
            },
            success: function(res){
                if (res['data'] == 'SAVED') {
                    console.log(res['data'])
                    hideModal();
                    alert('DEPT - ' + $('#id_name').val() + ' - SUCCESSFULLY SAVED ')
                } else if (res['data'] == 'NOT SAVED') {
                    hideModal();
                    alert('DEPT - ' + $('#id_name').val() + ' - NOT SAVED (Name May Already Exist)')
                    showModal();
                }
            }
        })
    })

    $('#submit-update-dept').click(function(e){
        e.preventDefault()
        console.log("button update radi_dept clicked")
        var csrf = document.getElementsByName("csrfmiddlewaretoken")[0].value
        id = $('#id_dept').val()
        id2 = $('#id_name').val()
        console.log(id2)
        $.ajax({
            url: '../../radi/deptUpdate/' + id,
            type: 'post',
            dataType: 'json',
            data: {
                csrfmiddlewaretoken: csrf,
                name:$('#id_name').val(),
                type_name:$('#id_dept').val(),
                beforeSend: showModal(),
            },
            success: function(res){
                if (res['data'] == 'UPDATED') {
                    console.log(res['data'])
                    hideModal();
                    alert('DEPT - ' + $('#id_name').val() + ' - SUCCESSFULLY UPDATED ')
                } else if (res['data'] == 'NOT SAVED') {
                    hideModal();
                    alert('DEPT - ' + $('#id_name').val() + ' - CANNOT UPDATE')
                    showModal();
                }
            }
        })
    })

    $('#submit-delete-type').click(function(e){
        var csrf = document.getElementsByName("csrfmiddlewaretoken")[0].value
        e.preventDefault()
        console.log("delete clicked")
        var id = $('#type_id').val()
        console.log(id)
        $.ajax({
            url: '../../radix/typeDelete/' + id,
            type: 'post',
            dataType: 'json',
            data: {
                csrfmiddlewaretoken: csrf,
                id: $('#type_id').val()
            },
            success: function(res){
                if (res['data'] == 'DELETED') {
                    console.log(res['data'])
                    hideModal();
                    alert('TYPE - ' + $('#type_name').val() + ' - SUCCESSFULLY DELETED ')
                } else if (res['data'] == 'NOT DELETED') {
                    hideModal();
                    alert('TYPE - ' + $('#type_name').val() + ' - CANNOT DELETED')
                    showModal();
                }
            }
        })
    })

    $('.dept-update').click(function(e){
        e.preventDefault()
        console.log("button update dept clicked")
        var currentRow = $(this).closest('tr');
        var id = currentRow.find('td:eq(0)').html();
        console.log("id: " + id)
        $.ajax({
            url: '../../radi/deptUpdate/' + id,
            type: 'get',
            dataType: 'json',
            beforeSend: function(){
                $('#modal-dept').modal('show')
            },
            success: function(data){
                $('#modal-dept .modal-content').html(data.html_form);
            }
        });
    });

    $('.dept-delete').click(function(e){
        e.preventDefault()
        console.log("button delete dept clicked")
        var currentRow = $(this).closest('tr');
        var id = currentRow.find('td:eq(0)').html();
        console.log("id: " + id)
        $.ajax({
            url: '../../radi/deptDelete/' + id,
            type: 'get',
            dataType: 'json',
            beforeSend: function(){
                $('#modal-dept').modal('show')
            },
            success: function(data){
                $('#modal-dept .modal-content').html(data.html_form);
            }
        });
    });

})

function showModal(){
    $('#modal-dept').modal('show')
}

function hideModal(){
    $('#modal-dept').modal('hide')
}