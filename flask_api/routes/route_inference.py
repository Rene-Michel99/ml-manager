import sys
from flask import request
from http import HTTPStatus
from flask_restx import Namespace, Resource, fields
from flask_api.utils.utils import run_inference_job
sys.path.append('..')


api = Namespace('inferences', description='network inference')

report_model = api.model(
    'Report',
    {
        'size': fields.Boolean(default=True),
        'distribution': fields.Boolean(default=True),
        'shapeObject': fields.Boolean(default=True)
    }
)

example_input = api.model(
    'Expected inference input data',
    {
        'user': fields.String('fulanodetal789'),
        'datasetPath': fields.String('https://aws.linkToS3.com'),
        'project': fields.String('ALITA'),
        'report': fields.Nested(report_model)
    }
)

example_ouput = api.model(
    'Expected inference output data', {
        'imagesProcessed': fields.String('https::/aws.linkToS3.com'),
        'report': fields.String({
            'maxSizeAlita': 20,
            'minSizeAlita': 20,
            'qtyXeno': 30,
            'qtyIso': 5
        }),
        'project': fields.String('ALITA')
    })


class InferenceNetwork(Resource):
    """Endpoint /inferences with post method.

    Args:
        Resource (inference_data): JSON containing all inference data

    Returns:
        HTTP_STATUS_CODE: Success - 200
        HTTP_STATUS_CODE: Bad Request - 400
        HTTP_STATUS_CODE: Internal Server Error - 500
    """

    @api.expect(example_input)
    @api.response(code=200, description='Success', model=example_ouput)
    @api.doc(responses={
        200: 'Success',
        400: 'Bad Request',
        500: 'Internal Server Error'
    })
    def post(self):
        """Post method with a inference data in request body

        Returns:
            200: Set of images, report and h5
            500: Internal Server Error
            400: Bad Request
        """
        try:
            json_data = request.get_json(force=True)

            run_inference_job()
            return "passed"
        except BaseException:
            return ({'error': 'Bad Request'}, HTTPStatus.BAD_REQUEST)


api.add_resource(InferenceNetwork, '/')
