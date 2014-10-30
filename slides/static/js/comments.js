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
    var fileData = [];

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
        weekNumber = path.split('/')[1];
        day = path.split('/')[2]; //string
        if (path.split('/').length < 5){
            slideSet = 0;
            slideNumber = 0;
        } else if (path.split('/').length < 6){
            slideSet= parseInt(path.split('/')[4]);
            slideNumber = 0;
        } else {
            slideSet= parseInt(path.split('/')[4]);
            slideNumber = parseInt(path.split('/')[5]);
        }
        console.log(weekNumber, day, slideSet, slideNumber);
    };

    var getHeader = function(){
//        headerHtml = $('.present').find('h2');
//        console.log(headerHtml);
//        slideHeader = headerHtml[0].firstChild.nodeValue;
        slideHeader = "Hello World";
    };


   $('#save').on('click', function(){
       review_url(location.pathname);
       getHeader();
       console.log('passed review_url and getHeader');
       console.log(fileData);
       $.ajax({
           //think about passing the data differently (maybe through data?)
            url: '/create_comment/' + weekNumber + '/'
                + day + '/' + slideSet + '/'
                + slideNumber + '/',
            type: 'POST',
            dataType: 'json',
            data: {
                'text': JSON.stringify($('#resource-area').val()),
                'slide_header': JSON.stringify(slideHeader),
                'files[]' : fileData,
                'url' : JSON.stringify(url)
            },
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
    $(function () {
        'use strict';

        $('#fileupload').fileupload({
            dataType: 'json',
            autoUpload: false,
            acceptFileTypes: /(\.|\/)(gif|jpe?g|png|js|html|css|pdf|py)$/i,
            maxFileSize: 20000000, // 20 MB
            // Enable image resizing, except for Android and Opera,
            // which actually support image resizing, but fail to
            // send Blob objects via XHR requests:
            disableImageResize: /Android(?!.*Chrome)|Opera/
                .test(window.navigator.userAgent),
            previewMaxWidth: 100,
            previewMaxHeight: 100,
            previewCrop: true
        }).on('fileuploadadd', function (e, data) {
            fileData.push(data.files[0]);
            console.log(data);
            console.log(fileData);
            data.context = $('<div/>').appendTo('#files');
            $.each(data.files, function (index, file) {
                var node = $('<p/>')
                        .append($('<span/>').text(file.name));
                node.appendTo(data.context);
            });
        }).on('fileuploadprocessalways', function (e, data) {
            var index = data.index,
                file = data.files[index],
                node = $(data.context.children()[index]);
            if (file.preview) {
                node
                    .prepend('<br>')
                    .prepend(file.preview);
            }
            if (file.error) {
                node
                    .append('<br>')
                    .append($('<span class="text-danger"/>').text(file.error));
            }
            if (index + 1 === data.files.length) {
                data.context.find('button')
                    .text('Upload')
                    .prop('disabled', !!data.files.error);
            }
        }).on('fileuploadprogressall', function (e, data) {
            var progress = parseInt(data.loaded / data.total * 100, 10);
            $('#progress .progress-bar').css(
                'width',
                progress + '%'
            );
        }).on('fileuploaddone', function (e, data) {
            $.each(data.result.files, function (index, file) {
                if (file.url) {
                    var link = $('<a>')
                        .attr('target', '_blank')
                        .prop('href', file.url);
                    $(data.context.children()[index])
                        .wrap(link);
                } else if (file.error) {
                    var error = $('<span class="text-danger"/>').text(file.error);
                    $(data.context.children()[index])
                        .append('<br>')
                        .append(error);
                }
            });
        }).on('fileuploadfail', function (e, data) {
            $.each(data.files, function (index) {
                var error = $('<span class="text-danger"/>').text('File upload failed.');
                $(data.context.children()[index])
                    .append('<br>')
                    .append(error);
            });
        }).prop('disabled', !$.support.fileInput)
            .parent().addClass($.support.fileInput ? undefined : 'disabled');
    });

});

//TEST
//$(document).ready(function(){
//    var weekNumber;
//    var day;
//    var slideSet;
//    var slideNumber;
//    var slideHeader;
//    var url;
//    var headerHtml;
//
//    //cancel form
//    $('#btn1').click(function () {
//        $('#resources1').show();
//        $('#comments1').show();
//    });
//
//    $('#comments1').hide();
//    $('#btn2').click(function () {
//        review_url(location.pathname);
//        getHeader();
//        $.ajax({
//            url: '/create_comment/' + weekNumber + '/'
//                + day + '/' + slideSet + '/'
//                + slideNumber + '/' + slideHeader
//                + '/' + url + '/',
//            type: 'GET',
//            success: function(response) {
//                console.log('success');
//                $('#resources1').hide();
//                $('#comments1').html(response).show();
////                $('#comments1').html(response);
//            },
//            error: function(response) {
//                console.log(response.body);
//            }
//        });
//
//    });
//
//   $('#save').on('click', function(){
//       $.ajax({
//            url: '/create_comment/' + weekNumber + '/'
//                + day + '/' + slideSet + '/'
//                + slideNumber + '/' + slideHeader
//                + '/' + url + '/',
//            type: 'POST',
//            dataType: 'json',
//            data: $(this).serialize(), //what should be serialized here?
//            success: function(response) {
//                console.log('success');
//                $('#resources1').hide();
//                $('#comments1').show();
//            },
//            error: function(response) {
//                console.log(response.body);
//            }
//        });
//   });
//    var review_url = function(path){
//       //figure out regex
//        url = path;
//        weekNumber = parseInt(path.split('/')[3]);
//        day = path.split('/')[4]; //string
//        slideSet= parseInt(path.split('/')[6]);
//        slideNumber = parseInt(path.split('/')[7]);
//    };
//
//    var getHeader = function(){
//        headerHtml = $('.present').find('h2');
//        slideHeader = headerHtml[0].firstChild.nodeValue;
//    };
//
//});