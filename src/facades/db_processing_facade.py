from sqlalchemy.orm import Session
from models.db_engine import Alchemy_engine
from facades.data_transformator_facade import Data_transformator
from models.wallets_model import Wallet
from models.wallets_categories_model import Wallet_Category


class DB_processor:
    def __init__(self) -> None:
        self.data_processor = Data_transformator()

    def populate_wallets(self):
        session = Session(bind=Alchemy_engine.create_engine())
        for wallet in self.data_processor.wallet_parsing():
            session.merge(wallet)
        session.commit()

    def populate_transactions(self, start_date, end_date):
        session = Session(bind=Alchemy_engine.create_engine())
        for transaction in self.data_processor.transaction_parsing(start_date, end_date):
            session.merge(transaction)
        session.commit()

# All the categories are going to be based of the @efectivo wallet, including the @efectivo subcategory
    def populate_categories(self):
        session = Session(bind=Alchemy_engine.create_engine())
        wallet_ids = session.query(Wallet.id).all()
        for category in self.data_processor.category_parsing('b56df28c17784067b4b718909fec7609'):
            session.merge(category)
            for wallet_id in wallet_ids:
                session.merge(Wallet_Category(wallet_id=wallet_id[0], category_id=category.name))
        session.commit()
        
