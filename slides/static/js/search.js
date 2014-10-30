/**
 * Created by GKadillak on 10/27/14.
 */

//$(document).ready(function () {
//
//    // Hide weekly slides, insert search box
//    $('#search').click(function () {
//       var $allweeks = $('#all-weeks');
//        $('.accordion').slideUp('step');
//        $allweeks.children(':last').slideToggle();
//        $allweeks.append('<input type="search" id="search-box" placeholder="Search">');
//    });
//
//    $('#search-box').click(function() {
//       var $allweeks = $('#all-weeks');
//
//        $allweeks.append('<')
//    });
//
//    // Remove items not clicked on, put clicked title on line and show the accordion elements below
//    $('dt').click(function () {
//        var $all_weeks = $('#all-weeks');
//        var $this = $(this);
//
//        $all_weeks.children().hide();
//        $all_weeks.append('<h2 id="front-search">' + $this.text() + '</h2>');
//        $('.accordion').children().hide();
//        $('.reveal ul').css({
//            'list-style-type': 'none',
//            'margin-left': '-2%'
//        });
//    });
//
//});

$(document).ready(function () {
    $('#all-weeks-copy').hide();
    $('#search').click(function () {
        $('#all-weeks').hide();
        $('#all-weeks-copy').show();
    });

});

$(document).ready(function () {
    $('#search2').click(function () {
        $('#all-weeks-copy').hide();
        $('#all-weeks').show();
    });
});

$(document).ready(function () {
    $('#resource-section').hide();
    $('#slides-section').hide();
    $('#search').click(function () {
        $('#index-section').hide();
        $('#resource-section').show();
        $('#slides-btn').click(function () {
            $('#resource-section').hide();
            $('#slides-section').show();
            $('#resource-btn').click(function () {
                $('#slides-section').hide();
                $('#resource-section').show();
                $('#search2').click(function () {
                    $('#slides-section').hide();
                    $('#resource-section').hide();
                    $('#index-section').show();


                });

            });
        });
    });
});