var searchForm = $("#search-form")  // or var searchForm = document.getElementById("#search-form")
var resultBox = $("#result-box")                // ok
var searchResult = $('.search-results')
var searchFormVal = searchForm.val()            // ok
var searchInput = $("#search-input")            // ok
var csrf = document.getElementsByName("csrfmiddlewaretoken")[0].value    // ok

$('#submit-form').hide()
$('#result-box').hide()
$(document).on('click', '#submit-form', function(e) {
    e.preventDefault();
    if ($('#id_xexam').val() !== "") {
        if ($('#id_xtype').val() !== "") {
            if ($('#id_staff').val() !== "") {
                if ($('#id_findings').val() !== "") {
                    console.log("True")
                    console.log($('#id_xexam').val())
                    $.ajax({
                        type: 'post',
                        url: '/radi/x_resultcreate/',
                        data: {
                            csrfmiddlewaretoken: csrf,
                            u_exam:$('#id_xexam').val(),
                            u_test:$('#id_xtype').val(),
                            staff:$('#id_staff').val(),
                            //paid:$('#id_paid').val(),
                            findings:$('#id_findings').val(),
                            code:$('#id_code').val(),
                        },
                        success: function(res){
                            console.log(res)
                            if (res == "SAVED") {
                                alert($('#id_xtype').val() + " Result Saved Successfully")
                            }
                            if (res == "NOT SAVED") {
                                alert("Form Data Not Valid")
                            } else if (res == "EXIST ALREADY") {
                                alert("Xray Test - " + $('#id_xtype').val() + " RESULT ALREADY EXIST !!!")
                            }
                        }
                    })
                }
                else
                    console.log("Fill Findings")
            }
            else
                alert("Select Sonographer (Staff) ?")
        }
        else
            alert("Select Xray Test")
    }
    else
        alert("Enter Book Num")
})


$(document).on('click', '#submit-update', function(e) {
    e.preventDefault();

    if ($('#id_xexam').val() !== "") {
        if ($('#id_xtype').val() !== "") {
            if ($('#id_paid').val() !== "") {
                if ($('#id_staff').val() !== "") {
                    if ($('#id_findings').val() !== "") {
                        $.ajax({
                            type: 'post',
                            url: url,
                            data: {
                                csrfmiddlewaretoken: csrf,
                                lexam:$('#id_xexam').val(),
                                ltype:$('#id_xtype').val(),
                                staff:$('#id_staff').val(),
                                paid:$('#id_paid').val(),
                                findings:$('#id_findings').val(),
                            },
                            success: function(res){
                                console.log(res)
                                if (res == "Result Saved") {
                                    alert($('#id_xexam').val() + " Result Saved Successfully")
                                } if (res == "Result Exist Already") {
                                    alert("Form Data Not Valid")
                                } else {
                                    alert("Xray Test - " + $('#id_xtype').val() + " Result Updated!!!")
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
            console.log("Enter Xray Test")
    }
    else
        console.log("Enter Book Num")
})


$('#id_category').on('change', function(e) {
    e.preventDefault();

    $.ajax({
        type: 'post',
        url: '/radi/search_xray_test/',
        data: {
            csrfmiddlewaretoken: csrf,
            category: $('#id_category').val(),
        },
        success: function(res){
            if (res == "") {
                console.log("No results")
            } else {
                var optionRow = '<option value="">---------</option>';
                res.forEach(function (object) {
                    object.forEach(function (item) {
                        optionRow += `<option value="${item.id}">${item.type_name}</option>`
                    });
                });
                $("#id_utype").html(optionRow);
            }
        }
    })
})


$('#id_xexam').change(function(e) {
    e.preventDefault();
    console.log('book_num changed')
    alert('book_num changed')

    $.ajax({
        type: 'post',
        url: '/radi/search_xray_test/',
        data: {
            csrfmiddlewaretoken: csrf,
            category: $('#id_xexam').val(),
        },
        success: function(res){
            if (res == "") {
                console.log("No results")
            } else {
                var optionRow = '<option value="">---------</option>';
                res.forEach(function (object) {
                    object.forEach(function (item) {
                        optionRow += `<option value="${item.id}">${item.type_name}</option>`
                    });
                });
                $("#id_xtype").html(optionRow);
            }
        }
    })
})


$('#id_code').on('keyup', function(e) {
    $.ajax({
        type: 'post',
        url: '/radi/validate_code/',
        data: {
            csrfmiddlewaretoken: csrf,
            code: $('#id_code').val(),
            staff: $('#id_staff').val(),
        },
        success: function(res){
            console.log(res)
            if (res == "VALID") {
                $('#submit-form').show()
            } else {
                $('#submit-form').hide()
            }
        }
    });
});


$('#search-input').on('keyup', function(e){
    sendSearchInputValue(e.target.value)
});


var sendSearchInputValue = (searchText) => {
    qt = $('#query-type').val()
    if (searchText.length > 3){
        $("#table-output").innerHTML = ""
        $('#result-box').show();
        fetch("../../radi/search_xray_exam/", {
            body: JSON.stringify({
                searchText: searchText,
                queryType: qt
            }),
            method: "POST",
        })
        .then((res) => res.json())
        .then((data) => {

            console.log(data)

            if (data.length===0){
                $("#div_no_data").show()
                $("#table-body").html('')
                $("#result-box").removeClass('not-visible')

            }else{
                $("#div_no_data").hide()
                $("#result-box").removeClass('not-visible')
                $("#table-body").html('')
                var i = 0;
                var rows = $.map(data[0], function(rowData) {
                    var row = $("<tr></tr>");
                    row.append($('<td class="class1"></td>').html(rowData.ys));
                    row.append($('<td class="class1"></td>').html(rowData.book_num));
                    row.append($('<td class="class2"></td>').html(rowData.full_name));
                    row.append($('<td class="class3"></td>').html(rowData.address));
                    row.append($('<td class="class4"></td>').html(rowData.age));
                    row.append($('<td class="class4"></td>').html(rowData.sex));
                    row.append($('<td class="class4"></td>').html(rowData.Phone));
                    row.append($('<td class="class4"></td>').html(rowData.date_created));

                    row.on("click", function() {
                      fillForm(rowData);
                      $('#result-box').hide();
                      $('#card-search').hide();
                      $('#card-test').hide();
                    });

                return row;
                });

                $(".table").append(rows);

                function fillForm(rowData) {
                    var form = $("#id_patient");
                    $('#id_xexam').val(rowData.book_num);
                    getTestItems(rowData.book_num);

                }

            }
        });

    }else{
        $('#result-box').hide();
    }
}


function getTestItems(data) {
    console.log("here")
    console.log(data)
    $.ajax({
        type: 'post',
        url: "../../radi/search_xray_test/",
        data: {
            csrfmiddlewaretoken: csrf,
            book_num: data
        },
        success: function(res){
            if (res[1] == "VALID") {
                console.log(res[0])
                console.log(res[0][0]['xtype'])
                console.log(res[0][1])
                var optionRow = '<option value="">---------</option>';
                res[0].forEach(function (object) {
                    optionRow += `<option value="${object['id']}">${object["xtype"]}</option>`
                });
                $("#id_xtype").html(optionRow);
                console.log(optionRow)
                console.log('succeeded')
                $('#submit-form').show()
            } else if (res[1] == "NON VALID") {
                console.log(res[1])
                //$('#submit-form').hide()
            }
        }
    });
}

