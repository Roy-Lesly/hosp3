// alert("labo/createPatientSearch.js")
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
var labtests = document.getElementsByName("lab_tests")
var fees = $("#id_fees")

// =========== Search_Patient and display in searchResult div ==========
searchResult.hide();
var sendSearchInputValue = (searchText) => {        // searchText = e.target.value
    qt = queryType.val()
    if (searchText.length > 3){
        tableOutput.innerHTML = ""
        searchResult.show();
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
                resultBox.removeClass('not-visible')
                regForm.removeClass('not-visible')
                tableBody.empty().html("No Results Found !!!")

            }else{
                resultBox.removeClass('not-visible')
                tableBody.html('')
                var i = 0;
                console.log(data)
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
                    $('#id_lexam').val(rowData.book_num);
                }

            }
        });

    }else{
        searchResult.hide();
    }
}

$(searchInput).on('keyup', function(e){
    sendSearchInputValue(e.target.value)
});



$(labtests).on('change', function() {
    var valArray = $(this).val()
    var clsAttr = [].map.call(this.children, function (e) {
        return e.getAttribute('class')
    })                                 // ok, works well
    var a = []
    for (var i = 0; i < valArray.length; i++) {
        var b = clsAttr[valArray[i]]
        a.push(b)
    }
    //console.log(a)
    sum = eval(clsAttr.join("+"))      // ok, works well
    sum1 = eval(valArray.join("+"))      // ok, works well
    sum2 = eval(a.join("+"))      // ok, works well
    console.log(valArray)
    console.log(a)
    $(fees).val(sum2)
});