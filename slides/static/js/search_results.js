$(document).ready(function () {
    //$('#search').dblclick(function () {
       // $('#search').click(function () {
    $(document).keypress(function(e) {
    if(e.which == 13) {
       // alert('You pressed enter!');


            console.log('test');
            var searchtext = $('#search-box').val();

            $.ajax({
                url: '/rusearch/?q=' + searchtext,
                type: 'GET',
                dataType: 'html',
                success: function (data) {
                    console.log(data);
                    $("#resource-section").append(data)
                },
                error: function (data) {
                    console.log('error');
                    console.log(data)


                }

            });

        //});
   // });

         }
});

});
