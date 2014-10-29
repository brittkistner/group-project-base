$(document).ready(function () {

    $.ajax({
        type: 'GET',
        dataType: "jsonp",
        url: "http://ec2-54-191-44-247.us-west-2.compute.amazonaws.com/week1/1/",

        success: function (data) {
            // var i = 1;
            console.log(data);
        },
        error: function (data) {
            {
                console.log('error');
                console.log(data);

            }
        }
    });

});

