from .routes import api 
from flask_restplus import fields

cat = api.model('Cat', {
    'id': fields.String(required=True, description='The cat identifier'),
    'name': fields.String(required=True, description='The cat name'),
})


catDetails = api.model("Cat Details",
                                 {
                                     "catName": fields.String(description="Cat Name", required=True),
                                     "catAge": fields.Integer(description="Cat Age", required=True),
                                     "catBreed": fields.String(description="Cat Breed", required=True),
                                     "catColor": fields.String(description="Cat Color"),
                                 }
                                 )