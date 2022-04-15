

// $('#submit-form').hide();
$(document).ready(function(){

    $('.update-result').click(function(e){
        e.preventDefault();
        console.log("button edit result clicked")
        var currentRow = $(this).closest('tr');
        var id = currentRow.find('td:eq(1)').html();
        console.log(id)
        $.ajax({
            url: '../../labo/resultupdate/' + id,
            type: 'get',
            dataType: 'json',
            beforeSend: function(){
                showModal();
            },
            success: function(data){
                console.log(data)
                $('#modal-result .modal-content').html(data.html_form);
            }
        });
    });

    $('.delete-result').click(function(e){
        e.preventDefault()
        console.log("button delete result clicked")
        var currentRow = $(this).closest('tr');
        var id = currentRow.find('td:eq(1)').html();
        console.log("id: " + id)
        $.ajax({
            url: '../../labo/resultdelete/' + id,
            type: 'get',
            dataType: 'json',
            beforeSend: function(){
                $('#modal-result').modal('show')
            },
            success: function(data){
                $('#modal-result .modal-content').html(data.html_form);
            }
        });
    });

    $('#submit-update-result').click(function(e){
        e.preventDefault()
        console.log("button update staff clicked")
        var csrf = document.getElementsByName("csrfmiddlewaretoken")[0].value
        var id = $('#result_id').val()
        console.log(id)
        console.log($('#id_staff').val())
        console.log($('#id_lab_test').val())
        console.log($('#id_lab_exam').val())
        console.log($('#id_findings').val())
        $.ajax({
            url: '../../labo/resultupdate/' + id,
            type: 'post',
            dataType: 'json',
            data: {
                csrfmiddlewaretoken: csrf,
                staff:$('#id_staff').val(),
                lab_test:$('#id_lab_test').val(),
                lab_exam:$('#id_lab_exam').val(),
                findings:$('#id_findings').val(),
            },
            success: function(res){
                if (res['data'] == 'UPDATED') {
                    console.log(res['data'])
                    hideModal();
                    alert('RESULT - ' + $('#id_lab_test').val() + ' - SUCCESSFULLY UPDATED ')
                } else if (res['data'] == 'NOT UPDATED') {
                    hideModal();
                    alert('RESULT - ' + $('#id_lab_test').val() + ' - CANNOT UPDATE')
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

    $('#submit-delete-result').click(function(e){
        var csrf = document.getElementsByName("csrfmiddlewaretoken")[0].value
        e.preventDefault()
        console.log("delete clicked")
        var id = $('#result_id').val()
        console.log(id)
        $.ajax({
            url: '../../labo/resultdelete/' + id,
            type: 'post',
            dataType: 'json',
            data: {
                csrfmiddlewaretoken: csrf,
                id: $('#result_id').val()
            },
            success: function(res){
                if (res['data'] == 'DELETED') {
                    console.log(res['data'])
                    hideModal();
                    alert('RESULT - ' + $('#result_test').val() + ' - SUCCESSFULLY DELETED ')
                } else if (res['data'] == 'NOT DELETED') {
                    hideModal();
                    alert('RESULT - ' + $('#result_test').val() + ' - CANNOT DELETED')
                    showModal();
                }
            }
        })
    })

});

function showModal(){
    $('#modal-result').modal('show')
}

function hideModal(){
    $('#modal-result').modal('hide')
}
