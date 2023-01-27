from flask import Flask
from flask import request, render_template
from db_context_manager import DataBase
from tasks import get_bank_task
import all_db
import models_db
from sqlalchemy import select
from sqlalchemy.orm import Session

# from flask.ext.session import Session as FlaskSession
from flask import session as flask_session


app = Flask(__name__, static_folder="static")
app.secret_key = 'secret_key'


@app.route('/login', methods=['GET', 'POST'])
def login_user():
    if request.method == 'POST':
        try:
            user_name = request.form['username']
            user_password = request.form['password']
            user_email = request.form['email']
            with Session(all_db.engine) as session:
                statement1 = select(models_db.Users).filter_by(username=user_name,
                                                               password=user_password,
                                                               email=user_email)
                first_user = session.scalars(statement1).first()
                username, password, email = first_user.username, first_user.password, first_user.email
            firstuser = username, password, email
            if firstuser:
                return render_template('login_form.html',
                                       firstuser=firstuser)
        except AttributeError:
            return render_template('login_form.html',
                                   firstuser='No user found')
    else:
        if 'username' in flask_session:
            return render_template('login_form.html',
                                   firstuser=flask_session['username'])
        return 'Hello, you are logged out as an unknown user, please first register in our database'


@app.route('/logout', methods=['GET'])
def logout_user():
    get_bank_task()
    if 'username' in flask_session:
        return 'Operation done'
    return 'Hello, you are logged out as an unknown user, please first register in our database'


@app.route('/ok', methods=['GET'])
def ok_user():
    flask_session.pop('username', None)
    return f'Operation done'


@app.route('/register', methods=['GET', 'POST'])
def register_user():
    if request.method == 'POST':
        with Session(all_db.engine) as session:
            record = models_db.Users(username=request.form['username'],
                                     password=request.form['password'],
                                     email=request.form['email'])
            session.add(record)
            session.commit()
        with Session(all_db.engine) as session:
            query = select(models_db.Users).filter(models_db.Users.username == request.form['username'],
                                                   models_db.Users.password == request.form['password'],
                                                   models_db.Users.email == request.form['email'])
            result = session.execute(query).fetchall()
            if result:
                flask_session['username'] = request.form['username']
            else:
                return render_template('index.html', username='No user found')
            return render_template('index.html', username=flask_session['username'])
    else:
        return render_template('register_form.html')


@app.route('/user_page', methods=['GET'])
def index():
    if 'username' in flask_session:
        return f'Logged in as {flask_session["username"]}'
    return 'You are not logged in'


@app.route('/currency', methods=['GET', 'POST'])
def currency_convert():
    if request.method == 'POST':
        user_bank = request.form['bank']
        user_currency_1 = request.form['currency_1']
        user_currency_2 = request.form['currency_2']
        user_date = request.form['date']
        with Session(all_db.engine) as session:
            statement_1 = select(models_db.User).filter_by(bank=user_bank,
                                                           date=user_date,
                                                           currency=user_currency_1)
            currency_1 = session.scalars(statement_1).first()
            statement_2 = select(models_db.User).filter_by(bank=user_bank,
                                                           date=user_date,
                                                           currency=user_currency_2)
            currency_2 = session.scalars(statement_2).first()
            buy_rate_1, sale_rate_1 = currency_1.buy_rate, currency_1.sale_rate
            buy_rate_2, sale_rate_2 = currency_2.buy_rate, currency_2.sale_rate
        operation_buy = buy_rate_2 / buy_rate_1
        operation_sale = sale_rate_2 / sale_rate_1
        return render_template('data_form.html',
                               operation_buy=round(operation_buy, 2),
                               operation_sale=round(operation_sale, 2),
                               user_currency_1=user_currency_1,
                               user_currency_2=user_currency_2,
                               username=flask_session['username'])
    else:
        if 'username' in flask_session:
            return render_template('data_form.html',
                                   username=flask_session['username'])
        return 'Hello, you are logged out as an unknown user, please first register in our database'


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000, debug=True)






