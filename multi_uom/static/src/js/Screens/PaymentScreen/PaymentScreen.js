odoo.define('multi_uom.PaymentScreen', function(require){
    'use strict';

    var PaymentScreen = require('point_of_sale.PaymentScreen');
    var Registries = require('point_of_sale.Registries');

    var PaymentScreenExtend = PaymentScreen => class extends PaymentScreen{
        async validateOrder(isForceValidate) {
            var res = await super.validateOrder(this, arguments);
            var lines = this.currentOrder.get_orderlines();
            var index = 0;
            for(var index=0; index < lines.length; index++){
                var line = lines[index];
                if(line.product.previousUomId){
                    line.product.set_previous_uom(line.product.previousUomId);
                }
            }
            return res
        }
    };

    Registries.Component.extend(PaymentScreen, PaymentScreenExtend);

    return PaymentScreenExtend;

});