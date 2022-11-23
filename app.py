from flask import Flask
from flask import request


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
    if request.method == 'GET':
        return 'currency_convert GET/currency'
    else:
        return 'currency_convert POST/currency'

# в терминале проверила после запуска этого кода
# посмотрела карту маршрутов, командой flask routes - все работает