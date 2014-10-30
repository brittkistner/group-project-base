(function($) {

  var allPanels = $('.accordion > div').hide();

  $('.show > div > a').click(function() {
    allPanels.slideUp();
    $(this).parent().next().slideDown();
    return false;
  });

})(jQuery);

$(document).ready(function () {
    var weekNumber;
    var day;
    var slideSet;
    var slideNumber;
    var slideHeader;
    var url;
    var headerHtml;

    $('#comments1').hide();
    $('#btn2').click(function () {
        $('#resources1').hide();
        $('#comments1').show();
    });

    $('#btn1').click(function () {
        $('#resources1').show();
        $('#comments1').show();
    });

    var review_url = function(path){
       //figure out regex
        url = path;
        weekNumber = parseInt(path.split('/')[3]);
        day = path.split('/')[4]; //string
        slideSet= parseInt(path.split('/')[6]);
        slideNumber = parseInt(path.split('/')[7]);
    };

    var getHeader = function(){
        headerHtml = $('.present').find('h2');
        slideHeader = headerHtml[0].firstChild.nodeValue;
    };

   $('#save').on('click', function(){
       review_url(location.pathname);
       getHeader();
       $.ajax({
            url: '/create_comment/' + weekNumber + '/'
                + day + '/' + slideSet + '/'
                + slideNumber + '/' + slideHeader
                + '/' + url + '/',
            type: 'POST',
            dataType: 'json',
            data: $(this).serialize(), //what should be serialized here?
            success: function(response) {
                console.log('success');
                $('#resources1').hide();
                $('#comments1').show();
            },
            error: function(response) {
                console.log(response.body);
            }
        });
   });



   //Drag and drop below

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