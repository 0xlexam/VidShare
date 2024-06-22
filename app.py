from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from dotenv import load_dotenv
import os

load_dotenv()

flask_app = Flask(__name__)

flask_app.config['SECRET_KEY'] = os.getenv('SECRET_KEY')
flask_app.config['DATABASE_CONNECTION_URI'] = os.getenv('DATABASE_URI')
flask_app.config['DISABLE_SQLALCHEMY_TRACK_MODIFICATIONS'] = False

database = SQLAlchemy(flask_app)

class UserAccount(database.Model):
    user_id = database.Column(database.Integer, primary_key=True)
    user_name = database.Column(database.String(80), unique=True, nullable=False)

from video_sharing_blueprint import video_sharing_blueprint

flask_app.register_blueprint(video_sharing_blueprint, url_prefix='/video_sharing')

if __name__ == '__main__':
    flask_app.run(debug=True)