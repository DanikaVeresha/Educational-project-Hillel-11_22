import sqlite3


class DBManager:
    def __enter__(self):
        self.con = sqlite3.connect("currency_pair.db")
        self.cursor = self.con.cursor()
        return self

    def __exit__(self):
        self.cursor.close()
        self.con.close()

    def get_query(self, query):
        result_query = self.cursor.execute(query)
        result = result_query.fetchone()
        return result


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


