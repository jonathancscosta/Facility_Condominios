from odoo import http

class PetController(http.Controller):

@http.route('/pet', auth='public', website=True)
def index(self, **kw):
    pets = http.request.env['pet.pet'].search([])
    return http.request.render('pet.index', {'pets': pets})

@http.route('/pet/<int:pet_id>', auth='public', website=True)
def detail(self, pet_id, **kw):
    pet = http.request.env['pet.pet'].sudo().browse(pet_id)
    return http.request.render('pet.detail', {'pet': pet})

@http.route('/pet/create', auth='public', website=True)
def create(self, **kw):
    return http.request.render('pet.create')

@http.route('/pet/create', auth='public', website=True, methods=['POST'])
def create_pet(self, **kw):
    pet = http.request.env['pet.pet'].create({
        'name': kw.get('name'),
        'breed': kw.get('breed'),
        'birthdate': kw.get('birthdate'),
        'weight': kw.get('weight'),
    })
    return http.request.redirect('/pet/{}'.format(pet.id))
