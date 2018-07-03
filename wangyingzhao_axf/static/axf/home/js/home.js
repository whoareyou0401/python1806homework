$(function () {
    initTopSwiper();
    initMustSwiper()
})

function initTopSwiper() {
    var mySwiper = new Swiper('#topSwiper', {
        // direction: 'vertical',
        loop: true,
        autoplay: 2000,
        // effect : "flip",

        // 如果需要分页器
        pagination: '.swiper-pagination',

        // 如果需要前进后退按钮
        nextButton: '.swiper-button-next',
        prevButton: '.swiper-button-prev',

        // 如果需要滚动条
        // scrollbar: '.swiper-scrollbar',
    })
}


function initMustSwiper() {
    var mySwiper = new Swiper('#swiperMenu', {
        // direction: 'vertical',
        // loop: true,
        slidesPerView: 3
        // autoplay: 2000,
        // effect : "flip",

        // 如果需要分页器
        // pagination: '.swiper-pagination',

        // 如果需要前进后退按钮
        // nextButton: '.swiper-button-next',
        // prevButton: '.swiper-button-prev',

        // 如果需要滚动条
        // scrollbar: '.swiper-scrollbar',
    })
}