import unittest
from bridge import *

class Tests(unittest.TestCase):
    def setUp(self):
        self.cook = SaladCook()
        self.chief = SaladChief(self.cook)
    def test_start_cooking(self):
        self.assertEqual(self.chief.StartCooking(), "Started cooking!")
    def test_cooking(self):
        self.assertEqual(self.chief.cook_meat_salad(), "Cooking meat salad...")
        self.assertEqual(self.chief.cook_vegetarian_salad(), "Cooking vegetarian salad...")
    def test_ingredients(self):
        self.chief.cook_meat_salad()
        self.assertEqual(self.cook.salad.list_ingredients(), "Salad ingredients: vegetables, meat, sauce")
        self.chief.cook_vegetarian_salad()
        self.assertEqual(self.cook.salad.list_ingredients(), "Salad ingredients: vegetables, sauce")
    def test_no_cooking(self):
        self.assertEqual(self.cook.salad.list_ingredients(), "There is no salad ready")
    def test_no_recipe(self):
        with self.assertRaises(AttributeError):
            self.chief.cook_pizza()

if __name__ == "__main__":
    unittest.main()