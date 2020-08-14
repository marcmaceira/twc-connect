$(document).ready(function() {  
    // ============ parallax background scrolling =================
    $window = $(window);
  
    $('[data-type="background"]').each(function() {
        // declare the variable to affect the defined data-type
        var $scroll = $(this);

        $(window).scroll(function() {                             
            var yPos = -(($window.scrollTop() - $scroll.offset().top) / $scroll.data('speed'));

            // background position
            var coords = '50% calc(50% + ' + yPos + 'px)';

            // move the background
            $scroll.css({
            backgroundPosition: coords
            });
        }); // end window scroll
    }); // end section function
});