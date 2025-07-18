from odoo import Command, models


class EstateProperty(models.Model):
    _inherit = "estate.property"

    def action_property_sold(self):
        offer_id = [offer_id for offer_id in self.offer_ids if offer_id.status == 'accepted'][0]
        self.env['account.move'].create({
            'partner_id': offer_id.partner_id.id,
            'move_type': 'out_invoice',
            'line_ids': [
                Command.create({
                    'name': self.name,
                    'quantity': 1,
                    'price_unit': offer_id.price,
                }),
                Command.create({
                    'name': 'Salesperson fee',
                    'quantity': '1',
                    'price_unit': offer_id.price * 6 / 100,
                }),
                Command.create({
                    'name': 'Administration fees',
                    'quantity': '1',
                    'price_unit': 100,
                }),
            ],
        })
        return super().action_property_sold()
