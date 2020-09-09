import os

from flask import Flask, session, redirect, url_for, render_template
from views.alerts import alert_blueprint
from views.stores import store_blueprint
from views.users import user_blueprint

app = Flask(__name__)
# app.secret_key='1234'
app.config['SECRET_KEY'] = '123456'
app.config.update(ADMIN=os.environ.get('ADMIN'))

app.register_blueprint(alert_blueprint, url_prefix='/alerts')
app.register_blueprint(store_blueprint, url_prefix='/stores')
app.register_blueprint(user_blueprint, url_prefix='/users')


@app.route('/')
def home():
    return render_template('home.html')


if __name__ == '__main__':
    app.run(port=4995, debug=True)
