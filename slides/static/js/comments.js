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
    $(function () {
        'use strict';

        $('#fileupload').fileupload({
            dataType: 'json',
            autoUpload: false,
            acceptFileTypes: /(\.|\/)(gif|jpe?g|png)$/i,
            maxFileSize: 5000000, // 5 MB
            // Enable image resizing, except for Android and Opera,
            // which actually support image resizing, but fail to
            // send Blob objects via XHR requests:
            disableImageResize: /Android(?!.*Chrome)|Opera/
                .test(window.navigator.userAgent),
            previewMaxWidth: 100,
            previewMaxHeight: 100,
            previewCrop: true
        }).on('fileuploadadd', function (e, data) {
            console.log("I made it");
            console.log(data.files);
            fileData.push(data.files);
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