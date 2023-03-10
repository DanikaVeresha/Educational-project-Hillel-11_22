import requests
import datetime
from sqlalchemy.orm import Session
import all_db
import models_db


def PB_bank():
    current_date = datetime.datetime.now().strftime("%d.%m.%Y")
    db_date = datetime.datetime.now().strftime("%Y-%m-%d")
    inquiry = requests.get(f'https://api.privatbank.ua/p24api/exchange_rates?json&date={current_date}')
    currency_info = inquiry.json()
    saleRate_USD = 0
    purchaseRate_USD = 0
    purchaseRate_UAH = 0
    saleRate_UAH = 0
    for item in currency_info['exchangeRate']:
        if item['currency'] == 'USD':
            saleRate_USD = item['saleRate']
            purchaseRate_USD = item['purchaseRate']
        elif item['currency'] == 'UAH':
            saleRate_UAH = item['saleRateNB']
            purchaseRate_UAH = item['purchaseRateNB']
    with Session(all_db.engine) as session:
        saleRate_currency_UAH = saleRate_UAH / saleRate_USD
        purchaseRate_currency_UAH = purchaseRate_UAH / purchaseRate_USD
        record_UAH = models_db.User(bank="Privatbank",
                                    currency="UAH",
                                    date=db_date,
                                    buy_rate=purchaseRate_currency_UAH,
                                    sale_rate=saleRate_currency_UAH)
        session.add(record_UAH)
        session.commit()
    for item in currency_info['exchangeRate']:
        currency_name = item['currency']
        if item.get('saleRate'):
            saleRate_currency = item['saleRate'] / saleRate_USD
            purchaseRate_currency = item['purchaseRate'] / purchaseRate_USD
            record_PB = models_db.User(bank="Privatbank",
                                       currency=currency_name,
                                       date=db_date,
                                       buy_rate=purchaseRate_currency,
                                       sale_rate=saleRate_currency)
            session.add(record_PB)
            session.commit()
