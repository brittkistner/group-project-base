$(document).ready(function () {

    $.ajax({
        type: 'GET',
        dataType: "html",
        url: "http://127.0.0.1:8000/week2/1_am/#/2/1",

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

