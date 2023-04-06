from odoo.tests.common import TransactionCase
from odoo.exceptions import ValidationError
from ..models.bike import Bike


class TestBike(TransactionCase):

    def setUp(self, *args, **kwargs):
        super(TestBike, self).setUp(*args, **kwargs)
        self.bike = self.env['bicicletario.bike'].create({
            'name': 'Bike1',
            'unit': 'A',
            'brand': 'Brand1',
            'model': 'Model1',
        })

    def test_bike_creation(self):
        self.assertEqual(self.bike.name, 'Bike1')
        self.assertEqual(self.bike.unit, 'A')
        self.assertEqual(self.bike.brand, 'Brand1')
        self.assertEqual(self.bike.model, 'Model1')
