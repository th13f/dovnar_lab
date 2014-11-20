$(document).ready(function () {
    function update_reports(){
        $.get("reports_list/", function(data){
            $("#reports").html(data);
        });
        $(".load_report").bind( "click", report_load);
        $(".delete_report").bind( "click", report_delete);
        $(".overwrite_report").bind( "click", report_overwrite);
    }

    function report_delete() {
        var report_id = $(this).closest("tr").find(".report_id").text();
        $.get("delete_report/"+report_id, function(data){});
        update_reports();
    }

    function report_load(){
        var report_id = $(this).closest("tr").find(".report_id").text();
        $.get("load_report/"+report_id, function(data){
            $("#tablice").html(data);
        });
    }

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
                update_reports();
            });
        }
    });

    function report_overwrite(){
        var report_name = $("#report_name").val();
        var report_id = $(this).closest("tr").find(".report_id").text();

        var x_axis = $( "#x_axis" ).val();
        var y_axis = $( "#y_axis" ).val();
        if (x_axis != "" && y_axis != "" && x_axis != y_axis){
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
            var content = { x_axis: x_axis, y_axis: y_axis, fixed: fixed, name: report_name};
            $.post("update_report/"+report_id, content, function(data){
                update_reports();
            });
        }
    }

    $(".load_report").bind( "click", report_load);
    $(".delete_report").bind( "click", report_delete);
    $(".overwrite_report").bind( "click", report_overwrite);
});