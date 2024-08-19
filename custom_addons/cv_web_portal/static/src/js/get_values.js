/** @odoo-module */
import publicWidget from "web.public.widget";

publicWidget.registry.Many2many_tag = publicWidget.Widget.extend({
    selector: '.new-get_data',
    start: function () {
        this._super.apply(this, arguments);
        $('.js-example-basic-multiple').select2();
    },
});
