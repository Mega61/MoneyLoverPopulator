from sqlalchemy import Column, String, DECIMAL, TIMESTAMP, ForeignKey
from sqlalchemy.orm import relationship
from models.base import Base
# from models.wallets_model import Wallet
from models.categories_model import Category


class Transaction(Base):

    __tablename__ = 'transactions'

    id = Column(String, primary_key=True)
    note = Column(String, nullable=True)
    wallet_id = Column(String, ForeignKey('wallets.id'), nullable=False)
    category_id = Column(String, ForeignKey('categories.name'), nullable=False)
    amount = Column(DECIMAL, nullable=False)
    display_date = Column(TIMESTAMP, nullable=False)
    created_at = Column(TIMESTAMP, nullable=False)

    wallets = relationship('Wallet', back_populates='transactions')
    categories = relationship('Category', back_populates='transactions')
