from flask import Flask
from flask import Blueprint
app = Flask(__name__)
app.config['SERVER_NAME'] = 'maslikhin.ru'

bp = Blueprint('subdomain', __name__, subdomain='dl')



@bp.route('/')
def index():
    return 'Deep Learning section'

app.route("/")
def hello():
    return "<h1 style='color:blue'>Coming soon...</h1><i>Скоро тут что-то будет... Но это не точно</i>"


if __name__ == "__main__":
    app.run(host='0.0.0.0')