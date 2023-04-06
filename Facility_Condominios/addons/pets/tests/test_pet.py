# -*- coding: utf-8 -*-
from odoo.tests.common import TransactionCase
import unittest
class TestPet(TransactionCase):
    def setUp(self):
        super(TestPet, self).setUp()
        self.pet = self.env['pet.pet'].create({'name': 'Rex', 'breed': 'Golden Retriever', 'birthdate': '2019-01-01', 'weight': 20.5})

    def test_name(self):
        self.assertEqual(self.pet.name, 'Rex')

    def test_breed(self):
        self.assertEqual(self.pet.breed, 'Golden Retriever')

    def test_birthdate(self):
        self.assertEqual(self.pet.birthdate, '2019-01-01')

    def test_weight(self):
        self.assertEqual(self.pet.weight, 20.5)
class TestPetView(TransactionCase):
    def test_pet_index(self):
        view_id = self.env.ref('pet.view_pet_index').id
        pet_id = self.env['pet.pet'].create({'name': 'Rex', 'breed': 'Golden Retriever', 'birthdate': '2019-01-01', 'weight': 20.5}).id
        view = self.env['ir.ui.view'].browse(view_id).render({'active_ids': [pet_id]})
        self.assertIn('Rex', view)
        self.assertIn('Golden Retriever', view)
        self.assertIn('2019-01-01', view)
        self.assertIn('20.5', view)
def suite():
    suite = unittest.TestSuite()
    suite.addTest(TestPet('test_name'))
    suite.addTest(TestPet('test_breed'))
    suite.addTest(TestPet('test_birthdate'))
    suite.addTest(TestPet('test_weight'))
    suite.addTest(TestPetView('test_pet_index'))
    return suite
