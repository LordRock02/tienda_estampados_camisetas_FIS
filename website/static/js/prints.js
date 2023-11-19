$(document).ready(function(){
    var width = $('.card-img-top').clientWidth;
    var height = $('.card-img-top').clientHeight;
    var ratio = width/height;
    if(width>height){
        $('.card-img-top').width(300);
        $('.card-img-top').height(300/ratio);
    }else{
        $('.card-img-top').height(300);
        $('.card-img-top').width(300*ratio);
    }
});