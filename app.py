from flask import Flask, render_template, redirect
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
    create_form = forms.UserForm(request.form)
    if request.method == 'POST':
        alum = Alumnos(
            id = create_form.id.data,
            nombre = create_form.nombre.data,
            apellidos = create_form.apellidos.data,
            email = create_form.email.data)
        db.session.add(alum)
        db.session.commit()
        
    return render_template('index.html', form = create_form)

@app.route('/modificar', methods=['GET','POST'])
def modificar():
    update_form=forms.UserForm(request.form)
    if request.method=="GET":
        id=request.args.get("id")
        alum1=db.session.query(Alumnos).filter(Alumnos.id==id).first()
        update_form.id.data=request.args.get("id")
        update_form.nombre.data=alum1.nombre
        update_form.apellidos.data=alum1.apellidos
        update_form.email.data=alum1.email

    if request.method=="POST":
        id=update_form.id.data
        alum=db.session.query(Alumnos).filter(Alumnos.id==id).first()
        alum.nombre=update_form.nombre
        alum.apellidos=update_form.apellidos
        alum.email=update_form.email

        db.session.add(alum)
        db.session.commit()
        return redirect(url_for("ABCCompleto"))
    return render_template('modificar.html', form = update_form)

@app.route('/ABCompleto', methods=['GET','POST'])
def ABCompleto():
    form=forms.UserForm(request.form)
    alumno=Alumnos.query.all()

    return render_template("ABCompleto.html",form=form,alumno=alumno)


if __name__ == '__main__':
    csrf.init_app(app)
    db.init_app(app)
    with app.app_context():
        db.create_all()
    app.run(port=3000)