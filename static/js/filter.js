/*$(".add-btn").on(function(e){
    var thisCheck = $(this);
    var checkbox = $('#'+$(this).attr('for'));
    var filter_el = $("#stores").prev().children(".ui-input-search").children("input");
    var filter_val = filter_el.val();
//    var filter_query = filter_val+$(this).text();
//        filter_el.val(filter_query);
//        filter_el.trigger("change");
    if ( checkbox.is(':checked') ) {
        filter_val = filter_val.replace($(this).text(), '');
        filter_el.val(filter_val);
        filter_el.trigger("change");
    }else{
        filter_val = filter_val+$(this).text();
        filter_el.val(filter_val);
        filter_el.trigger("change");
        filter_el.trigger("keyup");
    }
    //var filter_query = $(this).text();
});*/


$(".add-btn").bind('touchstart mousedown', function(){
    var thisCheck = $(this);
    var checkbox = $('#'+$(this).attr('for'));
    var filter_el = $("#stores").prev().children(".ui-input-search").children("input");
    //var filter_val = filter_el.val();

    if ( checkbox.is(':checked') ) {
        //filter_val = filter_val.replace($(this).text(), '');
        filter_el.val(filter_el.val().replace($(this).text(), ''));
        filter_el.trigger("change");
    }else{
        //filter_val = filter_val+$(this).text();
        filter_el.val(filter_el.val()+$(this).text());
        filter_el.trigger("change");
    }
});
