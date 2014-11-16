$(document).ready(function () {
    function update_table(fixed){
        var x_axis = $( "#x_axis" ).val();
        var y_axis = $( "#y_axis" ).val();
        if (x_axis != "" && y_axis != "" && x_axis != y_axis){
            $.post("get_tablice_html/", { x_axis: x_axis, y_axis: y_axis ,fixed:fixed}, function(data){
                $("#tablice").html(data);
            });
        }
    }

    $( "#submit_dates" ).click(function() {
        var fixed_start = $("#fixed_start").val();
        var fixed_end = $("#fixed_end").val();
        var fixed = {start:fixed_start, end:fixed_end};
        update_table(fixed);
    });

    $("#fixed_selector").change(function(){
        var array = $(this).val().join(", ");
        array = "[" + array + "]";
        var fixed = {values: array};
        update_table(fixed);
    });
});