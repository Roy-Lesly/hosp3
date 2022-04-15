var labtests = document.getElementsByName("lab_tests")

function labtests (e) {
    return $(labtests).on('change', function() {
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
};

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