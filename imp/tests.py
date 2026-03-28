from django.test import SimpleTestCase


class AdminSmokeTests(SimpleTestCase):
    def test_admin_login_page_loads(self):
        response = self.client.get('/admin/login/')

        self.assertEqual(response.status_code, 200)
