from facades.moneylover_facade import Moneylover
from models.wallets_model import Wallet
from models.transactions_model import Transaction
from models.categories_model import Category
from util.category_conversion import translate_category

class Data_transformator:
    def __init__(self) -> None:
        self.moneylover = Moneylover()
    
    def wallet_parsing(self):
        raw_wallets = self.moneylover.get_wallets()
        parsed_wallets = []
        for wallet in raw_wallets:
            wallet_id = wallet.get('_id')
            wallet_name = wallet.get('name')
            balance_info = wallet.get('balance', [{}])[0]
            if balance_info:
                currency, balance = next(iter(balance_info.items()))
                balance = float(balance)
            else:
                currency, balance = None, 0.0

            wallet = Wallet(id=wallet_id, name=wallet_name, balance=balance ,currency=currency)
            parsed_wallets.append(wallet)
        return parsed_wallets
    
    def transaction_parsing(self, start_date, end_date):
        raw_transactions = self.moneylover.get_transactions(start_date, end_date)
        parsed_transactions = []
        for transaction in raw_transactions:
            transaction_id = transaction.get('_id')
            note = transaction.get('note')
            wallet_id = transaction.get('account', {}).get('_id')
            category_id = translate_category(transaction.get('category', {}).get('name'))
            amount = transaction.get('amount')
            display_date = transaction.get('displayDate')
            created_at = transaction.get('createdAt')
            
            transaction = Transaction(id=transaction_id, note=note, wallet_id=wallet_id, category_id=category_id, amount=amount, display_date=display_date, created_at=created_at)
            parsed_transactions.append(transaction)
        return parsed_transactions
    
    def category_parsing(self, wallet_id):
        raw_categories = self.moneylover.get_categories(wallet_id)
        parsed_categories = []
        for category in raw_categories:
            category_id = category.get('_id')
            name = category.get('name')
            parent_category = category.get('parent', None)
            
            if parent_category is None:
                category = Category(id=category_id, name=name, parent_id=None)
                parsed_categories.append(category)
            else:
                category = Category(id=category_id, name=name, parent_id=parent_category)
                parsed_categories.append(category)
        
        return parsed_categories
    
            
            
        
        