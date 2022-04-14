from flask import Flask, render_template
from data import db_session

db_session.global_init("db/baza_danix.db")

app = Flask(__name__)
app.config['SECRET_KEY'] = 'yandexlyceum_secret_key'


@app.route('/')
@app.route('/authorization')
def index():
    return render_template('authorization_form.html')


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')
