


$(document).ready(function(){

    $('.show-form').click(function(){
        console.log("button add category clicked")
        $.ajax({
            url: '../../labo/categoryCreate',
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
        console.log("button submit category clicked")
        var csrf = document.getElementsByName("csrfmiddlewaretoken")[0].value
        $.ajax({
            url: '../../labo/categoryCreate/',
            type: 'post',
            dataType: 'json',
            data: {
                csrfmiddlewaretoken: csrf,
                category_name:$('#id_category_name').val(),
                beforeSend: showModal(),
            },
            success: function(res){
                if (res['data'] == 'SAVED') {
                    console.log(res['data'])
                    hideModal();
                    alert('CATEGORY - ' + $('#id_category_name').val() + ' - SUCCESSFULLY SAVED ')
                } else if (res['data'] == 'ALREADY EXIST') {
                    hideModal();
                    alert('CATEGORY - ' + $('#id_category_name').val() + ' - NOT SAVED (Already Exist)')
                    showModal();
                } else if (res['data'] == 'NOT SAVED') {
                    hideModal();
                    alert('CATEGORY - ' + $('#id_category_name').val() + ' - NOT SAVED (Error)')
                    showModal();
                }
            }

                // hideModal();
        })
    })

    $('#submit-update-category').click(function(e){
        e.preventDefault()
        console.log("button update category clicked")
        var csrf = document.getElementsByName("csrfmiddlewaretoken")[0].value
        id = $('#category_id').val()
        $.ajax({
            url: '../../labo/categoryUpdate/' + id,
            type: 'post',
            dataType: 'json',
            data: {
                csrfmiddlewaretoken: csrf,
                category_name:$('#id_category_name').val(),
                beforeSend: showModal(),
            },
            success: function(res){
                if (res['data'] == 'UPDATED') {
                    console.log(res['data'])
                    hideModal();
                    alert('CATEGORY - ' + $('#id_category_name').val() + ' - SUCCESSFULLY UPDATED ')
                } else if (res['data'] == 'NOT SAVED') {
                    hideModal();
                    alert('CATEGORY - ' + $('#id_category_name').val() + ' - CANNOT UPDATE')
                    showModal();
                }
            }

                // hideModal();
        })
    })

    $('#submit-delete-category').click(function(e){
        e.preventDefault()
        console.log("delete clicked")
        var csrf = document.getElementsByName("csrfmiddlewaretoken")[0].value
        var id = $('#category_id').val()
        console.log(id)
        $.ajax({
            url: '../../labo/categoryDelete/' + id,
            type: 'post',
            dataType: 'json',
            data: {
                csrfmiddlewaretoken: csrf,
                id: $('#category_id').val()
            },
            success: function(res){
                if (res['data'] == 'DELETED') {
                    console.log(res['data'])
                    hideModal();
                    alert('CATEGORY - ' + $('#category_name').val() + ' - SUCCESSFULLY DELETED ')
                } else if (res['data'] == 'NOT DELETED') {
                    hideModal();
                    alert('CATEGORY - ' + $('#staff_name').val() + ' - CANNOT DELETED')
                    showModal();
                }
            }

                // hideModal();
        })
    })

    $('.category-update').click(function(e){
        e.preventDefault()
        console.log("button update category clicked")
        var currentRow = $(this).closest('tr');
        var id = currentRow.find('td:eq(0)').html();
        console.log("id: " + id)
        $.ajax({
            url: '../../labo/categoryUpdate/' + id,
            type: 'get',
            dataType: 'json',
            beforeSend: function(){
                $('#modal-category').modal('show')
            },
            success: function(data){
            console.log("yes")
                $('#modal-category .modal-content').html(data.html_form);
            }
        });
    });

    $('.category-delete').click(function(e){
        e.preventDefault()
        console.log("button delete category clicked")
        var currentRow = $(this).closest('tr');
        var id = currentRow.find('td:eq(0)').html();
        console.log("id: " + id)
        $.ajax({
            url: '../../labo/categoryDelete/' + id,
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