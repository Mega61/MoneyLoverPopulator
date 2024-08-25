import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import unittest
from facades.moneylover_facade import Moneylover

class TestMoneylover(unittest.TestCase):

    def test_token_generation(self):
        moneylover_agent = Moneylover()
        expected_token = moneylover_agent.get_token()
        print(expected_token)
        self.assertTrue(expected_token, 'The token should not be empty')
        self.assertTrue(expected_token.startswith('ey'), 'The token should be JWT')

    def test_get_wallets(self):
        moneylover_agent = Moneylover()
        expected_wallets_data = moneylover_agent.get_wallets()
        self.assertTrue(expected_wallets_data, 'The wallets data should not be empty')

    def test_get_transactions(self):
        moneylover_agent = Moneylover()
        start_date = '2024-05-01'
        end_date = '2024-05-01'
        expected_transaction_data = moneylover_agent.get_transactions(start_date, end_date)
        self.assertTrue(expected_transaction_data, 'The transaction list should not be empty')

    def test_get_categories(self):
        moneylover_agent = Moneylover()
        wallet_id = 'web0819308cd4fff84a1158595f18a03'
        expected_categories_data = moneylover_agent.get_categories(wallet_id)
        print(expected_categories_data)
        self.assertTrue(expected_categories_data, 'The categories data should not be empty')
        
if __name__ == '__main__':
    unittest.main()
