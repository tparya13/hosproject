$(document).ready(function () {
    $('.deparw').slick({
        lazyLoad: 'ondemand',
        slidesToShow: 5,
        slidesToScroll: 4,
        autoplay: true,
        autoplaySpeed: 4000,

        infinite: true,
        arrows: false,
        responsive: [{
            breakpoint: 1280,
            settings: {
                arrows: false,
                slidesToShow: 3,
                slidesToScroll: 2,
            }
        },
        {
            breakpoint: 770,
            settings: {
                arrows: false,
                slidesToShow: 2,
                slidesToScroll: 1,
            }
        },
        {
            breakpoint: 520,
            settings: {
                slidesToShow: 2,
                slidesToScroll: 1,
                centerPadding: '0px',

            }
        }
        ]
    });
});
$(document).ready(function () {
    $('.gmrw').slick({
        lazyLoad: 'ondemand',
        slidesToShow: 3,
        slidesToScroll: 2,
        autoplay: true,
        autoplaySpeed: 4000,

        infinite: true,
        arrows: false,
        responsive: [{
            breakpoint: 1280,
            settings: {
                arrows: false,
                slidesToShow: 3,
                slidesToScroll: 2,
            }
        },
        {
            breakpoint: 770,
            settings: {
                arrows: false,
                slidesToShow: 2,
                slidesToScroll: 1,
            }
        },
        {
            breakpoint: 520,
            settings: {
                slidesToShow: 2,
                slidesToScroll: 1,
                centerPadding: '0px',

            }
        }
        ]
    });
});
$(document).ready(function () {
    $('.tesrw').slick({
        lazyLoad: 'ondemand',
        slidesToShow: 3,
        slidesToScroll: 2,
        autoplay: true,
        autoplaySpeed: 4000,

        infinite: true,
        arrows: false,
        responsive: [{
            breakpoint: 1280,
            settings: {
                arrows: false,
                slidesToShow: 3,
                slidesToScroll: 2,
            }
        },
        {
            breakpoint: 770,
            settings: {
                arrows: false,
                slidesToShow: 2,
                slidesToScroll: 1,
            }
        },
        {
            breakpoint: 520,
            settings: {
                slidesToShow: 2,
                slidesToScroll: 1,
                centerPadding: '0px',

            }
        }
        ]
    });
});