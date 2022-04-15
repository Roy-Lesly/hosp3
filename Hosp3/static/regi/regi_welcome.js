
$(document).ready(function(){

    $('.show-form').click(function(){
        console.log("button add staff clicked")
        $.ajax({
            url: '../../regi/staffCreate',
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

    $('.staff-update').click(function(e){
        e.preventDefault()
        console.log("button update staff clicked")
        var currentRow = $(this).closest('tr');
        var id = currentRow.find('td:eq(0)').html();
        console.log("id: " + id)
        $.ajax({
            url: '../../regi/staffUpdate/' + id,
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
            url: '../../regi/staffDelete/' + id,
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

});