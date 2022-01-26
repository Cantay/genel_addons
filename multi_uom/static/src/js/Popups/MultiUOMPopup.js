odoo.define('multi_uom.MultiUOMPopup', function (require) {
    'use strict';

    const { Gui } = require('point_of_sale.Gui');
    const SelectionPopup = require('point_of_sale.SelectionPopup');
    const Registries = require('point_of_sale.Registries');

    class MultiUOMPopup extends SelectionPopup {
        async selectItem(itemId) {
            const list = this.props.list;
            for(const record of list){
                const tr = document.getElementById(String(record.id));
                tr.style.color = '';
                tr.style.backgroundColor = '';
            }
            const selectedIdInput = document.getElementById('selectedId');
            const selectedTr = document.getElementById(String(itemId));
            selectedTr.style.backgroundColor = '#b7bded';
            selectedTr.style.color = '#ffffff';
            selectedIdInput.value = itemId;
        }

        async confirm() {
            const multiUOMLines = this.env.pos.multi_uom_lines;
            const order = this.env.pos.get_order();
            const selectedOrderLine = order.get_selected_orderline();
            const selectedIdInput = document.getElementById('selectedId');
            var selectedMultiUOMLine = multiUOMLines.filter((line) => line.id === parseInt(selectedIdInput.value));
            selectedMultiUOMLine = selectedMultiUOMLine[0]
            const uom_id = selectedMultiUOMLine.uom_id;
            const price = selectedMultiUOMLine.price;
            const previousUomId = selectedOrderLine.product.uom_id;
            selectedOrderLine.multi_uom_line_id = selectedMultiUOMLine.id;
            selectedOrderLine.setUom(previousUomId, uom_id, price);
            this.props.resolve({ confirmed: true, payload: await this.getPayload() });
            this.trigger('close-popup');
        }
    }
    MultiUOMPopup.template = 'MultiUOMPopup';
    MultiUOMPopup.defaultProps = {
        confirmText: 'Confirm',
        cancelText: 'Cancel',
        title: 'Select',
        body: '',
        list: [],
    };

    Registries.Component.add(MultiUOMPopup);

    return MultiUOMPopup;
});
