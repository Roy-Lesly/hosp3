
$('#submit-modal-create-pat').click(function(e){
    e.preventDefault()
    var csrf = document.getElementsByName("csrfmiddlewaretoken")[0].value
    var r = $('#id_reg_num').val()
    var rn = zeroPad(r)
    createRegisPat(rn);
});


function zeroPad(r_n) {
    var zero = 5 - r_n.toString().length + 1;
    var x = Array(+(zero > 0 && zero)).join("0") + r_n
    return 'X#' + x + '_' + (now.getFullYear()).toString().slice(2, 4);
}



function createRegisPat(rn){
    $.ajax({
        url: '../../regi/patCreateModal/',
        type: 'post',
        dataType: 'json',
        data: {
            csrfmiddlewaretoken: csrf,
            reg_num: rn,
            first_name:$('#id_first_name').val(),
            last_name:$('#id_last_name').val(),
            full_name:'x',
            address:$('#id_address1').val(),
            sex:$('#id_sex').val(),
            dob:$('#id_dob').val(),
            age:0,
            Phone:$('#id_Phone').val(),
        },
        success: function(res){
            if (res['data'] == 'SAVED') {
                console.log(res['data'])
                console.log(res['patient'])
                $("#card-test").hide()
                $("#card-exam").hide()
                $("#search-box").hide()
                $("#result-box").hide()
                $("#card-patient").show()
                hideModal();
                alert('Patient -' + $('#id_first_name').val() + ' - SUCCESSFULLY SAVED ')
                $('#id_sn').val(res['patient'][0])
                $('#id_full_name_p').val(res['patient'][1])
                $('#id_address').val(res['patient'][2])
                $('#id_age_p').val(res['patient'][3])
                $('#id_phone_p').val(res['patient'][4])

            } else if (res['data'] == 'NOT SAVED') {
                hideModal();
                alert('Patient - ' + $('#id_first_name').val() + ' - NOT SAVED (Name or Phone May Already Exist)')
                showModal();
            }
        }
    })
}