
//

$(document).ready(function(){

    $('.show-form').click(function(){
        console.log("button add type clicked")
        $.ajax({
            url: '../../labo/typeCreate',
            type: 'get',
            dataType: 'json',
            beforeSend: function(){
                $('#modal-type').modal('show')
            },
            success: function(data){
                $('#modal-type .modal-content').html(data.html_form);
            }
        });
    });

    $('#submit-create-type').click(function(e){
        e.preventDefault()
        console.log("button submit type clicked")
        var csrf = document.getElementsByName("csrfmiddlewaretoken")[0].value
        $.ajax({
            url: '../../labo/typeCreate/',
            type: 'post',
            dataType: 'json',
            data: {
                csrfmiddlewaretoken: csrf,
                type_name:$('#id_type_name').val(),
                cost:$('#id_cost').val(),
                department:$('#id_department').val(),
                category:$('#id_category').val(),
                beforeSend: showModal(),
            },
            success: function(res){
                if (res['data'] == 'SAVED') {
                    console.log(res['data'])
                    hideModal();
                    alert('TYPE - ' + $('#id_type_name').val() + ' - SUCCESSFULLY SAVED ')
                } else if (res['data'] == 'NOT SAVED') {
                    hideModal();
                    alert('TYPE - ' + $('#id_type_name').val() + ' - NOT SAVED (Name or Phone May Already Exist)')
                    showModal();
                }
            }

                // hideModal();
        })
    })

    $('#submit-update-type').click(function(e){
        e.preventDefault()
        console.log("button update type clicked")
        var csrf = document.getElementsByName("csrfmiddlewaretoken")[0].value
        id = $('#type_id').val()
        $.ajax({
            url: '../../labo/typeUpdate/' + id,
            type: 'post',
            dataType: 'json',
            data: {
                csrfmiddlewaretoken: csrf,
                type_name:$('#id_type_name').val(),
                cost:$('#id_cost').val(),
                department:$('#id_department').val(),
                category:$('#id_category').val(),
                beforeSend: showModal(),
            },
            success: function(res){
                if (res['data'] == 'UPDATED') {
                    console.log(res['data'])
                    hideModal();
                    alert('TYPE - ' + $('#id_type_name').val() + ' - SUCCESSFULLY UPDATED ')
                } else if (res['data'] == 'NOT SAVED') {
                    hideModal();
                    alert('TYPE - ' + $('#id_type_name').val() + ' - CANNOT UPDATE')
                    showModal();
                }
            }

        })
    })

    $('#submit-delete-type').click(function(e){
        e.preventDefault()
        console.log("delete clicked")
        var csrf = document.getElementsByName("csrfmiddlewaretoken")[0].value
        var id = $('#type_id').val()
        console.log(id)
        $.ajax({
            url: '../../labo/typeDelete/' + id,
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

                // hideModal();
        })
    })

    $('.type-update').click(function(e){
        e.preventDefault()
        console.log("button update type clicked")
        var currentRow = $(this).closest('tr');
        var id = currentRow.find('td:eq(0)').html();
        console.log("id: " + id)
        $.ajax({
            url: '../../labo/typeUpdate/' + id,
            type: 'get',
            dataType: 'json',
            beforeSend: function(){
                $('#modal-type').modal('show')
            },
            success: function(data){
            console.log("yes")
                $('#modal-type .modal-content').html(data.html_form);
            }
        });
    });

    $('.type-delete').click(function(e){
        e.preventDefault()
        console.log("button delete type clicked")
        var currentRow = $(this).closest('tr');
        var id = currentRow.find('td:eq(0)').html();
        console.log("id: " + id)
        $.ajax({
            url: '../../labo/typeDelete/' + id,
            type: 'get',
            dataType: 'json',
            beforeSend: function(){
                $('#modal-type').modal('show')
            },
            success: function(data){
                $('#modal-type .modal-content').html(data.html_form);
            }
        });
    });

})

function showModal(){
    $('#modal-type').modal('show')
}

function hideModal(){
    $('#modal-type').modal('hide')
}