$(document).ready(function(){
    var new_comment = {};
    var weekNumber;
    var day;
    var slideSet;
    var slideNumber;
    var fileUploads;


    var url = '/image/upload/';
        $('#fileupload').fileupload({
            url: url,
            dataType: 'json',
            done: function (e, data) {
                $.each(data.result.files, function (index, file) {
                    $('<p/>').text(file.name).appendTo('#files');
                    $('<p/>').html("<img src='" + file.url + "' width=160px/>").appendTo('#files');
                });
            }
        });




//  //ADD COMMENT
//    //ajax call which renders a django comment form with fields text and attachment
//    $("#add_comment").on("click", function(){
//       $.ajax({
//            url: '',
//            type: 'GET',
//            success: function(response) {
//                //render the django comment form, will this go through the create_comment view?
//            },
//            error: function(response) {
//                console.log(response.body);
//            }
//        });
//    });
//
//    $("#fileupload").fileupload({
////       url: url,
////       dataType: 'json',
////       done: function (e, data)
//        //return
//    });
//  // CREATE COMMENT
//    $("#comment_form_submit").on("submit", function(){
//        //figure out regex
//        weekNumber = parseInt(location.pathname.split('/')[3]);
//        day = location.pathname.split('/')[4]; //string
//        slideSet= parseInt(location.pathname.split('/')[6]);
//        slideNumber = parseInt(location.pathname.split('/')[7]);
////        var url = (location.pathname)
////        var myRegexp;  //come up with this
////        var match = myRegexp.exec(myRegexp);
////        weekNumber = parseInt(match[1])
////        day = match
//
//
//        //return fileupload here
//
//        $.ajax({
//            url: '/create_comment/week' + weekNumber + '/' + day + '/' + slideSet + '/' + slideNumber + '/',
//            type: 'POST',
//            dataType: 'json',
//            data: $(this).serialize(),
//            // will the data look like this? data = { 'commentText': 'text field', 'attachments' : [] }
//            success: function(response) {
//                console.log(JSON.stringify(response));
//            },
//            error: function(response) {
//                console.log(response.body);
//            }
//        });
//    });
});

