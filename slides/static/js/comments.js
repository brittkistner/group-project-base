(function($) {

  var allPanels = $('.accordion > div').hide();

  $('.show > div > a').click(function() {
    allPanels.slideUp();
    $(this).parent().next().slideDown();
    return false;
  });

})(jQuery);

$(document).ready(function () {
    $('#comments1').hide();
    $('#btn2').click(function () {
        $('#resources1').hide();
        $('#comments1').show();
    });

    $('#btn1').click(function () {
        $('#resources1').show();
        $('#comments1').show();
    });

});

//$(document).ready(function () {
//    $('#comments1').hide();
//    $('#btn2').click(function () {
//        $('#resources1').hide();
//        $('#comments1').show();
//    });
//
//});