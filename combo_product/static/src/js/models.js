odoo.define('combo_product.combo_items', function (require) {
    "use strict";

var models = require('point_of_sale.models');

models.load_models([{
    model:  'combo.item',
    fields: ['id', 'product_id', 'product_template_id', 'quantity', 'remarks'],
    loaded: function(self, combo_items) {
        self.combo_items = combo_items
    }
}]);

});
