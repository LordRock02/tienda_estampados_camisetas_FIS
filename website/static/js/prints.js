$(document).ready(function(){
    var width = $('.card-img-top').clientWidth;
    var height = $('.card-img-top').clientHeight;
    var ratio = width/height;
    if(width>height){
        $('.card-img-top').width(150);
        $('.card-img-top').height(150*ratio);
    }else{
        $('.card-img-top').height(150);
        $('.card-img-top').width(150/ratio);
    }
});