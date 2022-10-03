from flask import Blueprint
from flask import Flask, url_for, send_from_directory, request, send_file, abort, render_template
from werkzeug.utils import secure_filename
import os
from io import BytesIO
from PIL import Image
from img_proc import create_image
from simpsons import models, classify
import traceback

app = Flask(__name__)
app.config['SERVER_NAME'] = 'maslikhin.ru'

UPLOAD_FOLDER = '/tmp/uploads/'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

bp = Blueprint('subdomain', __name__, subdomain='dl')
ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg', 'gif'}


def allowed_file(filename):
    """ Функция проверки расширения файла """
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


@bp.route('/')
def index():
    return "<h3 align='center'>Раздел по глубокому обучению</h3>"


@bp.route('/simpsons', methods=['GET', 'POST'])
def simpsons():
    filename = ''
    if request.method == 'GET':
        return render_template('simpsons.html')
    else:
        if 'image' in request.files and request.files['image'].filename != '' and \
             request.files['image'] and allowed_file(request.files['image'].filename):
            file = request.files['image']
            filename = os.path.join(app.config['UPLOAD_FOLDER'], secure_filename(file.filename))
            file.save(filename)
            pass
        elif request.form.get('im_url'):
            pass
        try:
            result_img = simpsons_classification_pipeline(filename)
            img_io = BytesIO()
            result_img.save(img_io, 'JPEG', quality=70)
            img_io.seek(0)
            return send_file(img_io, mimetype='image/jpeg')
        except Exception as error:
            tb = traceback.format_exc()
            return abort(500, f'Ошибка при обработке файла {filename}. {tb}')


def simpsons_classification_pipeline(f_name):
    image = Image.open(f_name)
    image.verify()
    labels = [m_name + ': ' + classify(f_name, model) for m_name, model in models.items()]
    result_img = create_image(labels, f_name)
    return result_img


@app.route("/")
def hello():
    return "<h1 style='color:blue'>Coming soon...</h1><i>Скоро тут что-то будет... " \
           "Но это не точно</i>"


app.register_blueprint(bp)

if __name__ == "__main__":
    app.run(host='0.0.0.0')
