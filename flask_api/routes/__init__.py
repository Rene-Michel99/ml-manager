from flask import Blueprint
from flask_restx import Api
from .route_inference import api as ns1
from .route_training import api as ns2


blueprint = Blueprint('swagger', 'swagger')

api = Api(
    blueprint,
    title='API for Mask RCNN TF 2.8 Model',
    version='1.0',
    description='API for Mask RCNN TF 2.8 Model'
)

api.add_namespace(ns1)
api.add_namespace(ns2)
