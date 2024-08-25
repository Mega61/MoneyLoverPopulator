import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import unittest
from facades.data_transformator_facade import Data_transformator

class TestDataTransformator(unittest.TestCase):

    def test_categories_parsing(self):
        transformator_agent = Data_transformator()
        expected_categories = transformator_agent.category_parsing('web0819308cd4fff84a1158595f18a03')
        self.assertTrue(expected_categories, 'The categories data should not be empty')
        
        
    def test_subcategories_parsing(self):
        transformator_agent = Data_transformator()
        expected_subcategories = transformator_agent.subcategory_parsing('web0819308cd4fff84a1158595f18a03')
        self.assertTrue(expected_subcategories, 'The subcategories data should not be empty')
    
    
    
if __name__ == '__main__':
    unittest.main()
