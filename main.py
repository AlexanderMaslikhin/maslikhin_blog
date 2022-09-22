import torch
from flask import Blueprint
from flask import Flask, url_for
import simpsons

app = Flask(__name__)
app.config['SERVER_NAME'] = 'maslikhin.ru'

bp = Blueprint('subdomain', __name__, subdomain='dl')


@bp.route('/')
def index():
    models = {'inception': torch.load('./simpsons_model.pkl'),
              'dense': torch.load('./dense.pt', map_location=torch.device('cpu'))}
    labels = {m_name: simpsons.classify('./static/test_imgs/1.jpg', model)
              for m_name, model in models.items()}
    file = url_for('static', filename='/test_imgs/1.jpg')
    result = f'<img src="{file}"></img><br>'
    for m_name, label in labels.items():
        result += f'Model {m_name}: {label}<br>'
    return result



@app.route("/")
def hello():
    return "<h1 style='color:blue'>Coming soon...</h1><i>Скоро тут что-то будет... " \
           "Но это не точно</i>"


app.register_blueprint(bp)

if __name__ == "__main__":
    app.run(host='0.0.0.0')
