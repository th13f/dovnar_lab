$(document).ready(function () {
    function update_fixed(){
        var x_axis = $( "#x_axis" ).val();
        var y_axis = $( "#y_axis" ).val();
        if (x_axis != "" && y_axis != "" && x_axis != y_axis){
            $.post("get_third_table/", { x_axis: x_axis, y_axis: y_axis }, function(data){
                $("#fixed").html(data);
                $.getScript('static/js/fixed_submit.js');
            });
        }
    }

    $( "#x_axis" ).change(function() {
        update_fixed();
    });
    $( "#y_axis" ).change(function() {
        update_fixed();
    });
    $("#save_report").click(function(){
        var report_name = $("#report_name").val();

        var x_axis = $( "#x_axis" ).val();
        var y_axis = $( "#y_axis" ).val();
        if (x_axis != "" && y_axis != "" && x_axis != y_axis && report_name != ""){
            var fixed_start = $("#fixed_start").val();
            var fixed_end = $("#fixed_end").val();
            var fixed = null;
            if (fixed_start == undefined){
                var array = $("#fixed_selector").val();
                if (array.length>0)
                    fixed = {values: "[" + array.join(", ") + "]"};
                else
                    fixed = {values: "[]"}
            }
            else
                fixed = {start:fixed_start, end:fixed_end};
            var content = { x_axis: x_axis, y_axis: y_axis, fixed: fixed};
            $.post("save_report/"+report_name, content, function(data){

            });
        }
    });
});
