import json
import unittest
from unittest.mock import Mock, patch
from app import app, reformat_datetime, firing_alert

class TestApp(unittest.TestCase):
    def setUp(self):
        self.client = app.test_client()

    def test_index(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Summary Table', response.data)

    def test_webhook_get(self):
        response = self.client.get('/webhook')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(json.loads(response.data), {'status': 'success'})

    def test_webhook_post_success(self):
        payload = {'status': 'firing', 'alerts': [{'labels': {'alertname': 'test', 'severity': 'warning'}, 'annotations': {'description': 'test'}}]}
        with patch('requests.post') as mock_post:
            mock_post.return_value.status_code = 200
            response = self.client.post('/webhook', json=payload, headers={'AUTHORIZATION': 'test'})
            self.assertEqual(response.status_code, 200)
            self.assertEqual(json.loads(response.data), {'status': 'success'})

    def test_webhook_post_failure(self):
        response = self.client.post('/webhook')
        self.assertEqual(response.status_code, 400)
        self.assertEqual(json.loads(response.data), {'status': 'bad request'})

    def test_logs(self):
        response = self.client.get('/logs')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Logs', response.data)

    def test_reformat_datetime(self):
        self.assertEqual(reformat_datetime('2023-03-14T10:00:00.000Z'), '2023-03-14 10:00:00')

    def test_firing_alert(self):
        request = Mock()
        request.json = {'status': 'firing', 'alerts': [{'labels': {'alertname': 'test', 'severity': 'warning'}, 'annotations': {'description': 'test'}}]}
        request.headers = {'AUTHORIZATION': 'test'}
        with patch('requests.post') as mock_post:
            mock_post.return_value.status_code = 200
            firing_alert(request)
            mock_post.assert_called_once()

if __name__ == '__main__':
    unittest.main()
