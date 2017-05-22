require=(function e(t,n,r){function s(o,u){if(!n[o]){if(!t[o]){var a=typeof require=="function"&&require;if(!u&&a)return a(o,!0);if(i)return i(o,!0);var f=new Error("Cannot find module '"+o+"'");throw f.code="MODULE_NOT_FOUND",f}var l=n[o]={exports:{}};t[o][0].call(l.exports,function(e){var n=t[o][1][e];return s(n?n:e)},l,l.exports,e,t,n,r)}return n[o].exports}var i=typeof require=="function"&&require;for(var o=0;o<r.length;o++)s(r[o]);return s})({1:[function(require,module,exports){
!function(a){function b(){g.hasClass(k)?h.toggleClass(l):h.toggleClass(m),q&&g.one("transitionend",function(){q.focus()})}function c(){g.hasClass(k)?h.removeClass(l):h.removeClass(m)}function d(){g.hasClass(k)?(h.addClass(l),g.animate({left:"0px"},r),i.animate({left:s},r),j.animate({left:s},r)):(h.addClass(m),g.animate({right:"0px"},r),i.animate({right:s},r),j.animate({right:s},r)),q&&q.focus()}function e(){g.hasClass(k)?(h.removeClass(l),g.animate({left:"-"+s},r),i.animate({left:"0px"},r),j.animate({left:"0px"},r)):(h.removeClass(m),g.animate({right:"-"+s},r),i.animate({right:"0px"},r),j.animate({right:"0px"},r))}function f(){a(t).addClass(v),a(t).on("click",function(){var b=a(this);b.hasClass(v)?(a(t).addClass(v).removeClass(u),b.removeClass(v).addClass(u)):b.addClass(v).removeClass(u)})}var g=a(".pushy"),h=a("body"),i=a("#container"),j=a(".push"),k="pushy-left",l="pushy-open-left",m="pushy-open-right",n=a(".site-overlay"),o=a(".menu-btn, .pushy-link"),p=a(".menu-btn"),q=a(g.data("focus")),r=200,s=g.width()+"px",t=".pushy-submenu",u="pushy-submenu-open",v="pushy-submenu-closed";a(t);a(document).keyup(function(a){27==a.keyCode&&(h.hasClass(l)||h.hasClass(m))&&(w?c():(e(),x=!1),p&&p.focus())});var w=function(){var a=document.createElement("p"),b=!1,c={webkitTransform:"-webkit-transform",OTransform:"-o-transform",msTransform:"-ms-transform",MozTransform:"-moz-transform",transform:"transform"};if(null!==document.body){document.body.insertBefore(a,null);for(var d in c)void 0!==a.style[d]&&(a.style[d]="translate3d(1px,1px,1px)",b=window.getComputedStyle(a).getPropertyValue(c[d]));return document.body.removeChild(a),void 0!==b&&b.length>0&&"none"!==b}return!1}();if(w)f(),o.on("click",function(){b()}),n.on("click",function(){b()});else{h.addClass("no-csstransforms3d"),g.hasClass(k)?g.css({left:"-"+s}):g.css({right:"-"+s}),i.css({"overflow-x":"hidden"});var x=!1;f(),o.on("click",function(){x?(e(),x=!1):(d(),x=!0)}),n.on("click",function(){x?(e(),x=!1):(d(),x=!0)})}}(jQuery);
},{}],"sphinx-rtd-theme":[function(require,module,exports){
var jQuery = (typeof(window) != 'undefined') ? window.jQuery : require('jquery');

// Sphinx theme nav state
function ThemeNav () {

    var nav = {
        navBar: null,
        win: null,
        winScroll: false,
        winResize: false,
        linkScroll: false,
        winPosition: 0,
        winHeight: null,
        docHeight: null,
        isRunning: false
    };

    nav.enable = function () {
        var self = this;

        if (!self.isRunning) {
            self.isRunning = true;
            jQuery(function ($) {
                self.init($);

                self.reset();
                self.win.on('hashchange', self.reset);

                // Set scroll monitor
                self.win.on('scroll', function () {
                    if (!self.linkScroll) {
                        self.winScroll = true;
                    }
                });
                setInterval(function () { if (self.winScroll) self.onScroll(); }, 25);

                // Set resize monitor
                self.win.on('resize', function () {
                    self.winResize = true;
                });
                setInterval(function () { if (self.winResize) self.onResize(); }, 25);
                self.onResize();
            });
        };
    };

    nav.init = function ($) {
        var doc = $(document),
            self = this;

        this.navBar = $('div.wy-side-scroll:first');
        this.win = $(window);

        // Set up javascript UX bits
        $(document)
            // Shift nav in mobile when clicking the menu.
            .on('click', "[data-toggle='wy-nav-top']", function() {
                $("[data-toggle='wy-nav-shift']").toggleClass("shift");
                $("[data-toggle='rst-versions']").toggleClass("shift");
                $("#slimheader").toggleClass("shift");
            })

            // Nav menu link click operations
            .on('click', ".wy-menu-vertical .current ul li a", function() {
                var target = $(this);
                // Close menu when you click a link.
                $("[data-toggle='wy-nav-shift']").removeClass("shift");
                $("[data-toggle='rst-versions']").toggleClass("shift");
                // Handle dynamic display of l3 and l4 nav lists
                self.toggleCurrent(target);
                self.hashChange();
            })
            .on('click', "[data-toggle='rst-current-version']", function() {
                $("[data-toggle='rst-versions']").toggleClass("shift-up");
            })

        // Make tables responsive
        $("table.docutils:not(.field-list)")
            .wrap("<div class='wy-table-responsive'></div>");

        // Add expand links to all parents of nested ul
        $('.wy-menu-vertical ul').not('.simple').siblings('a').each(function () {
            var link = $(this);
                expand = $('<span class="toctree-expand"></span>');
            expand.on('click', function (ev) {
                self.toggleCurrent(link);
                ev.stopPropagation();
                return false;
            });
            link.prepend(expand);
        });
    };

    nav.reset = function () {
        // Get anchor from URL and open up nested nav
        var anchor = encodeURI(window.location.hash);
        if (anchor) {
            try {
                var link = $('.wy-menu-vertical')
                    .find('[href="' + anchor + '"]');
                // If we didn't find a link, it may be because we clicked on
                // something that is not in the sidebar (eg: when using
                // sphinxcontrib.httpdomain it generates headerlinks but those
                // aren't picked up and placed in the toctree). So let's find
                // the closest header in the document and try with that one.
                if (link.length === 0) {
                  var doc_link = $('.document a[href="' + anchor + '"]');
                  var closest_section = doc_link.closest('div.section');
                  // Try again with the closest section entry.
                  link = $('.wy-menu-vertical')
                    .find('[href="#' + closest_section.attr("id") + '"]');

                }
                $('.wy-menu-vertical li.toctree-l1 li.current')
                    .removeClass('current');
                link.closest('li.toctree-l2').addClass('current');
                link.closest('li.toctree-l3').addClass('current');
                link.closest('li.toctree-l4').addClass('current');
            }
            catch (err) {
                console.log("Error expanding nav for anchor", err);
            }
        }
    };

    nav.onScroll = function () {
        this.winScroll = false;
        var newWinPosition = this.win.scrollTop(),
            winBottom = newWinPosition + this.winHeight,
            navPosition = this.navBar.scrollTop(),
            newNavPosition = navPosition + (newWinPosition - this.winPosition);
        if (newWinPosition < 0 || winBottom > this.docHeight) {
            return;
        }
        this.navBar.scrollTop(newNavPosition);
        this.winPosition = newWinPosition;
    };

    nav.onResize = function () {
        this.winResize = false;
        this.winHeight = this.win.height();
        this.docHeight = $(document).height();
    };

    nav.hashChange = function () {
        this.linkScroll = true;
        this.win.one('hashchange', function () {
            this.linkScroll = false;
        });
    };

    nav.toggleCurrent = function (elem) {
        var parent_li = elem.closest('li');
        parent_li.siblings('li.current').removeClass('current');
        parent_li.siblings().find('li.current').removeClass('current');
        parent_li.find('> ul li.current').removeClass('current');
        parent_li.toggleClass('current');
    }

    return nav;
};

module.exports.ThemeNav = ThemeNav();

if (typeof(window) != 'undefined') {
    window.SphinxRtdTheme = { StickyNav: module.exports.ThemeNav };
}

},{"jquery":"jquery"}]},{},[1,"sphinx-rtd-theme"]);
