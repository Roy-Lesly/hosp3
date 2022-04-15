
$('#submit-update').hide();
fetchInfo();

$('#id_code').on('keyup', function(e) {
    $.ajax({
        type: 'post',
        url: '/labo/validate_code/',
        data: {
            csrfmiddlewaretoken: csrf,
            code: $('#id_code').val(),
            staff: $('#id_staff').val(),
        },
        success: function(res){
            console.log(res)
            if (res == "VALID") {
                $('#submit-form').show()
                $('#submit-update').show()
            } else {
                $('#submit-form').hide()
                $('#submit-update').hide()
            }
        }
    });
});

function fetchInfo () {

    console.log("fetched")
    fetch("../resultupdate/2")
        .then((res) => res.json())
        .then((data) => {
            console.log(data)
        });
}