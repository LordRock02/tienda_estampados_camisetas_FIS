sizes = {
    '1' : 'small',
    '2' : 'medium',
    '3' : 'large', 
    '4' : 'xlarge'
}
$(document).ready(function(){
    getUser()
    getView()
    loadShoppingList()
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
        btns interaction
    */

    $('#cartBtn').click(function(){
        reloadCart()
        $('body').addClass('active')
    })
    $('.closeShoppingCart').click(function(){
        $('body').removeClass('active')
    })
    $('#buyBtn').click(function(){
        goToPage('/pago')

    })
    $('#goToUploadBtn').click(function(){
        goToPage('/redirect_upload')
    })
    $('.logOutBtn').click(function(){
        alert('Log Out')
    })
    $('#addPrintBtn').click(function(){
        alert($(this).attr('value'))
    })
    /*
        add products to the shopping cart
    */

    $('.addProduct').click(function(){
        //addTshirt($(this).attr('value'))
        redirectTshirtView($(this).attr('value'))
    })
    $('#addToCart').click(function(){
        addToCart($(this).attr('value'),$('#sizeTshirt option:selected').val(),$('#quantityTshirt').val())
    })
    $('.stockBtn').click(function(){
        alert('ver stock')
        redirectTshirtViewAdmin($(this).attr('value'))
    })
    $('.addToStock').click(function(){
        alert('stock')
        addToStock($(this).attr('value'),$('#sizeTshirt option:selected').val(),$('#quantityTshirt').val())

    })
    $('.payBtn').click(function(){
        purchase()
    })
    /*$("option[value='{{ size.id }}']").on("change", function(){
        // llamar a la función addToCart con los argumentos correspondientes
        alert('hola')
        addToCart('{{ tshirt.tshirt_id }}', '{{ size.id }}', this.value);
    });*/
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
            console.log(shoppingList)
            let count = 0
            let totalPrice = 0
            $('.listCard').empty()
            $.each(shoppingList, function(key, value){
                console.log('hola')
                totalPrice += value.quantity*value.price
                count += value.quantity
                if(value != null){
                   let newDiv = $('<li>')
                   newDiv.html('<div><img src="/static/img/CamisasHome/'+ value.image+ '" class="shoppingCard img-fluid"/></div>'+
                    '<div>' + value.name + ' ' + sizes[value.size] + '</div>' +
                    '<div>' + value.price + '</div>' +
                    '<div>' + 
                        '<button class="btn" id="minusBtn" onclick="removeTshirt(' + value.id + ', ' + value.size + ')">-</button>' +
                        '<div class="mx-3">' + value.quantity + '</div>' +
                        '<button class="btn" id="plusBtn" onclick="addToCart(' + value.id + ', ' + value.size +', 1)">+</button>' + 
                    '</div>' +
                    '<div style="margin-bottom: 24px;"></div>') 
                   $('.listCard').append(newDiv)
                }
            })
            console.log('Valor total:',totalPrice, 'cantidad:', count)
            $('.total').text(totalPrice)
            if(Object.keys(shoppingList).length>0){
                $('#quantityCircle').text(Object.keys(shoppingList).length)
            }
        })
    })
    loadShoppingList()
}

function loadShoppingList(){
    console.log('hello from loadShoppingList')
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
            $('.listCardPago').empty()
            $.each(shoppingList, function(key, value){
                console.log('hola')
                totalPrice += value.quantity*value.price
                count += value.quantity
                if(value != null){
                   let newDiv = $('<li>')
                   newDiv.html('<div class="d-flex justify-content-between align-items-center mb-2">'+
                        '<div class="d-flex" style="display: inline-block;">' +
                            '<div>' +
                            '<img src="/static/img/CamisasHome/' + value.image + '" alt="Producto 1" class="mr-2" style="width: 10%;">' +
                            '<span class="position-relative top-50 translate-middle badge bg-primary" id="quantityCircle">' + value.quantity + '</span>' +
                            '</div>' + 
                            '<div style="text-align:center;">' + value.name + '</div>' + 
                        '</div>' +
                            '<div>$' + value.price + '<div>' +
                        '<div>' +
                        '</div>' +
                        '</div>') 
                   $('.listCardPago').append(newDiv)
                }
            })
            console.log('Valor total:',totalPrice, 'cantidad:', count)
            $('#totalSpan').text('$'+totalPrice)
        })
    })
}

function removeTshirt(id, size){
    $(document).ready(function(){
        $.ajax({
            type: 'POST',
            url: "/remove", 
            data: {'id' : id, 'size' : size},
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

function logOut(){
    alert('Log Out')
    $(document).ready(function(){
        $.ajax({
            type: 'POST',
            url: "/logout"
        })
        $.ajax({
            url: "/redirect_home",
            type: 'GET',
            success: function(data){
                console.log(data.url)
                window.location.href = data.url
            }
        })
    }) 
}

function redirectSignUp(){
    console.log('signUp')
    $.ajax({
        url: "/redirect_sign-up",
        type: 'GET',
        success: function(data){
            console.log(data.url)
            window.location.href = data.url
        }
    })
}

function goToPage(page){
    $.ajax({
        url: "/isLoggedIn",
        type: 'GET',
        success: function(data){
            if(data.loggedIn){
                $.ajax({
                    url: page,
                    type: 'GET',
                    success: function(data){
                        console.log(data.url)
                        window.location.href = data.url
                    }
                })
            }else{
                $.ajax({
                    url: "/redirect_login",
                    type: 'GET',
                    success: function(data){
                        console.log(data.url)
                        window.location.href = data.url
                    }
                })
            }
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
}
function getView(){
    $.ajax({
        url: "/isLoggedIn",
        type: 'GET',
        success: function(data){
            $(document).ready(function(){
                $('#userOptions')
                if(data.loggedIn){
                    console.log('esta loggeado')
                    $('#userOptions').append($('<li>').html('<a class="dropdown-item logOutBtn" id="logOutBtn" onclick="logOut()">log out</a>'))
                    fetch('/getUser', {method:'POST'})
                    .then(response => response.json())
                    .then(data => {
                        console.log(data)
                    })


                }else{
                    console.log('no esta loggeado')
                    $('#userOptions').append($('<li>').html('<a href="/sign-in" class="dropdown-item">Sign-in</a>'))
                    $('#userOptions').append($('<li>').html('<a href="/sign-up" class="dropdown-item">Sign-up</a>'))
                }
            })
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
}
function getUser(){
    $(document).ready(function(){
        fetch('/getUser', {method:'POST'})
        .then(response => response.json())
        .then(data => {
            console.log('usuario',data.user.role)
            var contenido = $('#navUl').html()
            $('#goToManage').remove()
            $('#goUploadTshirts').remove()
            if (data.user.role == 'admin'){
                var li = $('<li class="nav-link">')
                li.html('<a class="nav-link" id="goToManage" href="/tshirts_admin"><b>Manage Tshirts</b></a>')
                $('#navUl').append(li)
                li = $('<li class="nav-link">')
                li.html('<a class="nav-link" id="goUploadTshirts" href="/upload-tshirt"><b>Upload Tshirts</b></a>')
                $('#navUl').append(li)
            }
        })
    })
}
function addPrintToCart(id){
    $.ajax({
        url: "/redirect_customize",
        type: 'GET',
        success: function(data){
            console.log(data.url)
            window.location.href = data.url
        }
    })
}
function redirectTshirtView(id){
    console.log('hola desde redirectTshirtView')
    $.get("/redirect_tshirt_view", {id : parseInt(id)}, function(data){
        console.log(data.url)
        window.location.href = data.url
    })
}
function redirectTshirtViewAdmin(id){
    $.get("/redirect_tshirt_view_admin", {id : parseInt(id)}, function(data){
        console.log(data.url)
        window.location.href = data.url
    })
}
function addToCart(id, size, quantity){
    console.log('id', id, 'size', size, 'quantity', quantity)
    $(document).ready(function(){
        $.ajax({
            url: '/get_stock_available/' + id + '/' + size + '/' + quantity,
            type: 'GET',
            success: function(data){
                if(data.available){
                    $.ajax({
                        type: 'POST',
                        url: "/add_to_cart", 
                        data: {'id' : id, 'size' : size, 'quantity' : quantity},
                        success: function(data){
                            reloadCart()
                        },
                        error: function(error) {
            
                            console.error('Error en la solicitud AJAX:', error);
                        },
                        complete: function() {
                            // Código que se ejecuta después de que la solicitud AJAX esté completa
                            // Esto se ejecutará incluso en caso de error
                        }
                    })
                }else{
                    alert('thers no more stock')
                }
            }
        })

    })
}
function addToStock(id, size, quantity){
    console.log('id', id, 'size', size, 'quantity', quantity)
    $(document).ready(function(){
        $.ajax({
            type: 'POST',
            url: "/add_to_stock", 
            data: {'id' : id, 'size' : size, 'quantity' : quantity},
            success: function(data){
                reloadCart()
            },
            error: function(error) {

                console.error('Error en la solicitud AJAX:', error);
            },
            complete: function() {
                // Código que se ejecuta después de que la solicitud AJAX esté completa
                // Esto se ejecutará incluso en caso de error
            }
        })
    })
}
function purchase(){
    $(document).ready(function(){
        alert('comprando')
        $.ajax({
            type: 'POST',
            url: '/finish_purchase', 
            success: function(){
                reloadCart()
            },
            error: function(error) {

                console.error('Error en la solicitud AJAX:', error);
            },
            complete: function() {
                // Código que se ejecuta después de que la solicitud AJAX esté completa
                // Esto se ejecutará incluso en caso de error
            }
        })
    })
}