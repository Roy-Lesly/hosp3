var url =window.location.href         // ok
var searchForm = $("#search-form")  // or var searchForm = document.getElementById("#search-form")
var resultBox = $("#result-box")                // ok
var searchResult = $('.search-results')
var searchFormVal = searchForm.val()            // ok
var searchInput = $("#search-input")            // ok
var csrf = document.getElementsByName("csrfmiddlewaretoken")[0].value    // ok

$(document).on('click', '#submit-form', function(e) {
    e.preventDefault();

    $.ajax({
        type: 'post',
        url: '/labo/patcreate/',
        data: {
            csrfmiddlewaretoken: csrf,
            patient:$('#id_sn').val(),
        },
        success: function(res){
            if (res == "Patient Not Created")
                alert($('#id_fullname').val() + " ALREADY EXIST")
            else
                alert($('#id_fullname').val() + " REGISTERED SUCCESSFULLY !!!")
        }
    });
});