from flask_restplus import Api

from .cats.routes import api as cat_api


api = Api(
    title='Zoo API',
    version='1.0',
    description='A simple demo API',
)


api.add_namespace(cat_api)