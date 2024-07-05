import os
from dotenv import load_dotenv
from sqlalchemy import create_engine, Column, Integer, String, ForeignKey, Text
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, relationship

# Load environment variables
load_dotenv()

# Database configuration variables
DATABASE_HOST = os.getenv("DB_HOST")
DATABASE_USER = os.getenv("DB_USER")
DATABASE_PASSWORD = os.getenv("DB_PASS")
DATABASE_NAME = os.getenv("DB_NAME")

# Database URI configuration
DATABASE_URI = f'mysql+pymysql://{DATABASE_USER}:{DATABASE_PASSWORD}@{DATABASE_HOST}/{DATABASE_NAME}'

# Creating engine and session factory
engine = create_engine(DATABASE_URI, echo=True)
Session = sessionmaker(bind=engine)
Base = declarative_base()

# Models
class Video(Base):
    __tablename__ = 'videos'
    id = Column(Integer, primary_key=True)
    title = Column(String(255), nullable=False)
    description = Column(Text, nullable=True)
    comments = relationship('Comment', backref='video')

class Comment(Base):
    __tablename__ = 'comments'
    id = Column(Integer, primary_key=True)
    video_id = Column(Integer, ForeignKey('videos.id'), nullable=False)
    content = Column(Text, nullable=False)

# Creating database schema
Base.metadata.create_all(engine)

# Function to add a new video
def add_video(title, description):
    session = Session()
    video = Video(title=title, description=description)
    session.add(video)
    session.commit()
    video_id = video.id
    session.close()
    return video_id

# Function to retrieve a video by id
def fetch_video(video_id):
    session = Session()
    video = session.query(Video).filter_by(id=video_id).first()
    session.close()
    return video

# Function to remove a video by id
def remove_video(video_id):
    session = Session()
    session.query(Video).filter_by(id=video_id).delete()
    session.commit()
    session.close()
    return True

# Function to add a new comment to a video
def add_video_comment(video_id, content):
    session = Session()
    comment = Comment(video_id=video_id, text=content)
    session.add(comment)
    session.commit()
    comment_id = comment.id
    session.close()
    return comment_id

# Function to retrieve all comments for a specific video
def fetch_video_comments(video_id):
    session = Session()
    comments = session.query(Comment).filter_by(video_id=video_id).all()
    session.close()
    return comments

# Function to remove a comment by id
def remove_comment(comment_id):
    session = Session()
    session.query(Comment).filter_by(id=comment_id).delete()
    session.commit()
    session.close()
    return True