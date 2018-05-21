$(function () {

    var versionsBar = $('.js-versions-bar');
    var footer = $('.Footer');
    var header = $('.Header');

    var menuContainerElement = $('.js-menu-container');
    var menuElement = $('.js-menu');
    var menuInnerElement = $('.js-menu-inner');

    $(window).on('load resize scroll', function (e) {

        // menu is positioned "fixed" for bigger screens only
        if (window.innerWidth > 992) {
            var versionsBarHeight = versionsBar.outerHeight() || 0;

            var headerVisibleAmount = Math.max(0, header.outerHeight() - window.pageYOffset);

            var footerVisibleAmount = $(window).scrollTop() + $(window).height() - ($(document).height() - footer.outerHeight());
            var footerOffset = Math.max(0, footerVisibleAmount);

            // menu height è il valore minimo tra:
            // - lo spazio disponibile senza header, versionsBar e footer
            // - l'altezza di menuContainerElement (necessario quando lo schermo è molto grande e il footer è sopra la baseline del viewport)
            var menuHeight = Math.min(menuContainerElement.height(), window.innerHeight - headerVisibleAmount - versionsBarHeight - footerOffset);

            menuElement.css({
                top: Math.floor(headerVisibleAmount) + 'px',
                height: Math.floor(menuHeight) + 'px'
            });

            versionsBar.toggleClass('u-fixedBottom', footerVisibleAmount < 0);
            versionsBar.toggleClass('u-posAbsolute', footerVisibleAmount > 0);

            if (e.type === "load") {

                // riposizionamento menu selezionato
                var currentElement = $('.toctree-l1.current');
                if (currentElement.length) {
                    menuInnerElement.animate({
                        scrollTop: currentElement.offset().top - menuInnerElement.offset().top
                    });
                }
            }
        } else {
            menuElement.css({
                top: 'auto',
                height: 'auto'
            });
        }
    });

    $('.version-list').on('change', function (e) {
        window.location = $(this).val();
    });

    $('.js-preventOffCanvasClose').on('click', function (e) {
        e.preventDefault();
        e.stopPropagation();
    });

});