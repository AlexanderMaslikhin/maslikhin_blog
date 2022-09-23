from flask import Blueprint
from flask import Flask, url_for
from simpsons import models, classify

app = Flask(__name__)
app.config['SERVER_NAME'] = 'maslikhin.ru'

bp = Blueprint('subdomain', __name__, subdomain='dl')


@bp.route('/<f_name>')
def index(f_name=None):
    if not f_name:
        f_name = '1.jpg'
    labels = {m_name: classify('./static/test_imgs/' + f_name, model)
              for m_name, model in models.items()}
    file = url_for('static', filename=f'/test_imgs/{f_name}')
    result = f'<img src="{file}"></img><br>'
    for m_name, label in labels.items():
        result += f'Model {m_name}: {label[0]} - {label[1]*100}%<br>'
    return result


@bp.route('/')
def void_index():
    return index()


@app.route("/")
def hello():
    return "<h1 style='color:blue'>Coming soon...</h1><i>Скоро тут что-то будет... " \
           "Но это не точно</i>"


app.register_blueprint(bp)

if __name__ == "__main__":
    app.run(host='0.0.0.0')
