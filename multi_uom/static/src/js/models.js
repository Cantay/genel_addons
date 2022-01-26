odoo.define('multi_uom.models', function (require) {
    'use strict';
    const models = require('point_of_sale.models');
    var utils = require('web.utils');
    var round_di = utils.round_decimals;

    models.load_fields('product.product', ['multi_uom_ok']);
    models.load_models([
        {
            model: 'multi.uom.line',
            fields: [],
            loaded: function(self, lines){
                self.multi_uom_lines = lines;
            },
        },
    ]);

    models.Order = models.Order.extend({
        add_product: function(product, options){
            if(this._printed){
                this.destroy();
                return this.pos.get_order().add_product(product, options);
            }
            this.assert_editable();
            options = options || {};
            var line = new models.Orderline({}, {pos: this.pos, order: this, product: product, multi_uom_line_id: options.multi_uom_line_id});
            this.fix_tax_included_price(line);

            this.set_orderline_options(line, options);

            var to_merge_orderline;
            for (var i = 0; i < this.orderlines.length; i++) {
                if(this.orderlines.at(i).can_be_merged_with(line) && options.merge !== false){
                    to_merge_orderline = this.orderlines.at(i);
                }
            }
            if (to_merge_orderline){
                to_merge_orderline.merge(line);
                this.select_orderline(to_merge_orderline);
            } else {
                this.orderlines.add(line);
                this.select_orderline(this.get_last_orderline());
            }

            if (options.draftPackLotLines) {
                this.selected_orderline.setPackLotLines(options.draftPackLotLines);
            }
            if (this.pos.config.iface_customer_facing_display) {
                this.pos.send_current_order_to_customer_facing_display();
            }
            },
        });

    var orderline_id = 1;
    const superOrderLine = models.Orderline.prototype;
    models.Orderline = models.Orderline.extend({

        initialize: function(attr,options){
            this.pos   = options.pos;
            this.order = options.order;
            if (options.json) {
                try {
                    this.init_from_JSON(options.json);
                } catch(error) {
                    console.error('ERROR: attempting to recover product ID', options.json.product_id,
                        'not available in the point of sale. Correct the product or clean the browser cache.');
                }
                return;
            }
            this.product = options.product;
            this.set_product_lot(this.product);
            this.set_quantity(1);
            this.discount = 0;
            this.discountStr = '0';
            this.selected = false;
            this.description = '';
            this.price_extra = 0;
            this.full_product_name = '';
            this.id = orderline_id++;
            this.price_manually_set = false;
            this.customerNote = this.customerNote || '';
            this.multi_uom_line_id = options.multi_uom_line_id;

            if (options.price) {
                this.set_unit_price(options.price);
            } else {
                this.set_unit_price(this.product.get_price(this.order.pricelist, this.get_quantity()));
            }
        },

        init_from_JSON: function(json) {
            this.product = this.pos.db.get_product_by_id(json.product_id);
            this.set_product_lot(this.product);
            this.price = json.price_unit;
            this.set_discount(json.discount);
            this.set_quantity(json.qty, 'do not recompute unit price');
            this.set_description(json.description);
            this.set_price_extra(json.price_extra);
            this.set_full_product_name(json.full_product_name);
            this.id = json.id ? json.id : orderline_id++;
            orderline_id = Math.max(this.id+1,orderline_id);
            var pack_lot_lines = json.pack_lot_ids;
            for (var i = 0; i < pack_lot_lines.length; i++) {
                var packlotline = pack_lot_lines[i][2];
                var pack_lot_line = new models.Packlotline({}, {'json': _.extend(packlotline, {'order_line':this})});
                this.pack_lot_lines.add(pack_lot_line);
            }
            this.tax_ids = json.tax_ids && json.tax_ids.length !== 0 ? json.tax_ids[0][2] : undefined;
            this.set_customer_note(json.customer_note);
            this.refunded_qty = json.refunded_qty;
            this.refunded_orderline_id = json.refunded_orderline_id;
            this.multi_uom_line_id = json.multi_uom_line_id;
        },

        export_as_JSON: function() {
            var values = superOrderLine.export_as_JSON.apply(this, arguments);
            Object.assign(values, {
                pos_uom_id: this.uom_id,
                multi_uom_line_id: this.multi_uom_line_id,
            })
            return values
        },

        setUom: function(previousUomId, uom_id, price){
            this.set_unit_price(price);
            this.uom_id = uom_id[0];
            this.uom_price = price;
            this.price_manually_set = true;
            this.product.previousUomId = previousUomId;
            this.set_unit_price(price);
            this.trigger('change', this);
        },

        set_unit_price: function(price){
            if(this.uom_id){
                arguments[0] = this.uom_price;
            }
            superOrderLine.set_unit_price.apply(this, arguments);
        },

        get_multi_unit: function(){
            var self = this;
            var lineId = this.multi_uom_line_id;
            if(lineId){
                var multiUomLine = this.pos.multi_uom_lines.filter((l) => l.id === lineId)[0];
            }
            else{
                var multiUomLine = this.pos.multi_uom_lines.filter((l) => l.uom_id[0] === self.get_unit().id)[0];
            }
            if(multiUomLine){
                return multiUomLine.display_name;
            }
            else{
                return self.get_unit().display_name;
            }
        },

        can_be_merged_with: function(orderline){
            var price = parseFloat(round_di(this.price || 0, this.pos.dp['Product Price']).toFixed(this.pos.dp['Product Price']));
            var order_line_price = orderline.get_product().get_price(orderline.order.pricelist, this.get_quantity());
            order_line_price = orderline.compute_fixed_price(order_line_price);
            if( this.get_product().id !== orderline.get_product().id){    //only orderline of the same product can be merged
                return false;
            }else if(!this.get_unit() || !this.get_unit().is_pos_groupable){
                return false;
            }else if(this.get_discount() > 0){             // we don't merge discounted orderlines
                return false;
            }else if(!utils.float_is_zero(price - order_line_price - orderline.get_price_extra(),
                        this.pos.currency.decimals)){
                return false;
            }else if(this.product.tracking == 'lot' && (this.pos.picking_type.use_create_lots || this.pos.picking_type.use_existing_lots)) {
                return false;
            }else if (this.description !== orderline.description) {
                return false;
            }else if (orderline.get_customer_note() !== this.get_customer_note()) {
                return false;
            } else if (this.refunded_orderline_id) {
                return false;
            }else{
                return true;
            }
        },

    });

    models.Product = models.Product.extend({
        set_previous_uom: function(previousUomId){
            this.uom_id = previousUomId;
        },
    });

    console.log('TICKET', models.PosModel.prototype.models);

});