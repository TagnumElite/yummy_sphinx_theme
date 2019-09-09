// Window Scroll
var windowScroll = function () {
    $(window).scroll(function () {

        var scrollPos = $(this).scrollTop();

        var system ={win : false,mac : false,xll : false};
        //检测平台
        var p = navigator.platform;
        system.win = p.indexOf("Win") == 0;
        system.mac = p.indexOf("Mac") == 0;
        system.x11 = (p == "X11") || (p.indexOf("Linux") == 0);
        //判断平台类型
        if(system.win||system.mac||system.xll){
            if ($(window).scrollTop() > 70)
            {
                $('.site-header').addClass('site-header-nav-scrolled');
            } else {
                $('.site-header').removeClass('site-header-nav-scrolled');
            }
        }else{
            //如果是手机则将顶栏移除界面
            if ($(window).scrollTop() > 40)
            {
                $('.site-header').addClass('site-header-nav-scrolled-ph');
            } else {
                $('.site-header').removeClass('site-header-nav-scrolled-ph');
            }
        }
 });
};

$( document ).ready(function() {
    windowScroll();
});

var fixmeTop = $('#toc').offset().top - 100;

$(window).scroll(function() {                  // assign scroll event listener
            var currentScroll = $(window).scrollTop(); // get current position
            if (currentScroll >= fixmeTop) {           // apply position: fixed if you
                $('#toc').css({      // scroll to that element or below it
                    top: '100px',
                    position: 'fixed'
                });
            } else {                                   // apply position: static
                $('#toc').css({      // if you scroll above it
                    position: 'inherit'
                });
            }
        });