from sqlalchemy import Column, Integer, String, Float
from all_db import Base


class User(Base):
    __tablename__ = 'currency_pair'
    id = Column(Integer, primary_key=True, unique=True)
    bank = Column(String(50))
    currency = Column(String(120))
    date = Column(String(120))
    buy_rate = Column(Float)
    sale_rate = Column(Float)

    def __init__(self, bank, currency, date, buy_rate, sale_rate):
        self.bank = bank
        self.currency = currency
        self.date = date
        self.buy_rate = buy_rate
        self.sale_rate = sale_rate

    def __repr__(self):
        return f'<User {self.name!r}>'
