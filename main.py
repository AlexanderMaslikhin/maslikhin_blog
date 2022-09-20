from flask import Blueprint
from flask import Flask, url_for

app = Flask(__name__)
app.config['SERVER_NAME'] = 'maslikhin.ru'

bp = Blueprint('subdomain', __name__, subdomain='dl')


@bp.route('/')
def index():
    file = url_for('static', filename='/test_imgs/1.jpg')
    return f'<img src="{file}"></img>'


@app.route("/")
def hello():
    return "<h1 style='color:blue'>Coming soon...</h1><i>Скоро тут что-то будет... Но это не точно</i>"


app.register_blueprint(bp)

if __name__ == "__main__":
    app.run(host='0.0.0.0')
