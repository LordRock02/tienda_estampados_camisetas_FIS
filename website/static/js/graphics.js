$(document).ready(function(){

    let products = []
    /*
        get all the tshirts from the database
    */
    function getTshirts(){
        fetch('/get_tshirts', {method:'POST'})
        .then(response => response.json())
        .then(data => {
            products = data
        })
    }
    getTshirts()
    /*
        get shoppingList from backend
    */
    let shoppingList = {}
    loadShoppingList()
    function loadShoppingList(){
        shoppingList = {}
        fetch('/load_shopping_cart', {method:'POST'})
        .then(response => response.json())
        .then(data => {
            $.each(data, function(key, value){
                shoppingList[key] = value
            })
        })
        console.log('loadShoppingList:',shoppingList)
    }
    /*
        add products to the cart
    */
    function addTocart(key){
        if(shoppingList[key] == null){
            shoppingList[key] = products[key]
            shoppingList[key].quantity = 1;
            console.log('se agrego', shoppingList[key].id)
        }else{
            shoppingList[key].quantity += 1;
        }
        reloadCart()
    }
    function reloadCart(){
        console.log('reloadCart', shoppingList)
        let count = 0
        let totalPrice = 0
        $('.listCard').empty()
        $.each(shoppingList, function(key, value){
            totalPrice += value.quantity*value.price
            count += value.quantity
            if(value != null){
               let newDiv = $('<li>')
               newDiv.html('<div><img src="static/img/CamisasHome/'+ value.image+ '" class="shoppingCard img-fluid"/></div>'+
                '<div>' + value.name + '</div>' +
                '<div>' + value.price + '</div>' +
                '<div>' + 
                '<button onclick="changeQuantity(${' + key + '}, ${' + (value.quantity -1) + '})">+</button>' +
                    '<div class="ml-2 mr-2">' + value.quantity + '</div>' +
                    '<button onclick="changeQuantity(${' + key + '}, ${' + (value.quantity +1) + '})">+</button>' + 
                '</div>' +
                '<div style="margin-bottom: 24px;"></div>') 
               $('.listCard').append(newDiv)
            }
        })
        console.log('Valor total:',totalPrice, 'cantidad:', count)
        $('.total').text(totalPrice)
    }
    function changeQuantity(key, quantity){
        console.log('hello from changequantity')
        if(quantity == 0){
            delete shoppingList[key]
        }else{
            shoppingList[key].quantity = quantity;
            shoppingList[key].price = quantity*products[key]
        }
    }
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
    $('#closeShoppingCart').click(function(){
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

    $('.product').click(function(){
        /*$.each(products, function(index, product){
            console.log('id:', product.id)
            console.log('name:', product.name)
            console.log('image:', product.image)
            console.log('price:', product.price)
            console.log('size:', product.size)
        })*/
        $.ajax({
            type: 'POST',
            url: "/add_to_cart",
            data: {"id" : $(this).attr('value')}
        })
        console.log($(this).attr('value')) 
        var ids = []
        $.each(products, function(index, product){
            ids.push(product.id)
        })
        addTocart(ids.indexOf(parseInt($(this).attr('value'))))
    })

});