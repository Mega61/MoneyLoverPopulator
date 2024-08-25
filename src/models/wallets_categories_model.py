from sqlalchemy import Column, String, ForeignKey
from sqlalchemy.orm import relationship
from models.base import Base
# from models.categories_model import Category
# from models.wallets_model import Wallet

class Wallet_Category(Base):
    __tablename__ = 'wallets_categories'
    
    category_id = Column(String, ForeignKey('categories.name'),primary_key=True)
    wallet_id = Column(String, ForeignKey('wallets.id'),primary_key=True)
    
    categories = relationship('Category', back_populates='wallets_categories')
    wallets = relationship('Wallet', back_populates='wallets_categories')
    