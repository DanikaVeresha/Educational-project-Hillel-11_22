from flask import Flask
from flask import request, render_template
from db_context_manager import DataBase
from tasks import get_bank_tasks
import all_db
import models_db
from sqlalchemy import select, insert
from sqlalchemy.orm import Session

app = Flask(__name__, static_folder="static")


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
            return render_template('userpost_login_form.html',
                                   firstuser=firstuser)
        except AttributeError:
            return 'Sorry, this user is not in our database'
    else:
        return render_template('userget_login_form.html')


@app.route('/logout', methods=['GET'])
def logout_user():
    get_bank_tasks.apply_async()
    return f'Operation done / logout / OK'


@app.route('/register', methods=['GET', 'POST'])
def register_user():
    if request.method == 'POST':
        with Session(all_db.engine) as session:
            record = models_db.Users(username=request.form['username'],
                                     password=request.form['password'],
                                     email=request.form['email'])
            session.add(record)
            session.commit()
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
        return render_template('userpost_form.html',
                               firstuser=firstuser)
    else:
        return render_template('userget_form.html')


@app.route('/user_page', methods=['GET'])
def user_page():
    return 'user_page'


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
                               user_currency_2=user_currency_2)
    else:
        return render_template('data_form.html')


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000, debug=True)






