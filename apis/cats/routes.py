from flask_restplus import Namespace, Resource, fields, reqparse
from flask import request
api = Namespace('cats', description='Cats related operations')

from .models import *


CATS = [
    {'id': 'felix', 'name': 'Felix'},
]




@api.route('/')
class CatList(Resource):
    @api.doc('list_cats')
    @api.marshal_list_with(cat)
    def get(self):
        '''List all cats'''
        return CATS


@api.route('/<id>')
@api.param('id', 'The cat identifier')
@api.response(404, 'Cat not found')
class Cat(Resource):
    @api.doc('get_cat')
    @api.marshal_with(cat)
    def get(self, id):
        '''Fetch a cat given its identifier'''
        for cat in CATS:
            if cat['id'] == id:
                return cat
        api.abort(404)

    @api.doc('update_cat')
    @api.expect(catDetails)
    @api.marshal_with(cat)
    def put(self, id):
        '''Update a cat given its identifier'''
        for cat in CATS:
            if cat['id'] == id:
                return cat
        api.abort(404)



@api.route('/createCatData')
@api.expect(catDetails)
@api.response(404, 'Cat not found')
class Cat(Resource):
    def post(self):
        parser = reqparse.RequestParser()
        parser.add_argument('catName', type=str, help='You need to enter the cat name', required=True)
        parser.add_argument('catAge', type=int, help='You need to enter the cat age', required=True)
        parser.add_argument('catBreed', type=str, help='You need to enter the cat breed', required=True)
        parser.add_argument('catColor', type=str, help='You need to enter the cat color', required=True)
        args = parser.parse_args()         
        json_data = request.get_json(force=True)
        return json_data