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

    // Remove
    $('dt').click(function () {
        var $all_weeks = $('#all-weeks');
        var $this = $(this);
        $all_weeks.children().hide();
        $all_weeks.append('<h2 id="front-search">' + $this.text() + '</h2>');
        $('.accordion').children().hide();

        // If the order doesn't matter, just append the elements with a map
        $('.reveal ul').css({
            'list-style-type': 'none',
            'margin-left': '-2%'
        });

        // Find the 'li' elements and replace them with paragraphs with text from inside previous tag
//        $this.find('li').replaceWith('<p>' + $(this).find('li').text() + '</p>');
    });
});
