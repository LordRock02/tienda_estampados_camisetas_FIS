$(document).ready(function(){
    /*
        categories interaction
    */
    $('.category-btn').click(function(){
        if($(this).find('input').attr('value')==''){
            alert('hols')
            $(this).css({
                'background-color': 'rgb(108, 92, 240)',
                'color': 'white'
            });
            $(this).find('i').removeClass('fa fa-plus').addClass('fa fa-remove');
            $(this).find('i').css('color', 'white');
            $(this).find('input').val($(this).attr('id'));            
        }else{
            $(this).css({
                'background-color': 'rgb(230, 230, 230)',
                'color': 'black'
            });
            $(this).find('i').removeClass('fa fa-remove').addClass('fa fa-plus');
            $(this).find('i').css('color', 'gray');
            $(this).find('input').val('');            
        }
    });
    $('#submitBtn').click(function(){
        
    })
    /*
        reescale images
    */
    var width = $('.card-img-top').clientWidth;
    var height = $('.card-img-top').clientHeight;
    var ratio = width/height;
    $('.card-img-top').height(300);
    $('.card-img-top').width(260);
    $('.card-img-top').css('object-fit','contain');

    $('#signInBtn').click(function(){
        alert('boton presionado')
    })

    /*
        shopping cart interaction
    */

    $('#cartBtn').click(function(){
        $('body').addClass('active')
    })
    $('.closeShopping').click(function(){
        $('body').removeClass('active')
    })

    $('.product').click(function(){
        $.ajax({
            type: 'POST',
            url: "/add_to_cart",
            data: {"id" : $(this).attr('value')}
        })
        
    })

});