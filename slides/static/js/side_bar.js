$(document).ready(function(){

    function makeSlideCall() {
       var currentSlideInfo = review_url(document.URL);
        $.ajax({
            url: '/get_slides/' + currentSlideInfo.weekNumber + '/' + currentSlideInfo.day,
            type: 'GET',
            success: function (data) {
                var slides = data;

                // Get the current day and slide set from the window and expand the appropriate accordion
                slides.forEach(function(slide) {
                    $('#comment-block').append('' +
                              '<div id="single-comment">'+
                                    '<dl class="accordion" id="side-comment">' +
                                        '<dt>'+ slide.fields.slide_set + ' ' + slide.fields.slide_header + '</dt>' +
                                            '<dd>' +
                                                '<ul>' +
                                                '</ul>' +
                                            '</dd>' +
                                    '</dl>' +
                                '</div>' +
                                '<hr>');

                $('.accordion').accordion();

                var allPanels = $('.accordion > dd').hide();
                    console.log(slide);
            });

            },
            error: function (response) {

            }
        });
    }

    // Get the slides once
    makeSlideCall();


    function fillComments(){
        var currentSlideInfo = review_url(document.location.href);
        console.log(document.location.href);
        if (isNaN(currentSlideInfo.slideNumber) === false) {

            var slideInWindow = String(currentSlideInfo.day) + " - " + String(currentSlideInfo.slideSet);
            $.ajax({
                url: '/subset_comment/' + currentSlideInfo.weekNumber + '/' + currentSlideInfo.day + '/' +
                    currentSlideInfo.slideSet + '/' + currentSlideInfo.slideNumber,
                type: 'GET',
                success: function (response) {
                    console.log(response);
//                $('dt:contains(' + slideInWindow + ')').append()

                }

            });
        }

        else {
            var slideInWindow = String(currentSlideInfo.day) + " - " + String(currentSlideInfo.slideSet);
            $.ajax({
                url: '/front_comment/' + currentSlideInfo.weekNumber + '/' + currentSlideInfo.day + '/' + currentSlideInfo.slideSet,
                type: 'GET',
                success: function (response) {
                    var comments = response;

                    comments.forEach(function (comment){
//                        $('dt:contains' + currentSlideInfo.'')
                        console.log(comment);
                    });
                }

            });
        }
    }

    // When the directional arrows are pressed, get the slide titles and their comments
    $(document).keydown(function (keyNumber) {
        var key = keyNumber.which;
        if( key === 39 || key === 38 ||  key === 37 || key === 40) {
            fillComments();
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



//on page load
//    $("#resources").on("click", function(){ //change
//       review_url(location.pathname);
//       $.ajax({
//            url: '/get_slides/' + weekNumber + '/' + day + '/',
//            type: 'GET',
//            success: function(response) {
//                $('#resources').html(response); //change
//            },
//            error: function(response) {
//                console.log(response.body);
//            }
//        });
//    });


});

