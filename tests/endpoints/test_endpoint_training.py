import unittest
import requests
from test_utils.json_utils import get_url


class TestServer(unittest.TestCase):
    def test_post_network_training(self):
        api_url = get_url()
        payload = {'json': 'teste'}
        api_output = requests.post(
            f'{api_url}/trainings/', json=payload, verify=False)

        self.assertIsNotNone(api_output)

    def test_post_network_inference(self):
        api_url = get_url()
        payload = {'json': 'teste'}
        api_output = requests.post(
            f'{api_url}/inferences/', json=payload, verify=False)

        self.assertEqual(200, api_output.status_code)
        self.assertIsNotNone(api_output)
