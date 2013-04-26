$(function(){
    $('.thumb').click(function(){
        $('.gallery .image img').hide(0);
        $('.gallery .image img[rel='+$(this).attr('rel')+']').show(0);
        return false;
    });

    $('.fancy').fancybox();
});