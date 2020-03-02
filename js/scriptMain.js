
var redirectIndex = 0;
glanceProductData = shooppableItems;
var swiper2 = new Swiper('.swiper-container2', {
    navigation: {
        nextEl: '.swiper-button-next',
        prevEl: '.swiper-button-prev',
    },
    effect: 'coverflow',
    grabCursor: true,
    centeredSlides: true,
    slidesPerView: 3,
    centeredSlides: true,
    uniqueNavElements: true,
    wrapperClass: "swiper-wrapper2",
    coverflowEffect: {
        rotate: 0,
        stretch: 0,
        depth: 100,
        modifier: 1,
        slideShadows: false,
    },
    loop: false
});
if (sessionStorage.getItem('subProductIndex') != undefined) {
    var subProductIndex = parseInt(sessionStorage.getItem('subProductIndex'));
    $('.slideItemBtn').attr('data-attribute', glanceProductData[subProductIndex].viewproductUrl);
    document.getElementById("dotid"+subProductIndex).className = "dot active";
    $('.slideItemTitle').fadeOut(100, function () {
        $(this).text(glanceProductData[subProductIndex].name).fadeIn(100);
    });
    $('.slideItemTitleDesc').fadeOut(100, function () {
        $(this).text(glanceProductData[subProductIndex].price).fadeIn(100);
    });
    swiper2.slideTo(subProductIndex, 50);
    sessionStorage.removeItem('productIndex');
    sessionStorage.removeItem('subProductIndex');
}
else {
    document.getElementById("dotid0").className = "dot active";
}
swiper2.on('slideChange', function (event) {
    const indexofprd = $(this)[0].activeIndex;
    document.getElementById("dotid"+indexofprd).className = "dot active";
    const prevIndex = $(this)[0].previousIndex;
    document.getElementById("dotid"+prevIndex).className = "dot";
    const merchantName =  glanceProductData[indexofprd].merchantName;
    const viewProductUrl =  glanceProductData[indexofprd].viewproductUrl;
    console.log("Data >>>", merchantName, 'View', viewProductUrl);

    gaanalytics('send', 'event', merchantName, 'View', viewProductUrl);

    $('.slideItemBtn').attr('data-attribute', glanceProductData[indexofprd].viewproductUrl)
    $('.slideItemTitle').fadeOut(100, function () {
        $(this).text(glanceProductData[indexofprd].name).fadeIn(100);
    });
    $('.slideItemTitleDesc').fadeOut(100, function () {
        $(this).text(glanceProductData[indexofprd].price).fadeIn(100);
    });

});
var galleryTop = new Swiper('.gallery-top', {
    spaceBetween: 0,
});

galleryTop.detachEvents();
$('.swiper-wrapper2 img').on({
    click: function (event) {
        if (swiper2.activeIndex == swiper2.clickedIndex) {
            $('#loadergop, .slideItemBtn').toggle();
            const merchantName =  glanceProductData[swiper2.clickedIndex].merchantName;
            const viewProductUrl =  glanceProductData[swiper2.clickedIndex].viewproductUrl;
            console.log("Data >>>", merchantName, 'Click', viewProductUrl);

            gaanalytics('send', 'event', merchantName, 'Click', viewProductUrl);

            sessionStorage.setItem('productIndex', galleryTop.activeIndex);
            sessionStorage.setItem('subProductIndex', swiper2.activeIndex);
            const reDirectUrl1 = $('.slideItemBtn').attr('data-attribute');
            $('#loadergop, .slideItemBtn').toggle();
          try {
        if (GlanceAndroidInterface) {
        GlanceAndroidInterface.userEngaged();
        const glanceBingeUrl = 'glance://binge?url='+encodeURIComponent(reDirectUrl1);
        if (AndroidUtils.isKeyguardLocked())
        {       document.querySelector('.over-text').innerText = 'Taking you to the lock screen...';
                document.querySelector('.overlay').style.display = 'block';
                document.querySelector('.loader1').style.display = 'block';
                setTimeout(() => {
                    document.querySelector('.overlay').style.display = 'none';
                    GlanceAndroidInterface.launchIntentAfterUnlock(null,glanceBingeUrl);
                }, 1000);
        }
        else
        GlanceAndroidInterface.launchIntent(null,reDirectUrl1);
    }
     else {
         var reDirectUrl2 = reDirectUrl1.replace("glance","");
         window.location.href = reDirectUrl2;
    }
    } catch {
         var reDirectUrl2 = reDirectUrl1.replace("glance","");
         window.location.href = reDirectUrl2;
        }
        }
        else {
            swiper2.slideTo(swiper2.clickedIndex, 500);
        }
    }
});

var redirectUrl = () => {
    $('#loadergop, .slideItemBtn').toggle();
    const merchantName =  glanceProductData[swiper2.activeIndex].merchantName;
    const viewProductUrl =  glanceProductData[swiper2.activeIndex].viewproductUrl;
    console.log("Data >>>", merchantName, 'Click', viewProductUrl);

    gaanalytics('send', 'event', merchantName, 'Click', viewProductUrl);

    sessionStorage.setItem('productIndex', galleryTop.activeIndex);
    sessionStorage.setItem('subProductIndex', swiper2.activeIndex);
    const reDirectUrl = $('.slideItemBtn').attr('data-attribute');
    $('#loadergop, .slideItemBtn').toggle();
try {
        if (GlanceAndroidInterface) {
        GlanceAndroidInterface.userEngaged();
        const glanceBingeUrl = 'glance://binge?url='+encodeURIComponent(reDirectUrl);
        if (AndroidUtils.isKeyguardLocked())
            {   document.querySelector('.over-text').innerText = 'Taking you to the lock screen...';
                document.querySelector('.overlay').style.display = 'block';
                document.querySelector('.loader1').style.display = 'block';
                setTimeout(() => {
                    document.querySelector('.overlay').style.display = 'none';
                    GlanceAndroidInterface.launchIntentAfterUnlock(null,glanceBingeUrl);
                }, 1000);
            }
       // 
        else
        GlanceAndroidInterface.launchIntent(null,reDirectUrl);
    }
     else {
      var reDirectUrl2 = reDirectUrl.replace("glance","");
         window.location.href = reDirectUrl2;
    }
    } catch {    
         var reDirectUrl2 = reDirectUrl.replace("glance","");
         window.location.href = reDirectUrl2;  
    }
}
