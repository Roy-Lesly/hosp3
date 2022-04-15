var url =window.location.href         // ok
var searchForm = $("#search-form")  // or var searchForm = document.getElementById("#search-form")
var resultBox = $("#result-box")                // ok
var searchResult = $('.search-results')
var searchFormVal = searchForm.val()            // ok
var searchInput = $("#search-input")            // ok
var csrf = document.getElementsByName("csrfmiddlewaretoken")[0].value    // ok
var url =window.location.href         // ok
var searchForm = $("#search-form")  // or var searchForm = document.getElementById("#search-form")
var resultBox = $("#result-box")                // ok
var searchResult = $('.search-results')
var searchFormVal = searchForm.val()            // ok
var searchInput = $("#search-input")            // ok
var csrf = document.getElementsByName("csrfmiddlewaretoken")[0].value    // ok
var tableOutput = $(".table-output")
var tableBody = $(".table-body")
var queryType = $('#query-type')
var regForm = $('.reg-form')

$('.search-results').hide();
$('#submit-exam').hide();
$('#submit-exam-item').hide();
$('#exam-item-form').hide();

search();
submitExam();
submitExamItem();
categoryChange();
displayCreateExam();
displayCreateLabTest();


// =========== Search_Patient and display in searchResult div ==========
var sendSearchInputValue = (searchText) => {        // searchText = e.target.value
    qt = $('#query-type').val()
    if (searchText.length > 3){
        tableOutput.innerHTML = ""
        searchResult.show();
        fetch("../search_labo_patient/", {
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
                resultBox.removeClass('not-visible')
                regForm.removeClass('not-visible')
                tableBody.empty().html("No Results Found !!!")

            }else{
                resultBox.removeClass('not-visible')
                regForm.addClass('not-visible')
                tableBody.html('')
                var i = 0;
                var rows = $.map(data[0], function(rowData) {
                    var row = $("<tr></tr>");
                    row.append($('<td class="class1"></td>').html(rowData.ln));
                    row.append($('<td class="class1"></td>').html(rowData.sn));
                    row.append($('<td class="class1"></td>').html(rowData.full_name));
                    row.append($('<td class="class3"></td>').html(rowData.age));
                    row.append($('<td class="class4"></td>').html(rowData.sex));
                    row.append($('<td class="class4"></td>').html(rowData.address));
                    row.append($('<td class="class4"></td>').html(rowData.Phone));
                    row.append($('<td class="class4"></td>').html(rowData.date_created));

                    row.on("click", function() {
                        searchResult.hide();
                        fillForm(rowData);
                    });

                return row;
                });

                $(".table").append(rows);

                function fillForm(rowData) {

                    $('#id_patient').val(rowData.ln);
                }

            }
        });

    }else{
        searchResult.hide();
    }
}

function search (e) {
    return $("#search-input").on('keyup', function(e){
        sendSearchInputValue(e.target.value)
    });
};
// ========== End Search ===============================================



// =========== Submit Exam Form ========================================
function submitExam (e) {
    $(document).on('click', '#submit-exam', function(e) {
        e.preventDefault();

        if ($('#id_patient').val() !== "") {
            if ($('input[name=book_num1]').val() !== "") {
                if ($('#id_prescriber').val() !== "") {
                    if ($('#id_ward').val() !== "") {
                        if ($('input[name=paid_exam]').val() !== "") {
                            console.log("True")
                            sendForm1();
                        }
                        else
                            alert("Enter Amount Paid")
                    }
                    else
                        alert("Select Ward")
                }
                else
                    alert("Enter Prescriber Info")
            }
            else
                alert("Enter Book Num")
        }
        else
            alert("Get Patient Id")

    });
};
// ========== End Submit ===============================================

// =========== Submit Exam Item Form ========================================
function submitExamItem (e) {
    $(document).on('click', '#submit-exam-item', function(e) {
        e.preventDefault();
        sendForm2();
    });
};
// ========== End Submit ===============================================

function sendForm1 () {
    $.ajax({
        type: 'post',
        url: '/labo/examcreate/',
        data: {
            csrfmiddlewaretoken: csrf,
            patient:$('#id_patient').val(),
            book_num:$('#id_book_num').val(),
            prescriber:$('#id_prescriber').val(),
            ward:$('#id_ward').val(),
            paid:$('input[name=paid_exam]').val(),
        },
        success: function(res){
            if (res == "EXAM CREATED") {
                alert("Exam " + $('#id_book_num').val() + " SUCCESSFULLY CREATED")
                $('#submit-exam').hide();
                $('#exam-item-form').show();
                $('#card1').hide();
                $('#card-search').hide();
                sendForm2();
            } else if (res == "EXAM NOT CREATED") {
                alert("Exam Data Not Valid")
            } else {
                alert("Check Book_num - " + $('#id_book_num').val() + "!!! or Register Lab Department")
            }
        }
    })
}


function sendForm2 () {
    $('input[name=book_num2]').val($('input[name=book_num1]').val())        // fill book_num 2 with 1
    if ($('input[name=book_num2]').val() !== "") {
        if ($('input[name=paid-exam-item]').val() !== "") {
            console.log($('input[name=paid-exam-item]').val())
            if ($('#ltype').val() !== "") {
                $.ajax({
                type: 'post',
                url: "../newtestinnewexam/",
                data: {
                    csrfmiddlewaretoken: csrf,
                    lexam:$('#id_lexam').val(),
                    ltype:$('#id_ltype').val(),
                    paid:$('input[name=paid-exam-item]').val(),
                },
                success: function(res){
                    console.log(res)
                    if (res == "EXAM ITEM CREATED") {
                        alert("LAB TEST SUCCESSFULLY CREATED FOR " + $('#id_lexam').val())
                        console.log($('#id_paid').val())
                        $('input[name=paid-exam-item]').val('')
                        $('#id_ltype').val('')
                        $('#id_category').val('')
                        $('#submit-exam-item').hide();
                    } if (res == "EXAM ITEM ALREADY EXIST") {
                        alert("LAB TEST ALREADY EXIST")
                        $('#submit-exam-item').hide();
                    } if (res == "EXAM ITEM NOT CREATED") {
                        alert("Lab Test - " + $('#id_ltype').val() + " LAB TEST NOT CREATED!!!")
                    }
                }
                });
            }
            else
                alert("Enter Lab Test")
        }
        else
            alert("Enter Lab Test Amount")
    }
    else
        alert("Enter Book Num")
};


function categoryChange(e) {
    $('#id_category').on('change', function(e) {
        e.preventDefault();

        $.ajax({
            type: 'post',
            url: '/labo/search_labo_test/',
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
                    $("#id_ltype").html(optionRow);
                }
            }
        })
    });
};


function displayCreateExam(e) {
    $('#id_ward').on('change', function(e) {
        e.preventDefault();
        console.log('ward changed')
        $('#submit-exam').show();
    });
};


function displayCreateLabTest(e) {
    $('#id_ltype').on('change', function(e) {
        e.preventDefault();
        $('#submit-exam-item').show();
    });
};