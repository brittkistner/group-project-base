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

$(document).ready(function () {
   // Change this to the location of your server-side upload handler:
    var url = 'upload/comment';
    var weekNumber;
    var day;
    var slideSet;
    var slideNumber;

    var review_url = function(url){
       //figure out regex
        weekNumber = parseInt(url.split('/')[3]);
        day = url.split('/')[4]; //string
        slideSet= parseInt(url.split('/')[6]);
        slideNumber = parseInt(url.split('/')[7]);
    };

    'use strict';
    $('#fileupload').fileupload({
        url: url,
        dataType: 'json',
        done: function (e, data) {
            $.each(data.result.files, function (index, file) {
                $('<p/>').text(file.name).appendTo('#files');
                $('<p/>').html("<img src='" + file.url + "' width=160px/>").appendTo('#files');
            });
        },
        progressall: function (e, data) {
            var progress = parseInt(data.loaded / data.total * 100, 10);
            $('#progress .progress-bar').css(
                'width',
                progress + '%'
            );
        }
    }).prop('disabled', !$.support.fileInput)
        .parent().addClass($.support.fileInput ? undefined : 'disabled');
});