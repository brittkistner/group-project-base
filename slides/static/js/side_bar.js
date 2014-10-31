$(document).ready(function(){


    function makeSlideCall() {
       var currentSlideInfo = review_url(window.location.href);
        console.log('a slide call has been made');
        $.ajax({
            url: '/get_slides/' + currentSlideInfo.weekNumber + '/' + currentSlideInfo.day,
            type: 'GET',
            success: function (data) {
                var slides = data;

                // Get the current day and slide set from the window and expand the appropriate accordion
                slides.forEach(function(slide) {
                        $('.accordion').append(
                            '<dt>'+ slide.fields.slide_set + ' ' + slide.fields.slide_header + '</dt>' +
                                '<dd>' +
                                    '<ul>' +
                                    '</ul>' +
                                '</dd>' +
                        '<hr>');

                    console.log(slide);
            });

            },
            error: function (response) {
                console.log(response);
            }
        });
    }

    // Get the slides once
    makeSlideCall();

    function fillComments(){
        var currentSlideInfo = review_url(window.location.href);
        console.log(window.location.href);
        if (isNaN(currentSlideInfo.slideNumber) === false) {
            console.log('The slide number is being pulled');    
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
            $.ajax({
                url: '/front_comment/' + currentSlideInfo.weekNumber + '/' + currentSlideInfo.day + '/' + currentSlideInfo.slideSet,
                type: 'GET',
                success: function (response) {
                    console.log(response);
                    var comments = response;

                    if ($('dt:contains(' + response[0].fields.day + ')').find('div').length === 0) {
                    comments.forEach(function (comment){
                        var $dt = $('dt:contains(' + comment.fields.slide_set + ')');
                        $dt.append(
                                '<div id=comment>' + comment.fields.text + '</div>'
                        );
                      });
                    }
                }

            });
        }
    }

    // When the directional arrows are pressed, get the slide titles and their comments
    $(document).keydown(function (keyNumber) {
        var key = keyNumber.which;
        if( key === 39 || key === 38 ||  key === 37 || key === 40) {
            setTimeout(fillComments(), 1000);
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

