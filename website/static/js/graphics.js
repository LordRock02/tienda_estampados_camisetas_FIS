$(document).ready(function(){
    /*
        categories interaction
    */
    $('.category-btn').click(function(){
        if($(this).find('input').attr('value')==''){
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

    var width = $('.shoppingCard').clientWidth;
    var height = $('.shoppingCard').clientHeight;
    var ratio = width/height;

    $('.shoppingCard').css('object-fit','contain');

    /*
        shopping cart interaction
    */

    $('#cartBtn').click(function(){
        reloadCart()
        $('body').addClass('active')
    })
    $('.closeShoppingCart').click(function(){
        $('body').removeClass('active')
    })
    $('#buyBtn').click(function(){
        alert('se presiono checkout')
        $.ajax({
            type: 'GET',
            url: "/calcular_total"
        })
    })
    
    /*
        add products to the shopping cart
    */

    $('.addProduct').click(function(){
        addTshirt($(this).attr('value'))
    })
});
function reloadCart(){
    $(document).ready(function(){
        var shoppingList = {}
        fetch('/load_shopping_cart', {method:'POST'})
        .then(response => response.json())
        .then(data => {
            $.each(data, function(key, value){
                shoppingList[key] = value
            })
            let count = 0
            let totalPrice = 0
            $('.listCard').empty()
            $.each(shoppingList, function(key, value){
                console.log('hola')
                totalPrice += value.quantity*value.price
                count += value.quantity
                if(value != null){
                   let newDiv = $('<li>')
                   newDiv.html('<div><img src="static/img/CamisasHome/'+ value.image+ '" class="shoppingCard img-fluid"/></div>'+
                    '<div>' + value.name + '</div>' +
                    '<div>' + value.price + '</div>' +
                    '<div>' + 
                        '<button class="btn" id="minusBtn" onclick="removeTshirt(' + value.id + ')">-</button>' +
                        '<div class="mx-3">' + value.quantity + '</div>' +
                        '<button class="btn" id="plusBtn" onclick="addTshirt(' + value.id + ')">+</button>' + 
                    '</div>' +
                    '<div style="margin-bottom: 24px;"></div>') 
                   $('.listCard').append(newDiv)
                }
            })
            console.log('Valor total:',totalPrice, 'cantidad:', count)
            $('.total').text(totalPrice)
        })
    })
}

function addTshirt(id){
    $(document).ready(function(){
        $.ajax({
            type: 'POST',
            url: "/add_to_cart", 
            data: {'id' : id},
            success: function(data){
                reloadCart()
            },
            error: function(error) {
                // Código que se ejecuta en caso de error de la solicitud AJAX
                console.error('Error en la solicitud AJAX:', error);
            },
            complete: function() {
                // Código que se ejecuta después de que la solicitud AJAX esté completa
                // Esto se ejecutará incluso en caso de error
            }
        })
    })
}

function removeTshirt(id){
    $(document).ready(function(){
        $.ajax({
            type: 'POST',
            url: "/remove", 
            data: {'id' : id},
            success: function(data){
                reloadCart()
            },
            error: function(error) {
                // Código que se ejecuta en caso de error de la solicitud AJAX
                console.error('Error en la solicitud AJAX:', error);
            },
            complete: function() {
                // Código que se ejecuta después de que la solicitud AJAX esté completa
                // Esto se ejecutará incluso en caso de error
            }
        })
    })
}