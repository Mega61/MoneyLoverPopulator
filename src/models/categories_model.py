from sqlalchemy import Column, String, ForeignKey
from sqlalchemy.orm import relationship, backref
from models.base import Base
from models.wallets_categories_model import Wallet_Category


class Category(Base):
    __tablename__ = 'categories'

    id = Column(String, primary_key=True)
    name = Column(String, nullable=False)
    parent_id = Column(String, ForeignKey('categories.id'), nullable=True)

    parent = relationship('Category', remote_side=[id])
    wallets_categories = relationship('Wallet_Category', back_populates='categories')
    transactions = relationship('Transaction', back_populates='categories')
