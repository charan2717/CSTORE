from flask import Flask, render_template, request, redirect, url_for, flash
from werkzeug.utils import secure_filename
import os
from models import db, App
from forms import AppUploadForm
from config import Config

app = Flask(__name__)
app.config.from_object(Config)
db.init_app(app)

with app.app_context():
    db.create_all()

@app.route('/')
def index():
    apps = App.query.all()
    return render_template('index.html', apps=apps)

@app.route('/app/<int:app_id>')
def app_detail(app_id):
    app_data = App.query.get_or_404(app_id)
    return render_template('app_detail.html', app=app_data)

@app.route('/upload', methods=['GET', 'POST'])
def upload():
    form = AppUploadForm()
    if form.validate_on_submit():
        image = form.image.data
        file = form.file.data

        image_filename = secure_filename(image.filename) if image else None
        file_filename = secure_filename(file.filename) if file else None

        if image:
            image.save(os.path.join('static/uploads', image_filename))
        if file:
            file.save(os.path.join('uploads', file_filename))

        new_app = App(
            name=form.name.data,
            description=form.description.data,
            image=image_filename,
            file=file_filename
        )
        db.session.add(new_app)
        db.session.commit()
        flash('App uploaded successfully!', 'success')
        return redirect(url_for('index'))

    return render_template('upload.html', form=form)

if __name__ == '__main__':
    app.run(debug=True)
