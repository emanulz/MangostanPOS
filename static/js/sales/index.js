
$(document).on('ready', main_sales );

function main_sales() {

        //Selectors
        var product_panel = $('.cd-panel-search-product');
        var client_panel = $('.cd-panel-search-client');
        var pay_panel = $('.cd-panel-pay');

        var btn_product_search = $('.product-search-btn');
        var btn_client_search = $('.btn-client-search');
        var btn_pay = $('.btn-pay');

        //EVENTS PRODUCT SEARCH PANEL

        btn_product_search.on('click', function(event){
            event.preventDefault();
            product_panel.addClass('is-visible');
            blurElement('.blur-div',2);
        });

        product_panel.on('click', function(event){
            if( $(event.target).is('.cd-panel') || $(event.target).is('.cd-panel-close') ) {
                product_panel.removeClass('is-visible');
                blurElement('.blur-div',0);
                event.preventDefault();
            }
        });

        $('#btncerrarbuscar').on('click', function(event){
                product_panel.removeClass('is-visible');
                blurElement('.blur-div',0);
                event.preventDefault();
        });

        //EVENTS PRODUCT SEARCH PANEL

        btn_client_search.on('click', function(event){
            event.preventDefault();
            client_panel.addClass('is-visible');
            blurElement('.blur-div',2);
        });

        client_panel.on('click', function(event){
            if( $(event.target).is('.cd-panel') || $(event.target).is('.cd-panel-close') ) {
                client_panel.removeClass('is-visible');
                blurElement('.blur-div',0);
                event.preventDefault();
            }
        });

        $('#btncerrarbuscarcliente').on('click', function(event){
                client_panel.removeClass('is-visible');
                blurElement('.blur-div',0);
                event.preventDefault();
        });

        //EVENTS PRODUCT SEARCH PANEL

        btn_pay.on('click', function(event){
            event.preventDefault();
            pay_panel.addClass('is-visible');
            blurElement('.blur-div',2);
        });

        pay_panel.on('click', function(event){
            if( $(event.target).is('.cd-panel') || $(event.target).is('.cd-panel-close') ) {
                pay_panel.removeClass('is-visible');
                blurElement('.blur-div',0);
                event.preventDefault();
            }
        });

        $('#btncerrarbuscarpay').on('click', function(event){
                pay_panel.removeClass('is-visible');
                blurElement('.blur-div',0);
                event.preventDefault();
        });

        localStorage.Products=null;


}//main

function blurElement(element, size){

    var filterVal = 'blur('+size+'px)';
    $(element)
      .css('filter',filterVal)
      .css('webkitFilter',filterVal)
      .css('mozFilter',filterVal)
      .css('oFilter',filterVal)
      .css('msFilter',filterVal);

}

function products_to_memory() {

    $.get('/api/products/', function (data) {

        $.each(data, function (i) {

            $('.new_order_search').append($('<option>', {
                value: data[i].product_code,
                text: data[i].product_description
            }));
        });

        localStorage.Products=JSON.stringify(data);
    });

}//SAVE PRODUCTS TO LOCAL STORAGE