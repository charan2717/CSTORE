from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class App(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    description = db.Column(db.Text, nullable=False)
    image = db.Column(db.String(120))
    file = db.Column(db.String(120))
