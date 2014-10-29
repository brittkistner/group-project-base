/**
 * Created by GKadillak on 10/27/14.
 */

$(document).ready(function () {

    // Hide weekly slides, insert search box
    $('#search').click(function () {
       var $allweeks = $('#all-weeks');
        $('.accordion').slideUp('step');
        $allweeks.children(':last').slideToggle();
        $allweeks.append('<input type="search" id="search-box" placeholder="Enter search term here">');
    });

    $('#search-box').click(function() {
       var $allweeks = $('#all-weeks');

        $allweeks.append('<')
    });

    // Remove items not clicked on, put clicked title on line and show the accordion elements below
    $('dt').click(function () {
        var $all_weeks = $('#all-weeks');
        var $this = $(this);

        $all_weeks.children().hide();
        $all_weeks.append('<h2 id="front-search">' + $this.text() + '</h2>');
        $('.accordion').children().hide();
        $('.reveal ul').css({
            'list-style-type': 'none',
            'margin-left': '-2%'
        });
    });





});
