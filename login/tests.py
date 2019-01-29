from django.test import TestCase


class BasicViewTests(TestCase):
    """ Check that the main views work """

    def test_basic_0(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 404)
        
    def test_basic_1(self):
        response = self.client.get('/accounts/login/')
        self.assertEqual(response.status_code, 200)

    def test_basic_2(self):
        response = self.client.get('/accounts/logout/')
        self.assertEqual(response.status_code, 200)

    def test_basic_3(self):
        response = self.client.get('/accounts/profile/')
        self.assertEqual(response.status_code, 200)
