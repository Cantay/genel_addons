odoo.define('multi_uom.ChangeUOMButton', function (require) {
    'use strict';

    const PosComponent = require('point_of_sale.PosComponent');
    const ProductScreen = require('point_of_sale.ProductScreen');
    const Registries = require('point_of_sale.Registries');
    const { useListener } = require('web.custom_hooks');
    const { Gui } = require('point_of_sale.Gui');

    class ChangeUOMButton extends PosComponent {
        constructor() {
            super(...arguments);
            useListener('click', this._onClick);
        }
        _onClick() {
            const order = this.env.pos.get_order();
            const selectedOrderline = order.selected_orderline;
            if(selectedOrderline){
                const product = selectedOrderline.product;
                const productTemplate = product.product_tmpl_id;
                var multi_uom_lines = this.env.pos.multi_uom_lines.filter((e) => e.product_tmpl_id[0] === productTemplate);
                multi_uom_lines.sort((a, b) => a.price > b.price)
                if(multi_uom_lines.length > 0 && product.multi_uom_ok){
                    Gui.showPopup('MultiUOMPopup', {
                            title: 'Select a UOM to change.',
                            list: multi_uom_lines,
                    });
                }
                else{
                    Gui.showPopup('ErrorPopup', {
                        confirmText: 'OK',
                        cancelText: 'Cancel',
                        title: 'Error',
                        body: 'Selected product is not available for multi UOM.',
                    });
                }
            }
            else{
                Gui.showPopup('ErrorPopup', {
                    confirmText: 'OK',
                    cancelText: 'Cancel',
                    title: 'Error',
                    body: 'Please select an order line first.',
                });
            }
        }
    }
    ChangeUOMButton.template = 'multi_uom.ChangeUOMButton';

    ProductScreen.addControlButton({
        component: ChangeUOMButton,
        condition: function () {
            return true;
        },
    });

    Registries.Component.add(ChangeUOMButton);

    return ChangeUOMButton;
});
