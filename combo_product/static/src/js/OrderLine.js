odoo.define('combo_product.OrderlineExtend', function (require) {
    'use strict';

    const Registries = require('point_of_sale.Registries');
    const Orderline = require('point_of_sale.Orderline');

    const OrderlineExtend = Orderline => class extends Orderline {
        getComboProducts(line){
            if (line.quantity <= 0){
                return []
            }
            var return_combo_lines = []
            var all_combo_items = new Array(this.env.pos.combo_items)
            all_combo_items = all_combo_items[0]
            const product_id = line.product.id;
            const product = this.env.pos.db.get_product_by_id(parseInt(product_id))
            const product_tmpl_id = product.product_tmpl_id

            for (let index = 0; index < all_combo_items.length; index++) {
                if(all_combo_items[index].product_template_id[0] === product_tmpl_id){
                    return_combo_lines.push({
                        product: all_combo_items[index].product_id[1],
                        quantity: line.quantity * all_combo_items[index].quantity
                    })   
                }
            }
            return return_combo_lines
        }
    }

    Registries.Component.extend(Orderline, OrderlineExtend);

    return OrderlineExtend;
});
