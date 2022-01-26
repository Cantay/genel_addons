odoo.define('multi_uom.OrderLineDetails', function(require){
    'use strict';

    var OrderLineDetails = require('point_of_sale.OrderlineDetails');
    var Registries = require('point_of_sale.Registries');
    const { format } = require('web.field_utils');
    const { round_precision: round_pr } = require('web.utils');

    var OrderLineDetailsExtend = OrderLineDetails => class extends OrderLineDetails{
        get line() {
            const line = this.props.line;
            const formatQty = (line) => {
                const quantity = line.get_quantity();
                const unit = line.get_unit();
                const decimals = this.env.pos.dp['Product Unit of Measure'];
                const rounding = Math.max(unit.rounding, Math.pow(10, -decimals));
                const roundedQuantity = round_pr(quantity, rounding);
                return format.float(roundedQuantity, { digits: [69, decimals] });
            };
            if(line.multi_uom_line_id){
                var multiUomLine = this.env.pos.multi_uom_lines.filter((l) => l.id === line.multi_uom_line_id)[0];
            }
            else{
                var multiUomLine = this.env.pos.multi_uom_lines.filter((l) => l.uom_id[0] === line.get_unit().id)[0];
            }
            return {
                productName: line.get_full_product_name(),
                totalPrice: line.get_price_with_tax(),
                quantity: formatQty(line),
                unit: line.get_unit().name,
                unitPrice: line.get_unit_price(),
                multiUomLine: multiUomLine,
            };
        }
        get pricePerUnit() {
            var uom = this.line.multiUomLine.display_name;
            return ` ${uom} at ${this.unitPrice} / ${uom}`;
        }
    };

    Registries.Component.extend(OrderLineDetails, OrderLineDetailsExtend);

    return OrderLineDetailsExtend;

});