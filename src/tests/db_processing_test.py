import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import unittest
from facades.db_processing_facade import DB_processor

class TestDBProcessor(unittest.TestCase):

    def test_populate_categories(self):
        processor_agent = DB_processor()
        processor_agent.populate_categories()
    
    
    
if __name__ == '__main__':
    unittest.main()
