$(document).ready(function(){

    function makeSlideCall() {
       var currentSlideInfo = review_url(document.URL);
        $.ajax({
            url: '/get_slides/' + currentSlideInfo.weekNumber + '/' + currentSlideInfo.day + '/' + currentSlideInfo.slideSet,
            type: 'GET',
            success: function (data) {
                var slide = data;
                fillComments();
                console.log('fill comments worked!');
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
        var currentSlideInfo = review_url(document.URL);
        $.ajax({
            url: '/get_comments/' + currentSlideInfo.day + '/' + currentSlideInfo.slideSet,
            type: 'GET',
            success: function(response) {
                console.log(response);

            }

        });
    }
    fillComments();

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
    var weekNumber;
    var day;



//on page load
    $("#resources").on("click", function(){ //change
       review_url(location.pathname);
       $.ajax({
            url: '/get_slides/' + weekNumber + '/' + day + '/',
            type: 'GET',
            success: function(response) {
                $('#resources').html(response); //change
            },
            error: function(response) {
                console.log(response.body);
            }
        });
    });


});

