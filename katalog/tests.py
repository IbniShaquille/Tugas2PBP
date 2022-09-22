from django.test import TestCase, Client

# Create your tests here.
class MyWatchListTest(TestCase):
    def html_test(self):
        urls_test = Client().get('/mywatchlist/html')
        self.assertEqual(urls_test.status_code, 200)

    def xml_test(self):
        urls_test = Client().get('/mywatchlist/xml')
        self.assertEqual(urls_test.status_code, 200)
        
    def json_test(self):
        urls_test = Client().get('/mywatchlist/json')
        self.assertEqual(urls_test.status_code, 200)