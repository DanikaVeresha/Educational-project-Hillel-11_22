import sqlite3


def context_manager():
    with sqlite3.connect('currency_pair.db') as db:
        cursor = db.cursor()
        bank = 'OTPbank'
        currency = 'GPB'
        date = '2022-12-01'
        buy_rate = 1.49
        sale_rate = 0.45
        query = f"""INSERT INTO currency_pair(bank, currency, date, buy_rate, sale_rate) VALUES('{bank}', '{currency}', '{date}', {buy_rate}, {sale_rate})"""
        cursor.execute(query)
        db.commit()


context_manager()
