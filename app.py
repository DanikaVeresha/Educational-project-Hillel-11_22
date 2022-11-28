from flask import Flask
from flask import request, render_template


app = Flask(__name__)


@app.route('/login', methods=['GET', 'POST'])
def login_user():
    if request.method == 'GET':
        return 'login_user GET/login'
    else:
        return 'login_user POST/login'


@app.route('/logout', methods=['GET'])
def logout_user():
    return 'logout_user'


@app.route('/register', methods=['GET', 'POST'])
def register_user():
    if request.method == 'GET':
        return 'register_user GET/register'
    else:
        return 'register_user POST/register'


@app.route('/user_page', methods=['GET'])
def user_page():
    return 'user_page'


@app.route('/currency', methods=['GET', 'POST'])
def currency_convert():
    currency_pair = [
        {'bank': 'A1', 'date': '2022-11-25', 'currency': 'UAH', 'buy_rate': 0.025, 'sale_rate': 0.023},
        {'bank': 'A1', 'date': '2022-11-25', 'currency': 'EUR', 'buy_rate': 0.9, 'sale_rate': 0.95},
        {'bank': 'A1', 'date': '2022-11-25', 'currency': 'USD', 'buy_rate': 1, 'sale_rate': 1},
        {'bank': 'A1', 'date': '2022-11-25', 'currency': 'GPB', 'buy_rate': 1.15, 'sale_rate': 1.12},

        {'bank': 'PrivatBank', 'date': '2022-11-25', 'currency': 'UAH', 'buy_rate': 0.030, 'sale_rate': 0.028},
        {'bank': 'PrivatBank', 'date': '2022-11-25', 'currency': 'EUR', 'buy_rate': 0.91, 'sale_rate': 0.89},
        {'bank': 'PrivatBank', 'date': '2022-11-25', 'currency': 'USD', 'buy_rate': 1, 'sale_rate': 1},
        {'bank': 'PrivatBank', 'date': '2022-11-25', 'currency': 'GPB', 'buy_rate': 1.41, 'sale_rate': 1.27},

        {'bank': 'Monobank', 'date': '2022-11-25', 'currency': 'UAH', 'buy_rate': 0.048, 'sale_rate': 0.036},
        {'bank': 'Monobank', 'date': '2022-11-25', 'currency': 'EUR', 'buy_rate': 0.96, 'sale_rate': 0.93},
        {'bank': 'Monobank', 'date': '2022-11-25', 'currency': 'USD', 'buy_rate': 1, 'sale_rate': 1},
        {'bank': 'Monobank', 'date': '2022-11-25', 'currency': 'GPB', 'buy_rate': 1.27, 'sale_rate': 1.18},

        {'bank': 'OshadBank', 'date': '2022-11-25', 'currency': 'UAH', 'buy_rate': 0.037, 'sale_rate': 0.033},
        {'bank': 'OshadBank', 'date': '2022-11-25', 'currency': 'EUR', 'buy_rate': 0.89, 'sale_rate': 0.87},
        {'bank': 'OshadBank', 'date': '2022-11-25', 'currency': 'USD', 'buy_rate': 1, 'sale_rate': 1},
        {'bank': 'OshadBank', 'date': '2022-11-25', 'currency': 'GPB', 'buy_rate': 1.24, 'sale_rate': 1.21}
    ]
    if request.method == 'POST':
        user_bank = request.form['bank']
        user_currency_1 = request.form['currency_1']
        user_currency_2 = request.form['currency_2']
        user_date = request.form['date']
        buy_rate_1 = 0
        buy_rate_2 = 0
        sale_rate_1 = 0
        sale_rate_2 = 0
        for item in currency_pair:
            if user_bank == item['bank'] and user_currency_1 == item['currency'] and user_date == item['date']:
                buy_rate_1 = item['buy_rate']
                sale_rate_1 = item['sale_rate']
            if user_bank == item['bank'] and user_currency_2 == item['currency'] and user_date == item['date']:
                buy_rate_2 = item['buy_rate']
                sale_rate_2 = item['sale_rate']
        operation_buy = buy_rate_2 / buy_rate_1
        operation_sale = sale_rate_2 / sale_rate_1
        return render_template('data_form.html',
                               operation_buy=operation_buy,
                               operation_sale=operation_sale,
                               user_currency_1=user_currency_1,
                               user_currency_2=user_currency_2)
    else:
        return render_template('data_form.html')

