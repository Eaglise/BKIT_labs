from bridge import *
from unittest import TestCase
from unittest.mock import patch

class Tests(TestCase):
    @patch('bridge.CookedSalad.list_ingredients', return_value="Salad ingredients: vegetables, meat, sauce")
    def test_meat_ingr(self, list_igredients):
        self.cook = SaladCook()
        self.assertEqual(self.cook.salad.list_ingredients(), "Salad ingredients: vegetables, meat, sauce")

if __name__ == "__main__":
    unittest.main()