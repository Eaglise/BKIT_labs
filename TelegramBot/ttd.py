import unittest
from functions import *

class Tests(unittest.TestCase):
    def setUp(self):
        self.city_correct = "Moscow"
        self.city_uncorrect = "Мазква"
        self.normal_request = "cat"
        self.weird_request = "fgycsynvuyqcu8947qwyyfHuank"
    def test_city_check(self):
        self.assertFalse(city_check(self.city_correct))
        self.assertTrue(city_check(self.city_uncorrect))
    def test_wrong_image_request(self):
        self.assertNotEqual(konachan(self.normal_request), "ERROR")
        self.assertEqual(konachan(self.weird_request), "ERROR")
        self.assertEqual(deviantart(self.weird_request), "ERROR")

if __name__ == "__main__":
    unittest.main()