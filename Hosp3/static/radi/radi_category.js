
$(document).ready(function(){

    $('.show-form').click(function(){
        console.log("button add category clicked")
        $.ajax({
            url: '../../radi/categoryCreate',
            type: 'get',
            dataType: 'json',
            beforeSend: function(){
                $('#modal-category').modal('show')
            },
            success: function(data){
                $('#modal-category .modal-content').html(data.html_form);
            }
        });
    });

    $('#submit-create-category').click(function(e){
        e.preventDefault()
        console.log("button submit type clicked")
        var csrf = document.getElementsByName("csrfmiddlewaretoken")[0].value
        $.ajax({
            url: '../../radi/categoryCreate/',
            type: 'post',
            dataType: 'json',
            data: {
                csrfmiddlewaretoken: csrf,
                category_name:$('#id_category_name').val(),
                department:$('#id_department').val(),
                beforeSend: showModal(),
            },
            success: function(res){
                if (res['data'] == 'SAVED') {
                    console.log(res['data'])
                    hideModal();
                    alert('CATEGORY - ' + $('#id_category_name').val() + ' - SUCCESSFULLY SAVED ')
                } else if (res['data'] == 'NOT SAVED') {
                    hideModal();
                    alert('CATEGORY - ' + $('#id_category_name').val() + ' - NOT SAVED')
                    showModal();
                } else if (res['data'] == 'EXIST ALREADY') {
                    hideModal();
                    alert('CATEGORY - ' + $('#id_category_name').val() + ' - EXIST ALREADY')
                    showModal();
                }
            }
        })
    })

    $('#submit-update-category').click(function(e){
        e.preventDefault()
        console.log("button update type clicked")
        var csrf = document.getElementsByName("csrfmiddlewaretoken")[0].value
        id = $('#id_category').val()
        console.log(id)
        $.ajax({
            url: '../../radi/categoryUpdate/' + id,
            type: 'post',
            dataType: 'json',
            data: {
                csrfmiddlewaretoken: csrf,
                category_name:$('#id_category_name').val(),
                department:$('#id_department').val(),
                beforeSend: showModal(),
            },
            success: function(res){
                if (res['data'] == 'UPDATED') {
                    console.log(res['data'])
                    hideModal();
                    alert('CATEGORY - ' + $('#id_name').val() + ' - SUCCESSFULLY UPDATED ')
                } else if (res['data'] == 'NOT SAVED') {
                    hideModal();
                    alert('CATEGORY - ' + $('#id_name').val() + ' - CANNOT UPDATE')
                    showModal();
                }
            }

                // hideModal();
        })
    })

    $('#submit-delete-category').click(function(e){
        var csrf = document.getElementsByName("csrfmiddlewaretoken")[0].value
        e.preventDefault()
        console.log("delete clicked")
        var id = $('#type_id').val()
        console.log(id)
        $.ajax({
            url: '../../radi/categoryxDelete/' + id,
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
                    alert('CATEGORY - ' + $('#type_name').val() + ' - SUCCESSFULLY DELETED ')
                } else if (res['data'] == 'NOT DELETED') {
                    hideModal();
                    alert('CATEGORY - ' + $('#type_name').val() + ' - CANNOT DELETED')
                    showModal();
                }
            }
        })
    })

    $('.category-update').click(function(e){
        e.preventDefault()
        console.log("button update category clicked")
        var currentRow = $(this).closest('tr');
        var id = currentRow.find('td:eq(0)').html();
        console.log("id: " + id)
        $.ajax({
            url: '../../radi/categoryUpdate/' + id,
            type: 'get',
            dataType: 'json',
            beforeSend: function(){
                $('#modal-category').modal('show')
            },
            success: function(data){
                $('#modal-category .modal-content').html(data.html_form);
            }
        });
    });

    $('.category-delete').click(function(e){
        e.preventDefault()
        console.log("button delete type clicked")
        var currentRow = $(this).closest('tr');
        var id = currentRow.find('td:eq(0)').html();
        console.log("id: " + id)
        $.ajax({
            url: '../../radi/categoryDelete/' + id,
            type: 'get',
            dataType: 'json',
            beforeSend: function(){
                $('#modal-category').modal('show')
            },
            success: function(data){
                $('#modal-category .modal-content').html(data.html_form);
            }
        });
    });

})

function showModal(){
    $('#modal-category').modal('show')
}

function hideModal(){
    $('#modal-category').modal('hide')
}