import sys
from http import HTTPStatus
from flask import request
from flask_restx import Namespace, Resource, fields
from flask_api.utils.utils import run_training_job

sys.path.append('..')


api = Namespace('trainings', description='Training network')

example_input = api.model(
    'Expected training input data',
    {
        'user': fields.String('fulanodetal789'),
        'datasetPath': fields.String('https://drive.google.com/u/0/uc?id=1ocDfyHfj-ogDpUS0bWJ8dGhm0_AE1Lr6&export=download'),
        'project': fields.String('ALITA')
    }
)

example_output = api.model(
    'Expected training output data', {
        'trainId': fields.String('hashhda12321')
    })


class TrainingNetwork(Resource):
    """
    Endpoint /training with post method.

    Args:
        Resource (training_data): JSON containing all training data.

    Returns:
        HTTP_STATUS_CODE: Success - 200,
        HTTP_STATUS_CODE: Internal Server Error - 500
        HTTP_STATUS_CODE: Bad Request - 400
    """

    @api.expect(example_input)
    @api.response(code=200, description='Success', model=example_output)
    @api.doc(responses={
        200: 'Success',
        500: 'Internal Server Error',
        400: 'Bad Request'
    })
    def post(self):
        """Post method with a training data in request body

        Returns:
            200: Set of images
            500: Internal Server Error
            400: Bad Request
        """
        try:
            json_data = request.get_json(force=True)
            run_training_job()
            return "passed"
        except BaseException:
            return ({'error': 'Bad Request'}, HTTPStatus.BAD_REQUEST)


api.add_resource(TrainingNetwork, '/')
