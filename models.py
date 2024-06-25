from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
import os

DATABASE_URL = os.environ.get('DATABASE_URL', 'sqlite:///vidshare.db')

db = SQLAlchemy()

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(255), nullable=False)
    videos = db.relationship('Video', backref='user', lazy=True)
    comments = db.relationship('Comment', backref='user', lazy=True)

    def __repr__(self):
        return '<User %r>' % self.username

class Video(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(255), nullable=False)
    description = db.Column(db.Text, nullable=True)
    path = db.Column(db.String(255), nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    creation_date = db.Column(db.DateTime, default=datetime.utcnow)
    comments = db.relationship('Comment', backref='video', lazy=True)

    def __repr__(self):
        return '<Video %r>' % self.title

class Comment(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    content = db.Column(db.Text, nullable=False)
    video_id = db.Column(db.Integer, db.ForeignKey('video.id'), nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    creation  = db.Column(db.DateTime, default=datetime.utcnow)

    def __repr__(self):
        return '<Comment %r>' % self.content

def init_app():
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = DATABASE_URL
    db.init_app(app)
    return app