from django.test import TestCase, Client

# Create your tests here.
class MyWatchListTest(TestCase):
    def test_html(self):
        urls_test = Client().get('/mywatchlist/html/')
        self.assertEqual(urls_test.status_code, 200)

    def test_xml(self):
        urls_test = Client().get('/mywatchlist/xml/')
        self.assertEqual(urls_test.status_code, 200)
        
    def test_json(self):
        urls_test = Client().get('/mywatchlist/json/')
        self.assertEqual(urls_test.status_code, 200)