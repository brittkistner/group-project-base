$(document).ready(function(){
//    var new_comment = {};
    var weekNumber;
    var day;
    var slideSet;
    var slideNumber;
//    var fileUploads;


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

    var review_url = function(url){
       //figure out regex
        weekNumber = parseInt(url.split('/')[3]);
        day = url.split('/')[4]; //string
        slideSet= parseInt(url.split('/')[6]);
        slideNumber = parseInt(url.split('/')[7]);
    };

});

