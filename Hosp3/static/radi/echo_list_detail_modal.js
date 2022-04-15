
$(".finding-table .tr").on("click", function() {
    var id = $(this).find(".id").text();
    console.log($(this).find(".id").text())
    $.ajax({
        url: '../../radi/u_resultdetail/' + id,
        type: 'get',
        dataType: 'json',
        beforeSend: function(){
            $('#modal-noti').modal('show')
        },
        success: function(data){
            $('#modal-noti .modal-content').html(data.html_form);
            console.log(data)
            console.log("=================")
            console.log(data.context)
            console.log(data.context["sn"])
            $('#pat_name').text(data.context["pat_name"])
            $('#sn').text(data.context["sn"])
            $('#un').text(data.context["un"])
            $('#bn').text(data.context["bn"])
            $('#test').text(data.context["test"])
            $('#pn').text(data.context["phone"])
            $('#findings').text(data.context["findings"])
            $('#staff').text(data.context["staff"])
            $('#date_created').text(data.context["date_created"])
            $('#date_updated').text(data.context["date_updated"])


            var rows = $.map(data.context.data, function(rowData) {
                var row = $("<tr></tr>");
                row.append($('<td class="class1"></td>').html(rowData.sn));
                row.append($('<td class="class1"></td>').html(rowData.bn));
                row.append($('<td class="class2"></td>').html(rowData.full_name));
                row.append($('<td class="class3"></td>').html(rowData.address));
                row.append($('<td class="class3"></td>').html(rowData.ward));
                row.append($('<td class="class4"></td>').html(rowData.sex));
                row.append($('<td class="class4"></td>').html(rowData.age));
                row.append($('<td class="class4"></td>').html(rowData.Phone));
                row.append($('<td class="class4"></td>').html(rowData.date_created));

                row.on("click", function() {
                    console.log("row clicked1")
                    $('#exam-table-modal').hide();
                    $('#card-exam-item-modal').show();
                      fillForm(rowData);
                      });
                return row;
            });
            $("#id_tbody").append(rows);
            $('#card-exam-item-modal').hide();

            function fillForm(rowData) {
                var form = $("#id_patient");
                $('#id_uexam_modal').val(rowData.bn);
            }
        }
    });
});


$(".exam-table").on("click", ".tr", function() {
    var id = $(this).find(".bn1").text();
    console.log($(this).find(".bn1").text())
    console.log($(this))
    $.ajax({
        url: '../../radi/u_examdetail/' + id,
        type: 'get',
        dataType: 'json',
        beforeSend: function(){
            $('#modal-noti').modal('show')
        },
        success: function(data){
            $('#modal-noti .modal-content').html(data.html_form);
            //console.log(data)
            console.log(data.context.test)
            var x = 1
            $.each(data.context.test, function(test_id, name) {
                $('#t' + x).text(test_id);
                $('#id-' + x).text(name);
                x++;
            });
            $('#pat_name').text(data.context["pat_name"])
            $('#sn').text(data.context["sn"])
            $('#un').text(data.context["un"])
            $('#bn').text(data.context["bn"])
            $('#ad').text(data.context["address"])
            $('#wd').text(data.context["ward"])
            $('#pn').text(data.context["phone"])
            $('#staff').text(data.context["staff"])
            $('#date_created').text(data.context["date_created"])
            $('#date_updated').text(data.context["date_updated"])


            var rows = $.map(data.context.data, function(rowData) {
                var row = $("<tr></tr>");
                row.append($('<td class="class1"></td>').html(rowData.sn));
                row.append($('<td class="class1"></td>').html(rowData.bn));
                row.append($('<td class="class2"></td>').html(rowData.full_name));
                row.append($('<td class="class3"></td>').html(rowData.address));
                row.append($('<td class="class3"></td>').html(rowData.ward));
                row.append($('<td class="class4"></td>').html(rowData.sex));
                row.append($('<td class="class4"></td>').html(rowData.age));
                row.append($('<td class="class4"></td>').html(rowData.Phone));
                row.append($('<td class="class4"></td>').html(rowData.date_created));

                row.on("click", function() {
                    console.log("row clicked1")
                    $('#exam-table-modal').hide();
                    $('#card-exam-item-modal').show();
                      fillForm(rowData);
                      });
                return row;
            });
            $("#id_tbody").append(rows);
            $('#card-exam-item-modal').hide();

            function fillForm(rowData) {
                var form = $("#id_patient");
                $('#id_uexam_modal').val(rowData.bn);
            }
        }
    });
});