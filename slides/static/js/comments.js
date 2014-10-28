(function($) {
    
  var allPanels = $('.accordion > div').hide();
    
  $('.show > div > a').click(function() {
    allPanels.slideUp();
    $(this).parent().next().slideDown();
    return false;
  });

})(jQuery);
