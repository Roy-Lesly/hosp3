var url =window.location.href         // ok
var searchForm = $("#search-form")  // or var searchForm = document.getElementById("#search-form")            // ok
var searchFormVal = searchForm.val()            // ok
var searchInput = $("#search-input")            // ok
var csrf = document.getElementsByName("csrfmiddlewaretoken")[0].value    // ok
// var labtests = document.getElementsByName("lab_tests")
var searchFormVal = searchForm.val()            // ok
var searchInput = $("#search-input")            // ok
var csrf = document.getElementsByName("csrfmiddlewaretoken")[0].value    // ok

$('#submit-form').hide()
$('#result-box').hide();
$('#id_code').hide();

// =========== Search_Patient and display in searchResult div ==========

var sendSearchInputValue = (searchText) => {        // searchText = e.target.value
    qt = $('#query-type').val()
    if (searchText.length > 3){
        $(".table-output").innerHTML = ""
        $('#result-box').show();
        console.log("getting Lab Exams ......")
        fetch("../search_labo_exam/", {
            body: JSON.stringify({
                searchText: searchText,
                queryType: qt
            }),
            method: "POST",
        })
        .then((res) => res.json())
        .then((data) => {

            if (data.length===0){
                $('#result-box').removeClass('not-visible')
                // regForm.removeClass('not-visible')
                $("#result-table-body").empty().html("No Results Found !!!")

            }else{
                $("#result-box").removeClass('not-visible')
                $("#result-table-body").html('')
                // var i = 0;
                var rows = $.map(data[0], function(rowData) {
                    var row = $("<tr></tr>");
                    row.append($('<td class="class1"></td>').html(rowData.book_num));
                    row.append($('<td class="class1"></td>').html(rowData.full_name));
                    row.append($('<td class="class3"></td>').html(rowData.age));
                    row.append($('<td class="class4"></td>').html(rowData.sex));
                    row.append($('<td class="class4"></td>').html(rowData.address));
                    row.append($('<td class="class4"></td>').html(rowData.Phone));
                    row.append($('<td class="class4"></td>').html(rowData.ln));
                    row.append($('<td class="class4"></td>').html(rowData.date_created));

                    row.on("click", function() {
                      fillForm(rowData);
                    });

                return row;
                });

                $(".table").append(rows);

                function fillForm(rowData) {
                    console.log("row clicked")
                    $('#result-box').hide();
                    // $('#query-card').hide();
                    $('#id_lab_exam').val(rowData.book_num);
                    getTests();
                }

            }
        });

    }else{
        $('.search-results').hide();
    }
}

$(searchInput).on('keyup', function(e){
    sendSearchInputValue(e.target.value)
});


$(document).on('click', '#submit-form', function(e) {
    e.preventDefault();
    console.log($('#id_ltype').val())
    console.log($('#id_lab_exam').val())
    console.log($('#id_staff').val())
    console.log($('#id_findings').val())
    if ($('#id_lexam').val() !== "") {
        if ($('#id_ltype').val() !== "") {
            if ($('#id_paid').val() !== "") {
                $.ajax({
                    type: 'post',
                    url: '/labo/resultcreate/',
                    data: {
                        csrfmiddlewaretoken: csrf,
                        lexam:$('#id_lab_exam').val(),
                        ltype:$('#id_ltype').val(),
                        staff:$('#id_staff').val(),
                        findings:$('#id_findings').val(),
                    },
                    success: function(res){
                        console.log(res)
                        if (res == "RESULT CREATED") {
                            alert("RESULTS FOR " + $('#id_ltype').val() + " CREATED SUCCESSFULLY")
                            $('#id_code').val(''),
                            $('#id_ltype').val(''),
                            $('#id_staff').val(''),
                            $('#id_findings').val(''),
                            $('#submit-form').hide()
                        }
                        else if (res == "RESULT NOT CREATED") {
                            alert("FORM DATA NOT VALID")
                        }
                        else if (res == "RESULT ALREADY EXIST") {
                            alert("Lab Result for - " + $('#id_ltype').val() + " ALREADY EXIST" + " !!!")
                            $('#id_code').val(''),
                            $('#id_ltype').val(''),
                            $('#id_staff').val(''),
                            $('#id_findings').val(''),
                            $('#submit-form').hide()

                        }
                    }
                });
            }
            else
                alert("Enter Amount Paid")
        }
        else
            alert("Enter Lab Test")
    }
    else
        alert("Enter Book Num")
});


$(document).on('click', '#submit-update', function(e) {
    e.preventDefault();

    if ($('#id_lexam').val() !== "") {
        if ($('#id_ltype').val() !== "") {
            if ($('#id_paid').val() !== "") {
                if ($('#id_staff').val() !== "") {
                    if ($('#id_findings').val() !== "") {
                        $.ajax({
                            type: 'post',
                            url: url,
                            data: {
                                csrfmiddlewaretoken: csrf,
                                lexam:$('#id_lexam').val(),
                                ltype:$('#id_ltype').val(),
                                staff:$('#id_staff').val(),
                                paid:$('#id_paid').val(),
                                findings:$('#id_findings').val(),
                            },
                            success: function(res){
                                console.log(res)
                                if (res == "Result Saved") {
                                    alert($('#id_lexam').val() + " Result Saved Successfully")
                                } if (res == "Result Exist Already") {
                                    alert("Form Data Not Valid")
                                } else {
                                    alert("Lab Test - " + $('#id_ltype').val() + " Result Updated!!!")
                                }
                            }
                        })
                    }
                    else
                        console.log("Enter Findings")
                }
                else
                    console.log("Staff Performed")
            }
            else
                console.log("Enter Amount Paid")
        }
        else
            console.log("Enter Lab Test")
    }
    else
        console.log("Enter Book Num")
})


/*
$('#id_ltype').on('change', function(e) {
    if ($('#id_paid').val() !== "") {
        console.log("2")
        $('#submit-form').show();
    }
}); */


function getTests () {
    console.log("getting tests.....")
    $.ajax({
        type: 'post',
        url: '../search_labo_test/',
        data: {
            csrfmiddlewaretoken: csrf,
            book_num: $('#id_lab_exam').val(),
        },
        success: function(res){
            console.log(res)
            $("#id_ltype").html('');
            if (res == "") {
                console.log("No results")
            } else {
                var optionRow = '<option value="">---------</option>';
                res.forEach(function (object) {
                    object.forEach(function (item) {
                        optionRow += `<option value="${item.id}">${item.ltype_name}</option>`
                    });
                });
                $("#id_ltype").html(optionRow);
            }
        }
    })
}


$('#id_staff').on('change', function(e) {
    console.log("staff clicked")
    $('#id_code').show();
});


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

