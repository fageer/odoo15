/** @odoo-module **/

const { Component } = owl;
const { useState } = owl.hooks;
const FormRenderer = require('web.FormRenderer');
const { ComponentWrapper } = require('web.OwlCompatibility');

class PartnerSummary extends Component {
    partner = useState({});

    constructor(self, partner){
        super();
        this.partner = partner;
    }

     resPartner(){
        alert("Hello")
    }
};
Object.assign(PartnerSummary, {
    template: "owl_partner_summary.PartnerSummary"
});

FormRenderer.include({
    async _renderView(){
        await this._super(...arguments);

        for(const element of this.el.querySelectorAll(".o_partner_order_summary")){
            this._rpc({
                model: "res.partner",
                method: "read",
                args: [[this.state.data.partner_id.res_id]]
            }).then(data => {
                (new ComponentWrapper(
                    this,
                    PartnerSummary,
                    useState(data[0])
                )).mount(element);
            });
        }
    }
});
