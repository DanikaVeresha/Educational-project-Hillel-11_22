from flask import Flask
from flask import request, render_template
import sqlite3


app = Flask(__name__, static_folder="static")


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
    if request.method == 'POST':
        con = sqlite3.connect("currency.db")
        cursor = con.cursor()
        user_bank = request.form['bank']
        user_currency_1 = request.form['currency_1']
        user_currency_2 = request.form['currency_2']
        user_date = request.form['date']
        res = cursor.execute(f'SELECT buy_rate, sale_rate FROM currency WHERE bank = "{user_bank}" and date = "{user_date}" and currency ="{user_currency_1}"')
        buy_rate_1, sale_rate_1 = res.fetchone()
        res = cursor.execute(f'SELECT buy_rate, sale_rate FROM currency WHERE bank = "{user_bank}" and date = "{user_date}" and currency ="{user_currency_2}"')
        buy_rate_2, sale_rate_2 = res.fetchone()
        operation_buy = buy_rate_2 / buy_rate_1
        operation_sale = sale_rate_2 / sale_rate_1
        cursor.close()
        con.close()
        return render_template('data_form.html',
                               operation_buy=operation_buy,
                               operation_sale=operation_sale,
                               user_currency_1=user_currency_1,
                               user_currency_2=user_currency_2)
    else:
        return render_template('data_form.html')


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000, debug=True)