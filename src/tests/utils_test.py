import unittest
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from util.category_conversion import translate_category


class TestUtils(unittest.TestCase):

    def test_category_conversion(self):
        translated_category = translate_category('Food & Beverage')
        print(translated_category)
        self.assertTrue(translated_category, 'The category should be translated')


if __name__ == '__main__':
    unittest.main()
