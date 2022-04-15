var csrf = document.getElementsByName("csrfmiddlewaretoken")[0].value
// register()

//$(document).on('submit', 'form-register', register(e))
$(document).on('submit', '#form-register', function(e){
    e.preventDefault();
    console.log('register submit')

    $.ajax({
        type: 'POST',
        url: '../../../'+'register/',
        data: {
            username: $('#id_username_r').val(),
            password: $('#id_password1').val(),
            password1: $('#id_password1').val(),
            password2: $('#id_password2').val(),
            csrfmiddlewaretoken: csrf
        },
        success: function(res){
            console.log(res.data)
            alert(res.data)


        }
    })
})

/*
function register(e) {
    $('#submit-register').on('submit', function(e) {
        e.preventDefault();
        console.log('submit-register')
    });
}*/