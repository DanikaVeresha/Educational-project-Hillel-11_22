from db_context_manager import DataBase


def write_new_data():
    '''Записать новие данные в базу данных'''
    with DataBase() as db:
        cursor = db.cursor()
        bank = 'OTPbank'
        currency = 'UAH'
        date = '2022-12-01'
        buy_rate = 0.036
        sale_rate = 0.031
        query = f"""INSERT INTO currency_pair(bank, currency, date, buy_rate, sale_rate) VALUES('{bank}', '{currency}', '{date}', {buy_rate}, {sale_rate})"""
        cursor.execute(query)
        db.commit()


write_new_data()

