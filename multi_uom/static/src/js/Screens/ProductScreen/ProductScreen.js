odoo.define('multi_uom.ProductScreen', function(require){
    'use strict';

    const ProductScreen = require('point_of_sale.ProductScreen');
    const Registries = require('point_of_sale.Registries');
    const NumberBuffer = require('point_of_sale.NumberBuffer');

    const ProductScreenExtend = ProductScreen => class extends ProductScreen{
        async _clickProduct(event) {
            if (!this.currentOrder) {
                this.env.pos.add_new_order();
            }
            const product = event.detail;
            const options = await this._getAddProductOptions(product);
            // Do not add product if options is undefined.
            if (!options) return;
            if (product.previousUomId){
                Object.assign({price: product.})
            }
            // Add the product after having the extra information.
            this.currentOrder.add_product(product, options);
            NumberBuffer.reset();
        }
    };

    Registries.Component.extend(ProductScreen, ProductScreenExtend);

    return ProductScreenExtend;

});