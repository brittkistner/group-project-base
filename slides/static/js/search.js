/**
 * Created by GKadillak on 10/27/14.
 */

$(document).ready(function () {
   $('#search').click(function () {
        $('.accordion').slideUp('step');
        $('#all-weeks').children(':last').slideToggle('easing');
        $('#all-weeks').append()
   });
});
