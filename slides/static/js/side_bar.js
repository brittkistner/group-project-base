$(document).ready(function(){

    function makeSlideCall() {
       var currentSlideInfo = review_url(document.URL);
        $.ajax({
            url: '/get_slides/' + currentSlideInfo.weekNumber + '/' + currentSlideInfo.day + '/' + currentSlideInfo.slideSet,
            type: 'GET',
            success: function (data) {
                var slide = data;
                console.log(slide);
                count = 0;
                // Get the current day and slide set from the window and expand the appropriate accordion
                slide.forEach(function(slideObj) {
                    var slideInWindow = String(currentSlideInfo.day) + " - " + String(currentSlideInfo.slideSet);

                    if (count === 0) {
                        $('dt:contains(' + slideInWindow + ')').trigger('click');
                        count++;
                    }

                    // If we're in the wrong week, just get outta there
                });

            },
            error: function (response) {

            }
        });
    }

    function fillComments(){
        $.ajax({
            url: ''
        })
    }

    $(document).keydown(function (keyNumber) {
        var key = keyNumber.which;
        if( key === 39 || key === 38 ||  key === 37 || key === 40) {
            makeSlideCall();
        }
    });

    function review_url(url){
       //figure out regex
        var splitURL = {};
        splitURL.weekNumber = parseInt(url.split('/')[3].slice(-1));
        splitURL.day = url.split('/')[4]; //string
        splitURL.slideSet= parseInt(url.split('/')[6]);
        splitURL.slideNumber = parseInt(url.split('/')[7]);

        return splitURL;
    }


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

