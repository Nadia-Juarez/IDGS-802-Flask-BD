from flask import Flask, render_template
from flask import request, url_for
import forms
from flask import jsonify
from config import DevelopmentConfig
from flask_wtf.csrf import CSRFProtect
from models import db, Alumnos

app = Flask(__name__)
app.config.from_object(DevelopmentConfig)
csrf = CSRFProtect()

@app.route('/', methods=['GET','POST'])
def formulario():
    form = forms.UserForm(request.form)
    if request.method == 'POST':
        alum = Alumnos(
            id = form.id.data,
            nombre = form.nombre.data,
            apellidos = form.apellidos.data,
            email = form.email.data)
        db.session.add(alum)
        db.session.commit()
        
    return render_template('index.html', form = form)

if __name__ == '__main__':
    csrf.init_app(app)
    db.init_app(app)
    with app.app_context():
        db.create_all()
    app.run(port=3000)