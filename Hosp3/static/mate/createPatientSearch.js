var url =window.location.href         // ok
var searchForm = $("#search-form")  // or var searchForm = document.getElementById("#search-form")               // ok
var searchResult = $('.search-results')
var searchFormVal = searchForm.val()            // ok
var searchInput = $("#search-input")            // ok
var csrf = document.getElementsByName("csrfmiddlewaretoken")[0].value    // ok
var tableOutput = $(".table-output")
var tableBody = $(".table-body")
var queryType = $('#query-type')
var regForm = $('.reg-form')
var labtests = document.getElementsByName("lab_tests")
var fees = $("#id_fees")


$("#result-box").hide()
// =========== Search_Patient and display in searchResult div ==========
searchResult.hide();
var sendSearchInputValue = (searchText) => {        // searchText = e.target.value
    qt = queryType.val()
    if (searchText.length > 3){
        tableOutput.innerHTML = ""
        $("#result-box").show();
        fetch("../../regi/search_patient/", {
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
                $("#result-box").show()
                regForm.removeClass('not-visible')
                tableBody.empty().html("No Results Found !!!")

            }else{
                $("#result-box").show()
                regForm.addClass('not-visible')
                tableBody.html('')
                var i = 0;
                var rows = $.map(data[0], function(rowData) {
                    var row = $("<tr></tr>");
                    row.append($('<td class="class1"></td>').html(rowData.sn));
                    row.append($('<td class="class1"></td>').html(rowData.reg_num));
                    row.append($('<td class="class2"></td>').html(rowData.full_name));
                    row.append($('<td class="class3"></td>').html(rowData.address));
                    row.append($('<td class="class4"></td>').html(rowData.age));
                    row.append($('<td class="class4"></td>').html(rowData.sex));
                    row.append($('<td class="class4"></td>').html(rowData.Phone));
                    row.append($('<td class="class4"></td>').html(rowData.date_created));

                    row.on("click", function() {
                      fillForm(rowData);
                      $("#result-box").show().hide()
                    });

                return row;
                });

                $(".table").append(rows);

                function fillForm(rowData) {
                    var form = $("#id_patient");
                    $('#id_sn').val(rowData.sn);
                    $('#id_full_name').val(rowData.full_name);
                    $('#id_phone').val(rowData.Phone);
                    $('#id_address').val(rowData.address);
                    $('#id_age').val(rowData.age);
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


$(function() {
    var tableData = [
        {
          name: "patient1",
          email: "n@gmail.com",
          address: "km5",
          age: "30"
        }, {
          name: "patient2",
          email: "s@gmail.com",
          address: "mboppi",
          age: "40"
        }
      ];

  var rows = $.map(tableData, function(rowData) {
    var row = $("<tr></tr>");
    row.append($('<td class="class1"></td>').html(rowData.name));
    row.append($('<td class="class2"></td>').html(rowData.email));
    row.append($('<td class="class3"></td>').html(rowData.address));
    row.append($('<td class="class4"></td>').html(rowData.age));

    row.on("click", function() {
      fillForm(rowData);
    });

    return row;
  });

  $(".data-table").append(rows);

  function fillForm(rowData) {
    var form = $(".data-form");

    form.find("input.name").val(rowData.name);
    form.find("input.email").val(rowData.email);
    form.find("input.address").val(rowData.address);
    form.find("input.age").val(rowData.age);
  }
});