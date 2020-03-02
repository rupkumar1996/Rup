// BackGroundPage Content
$('.gallery-top .swiper-slide').css('background','linear-gradient(to bottom, rgba(0,0,0,0.65) 0%,rgba(0,0,0,0) 25%,rgba(0,0,0,0) 40%,rgba(0,0,0,0) 58%,rgba(0,0,0,0.37) 82%,rgba(0,0,0,0.63) 99%,rgba(0,0,0,0.65) 100%),url('+backgroundImg.imageUrl+')');
$('.slideItemTitle').text(shooppableItems[0].name);
$('.slideItemTitleDesc').text(shooppableItems[0].price);
$('.slideItemBtn').attr('data-attribute', shooppableItems[0].viewproductUrl);
// Shopping Page
for(var inst = 0; inst < shooppableItems.length ;inst++){
    $('#secondSwipper').append('<div class="swiper-slide"><div class="slideItemCont"><img src="'+shooppableItems[inst].image+'" class="slideImg" alt=""></div></div>');
    $('#dots').append('<span id="dotid'+inst+'" class="dot"></span>'+'\n');
}
