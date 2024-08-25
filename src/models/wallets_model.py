from sqlalchemy import Column, String, DECIMAL
from sqlalchemy.orm import relationship
from models.base import Base
from models.transactions_model import Transaction
from models.wallets_categories_model import Wallet_Category

class Wallet(Base):
    __tablename__ = 'wallets'
    
    id = Column(String, primary_key=True)
    name = Column(String, nullable=False)
    balance = Column(DECIMAL, nullable=False)
    currency = Column(String(10), nullable=False)
    
    transactions = relationship('Transaction', back_populates='wallets')
    wallets_categories = relationship('Wallet_Category', back_populates='wallets')
    