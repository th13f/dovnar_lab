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
});
