import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Database configuration variables
DATABASE_HOST = os.getenv("DB_HOST")
DATABASE_USER = os.getenv("DB_USER")
DATABASE_PASSWORD = os.getenv("DB_PASS")
DATABASE_NAME = os.getenv("DB_NAME")

# Database URI configuration
DATABASE_URI = f'mysql+pymysql://{DATABASE_USER}:{DATABASE_PASSWORD}@{DATABASE_HOST}/{DATABASE_NAME}'
```
```python
from sqlalchemy import Column, Integer, String, ForeignKey, Text, create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, sessionmaker
from config import DATABASE_URI

Base = declarative_base()

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

# Engine and session creation
engine = create_engine(DATABASE_URI, echo=True)
Session = sessionmaker(bind=engine)

# Creating database schema
def init_db():
    Base.metadata.create_all(engine)
```
```python
from contextlib import contextmanager
from models import Session, Video, Comment

@contextmanager
def session_scope():
    """Provide a transactional scope around a series of operations."""
    session = Session()
    try:
        yield session
        session.commit()
    except:
        session.rollback()
        raise
    finally:
        session.close()

def add_video(title, description):
    with session_scope() as session:
        video = Video(title=title, description=description)
        session.add(video)
        return video.id

def get_video(video_id):
    with session_scope() as session:
        return session.query(Video).filter_by(id=video_id).first()

def delete_video(video_id):
    with session_scope() as session:
        session.query(Video).filter_by(id=video_id).delete()

def add_comment_to_video(video_id, content):
    with session_scope() as session:
        comment = Comment(video_id=video_id, content=content)
        session.add(comment)
        return comment.id

def get_comments_for_video(video_id):
    with session_scope() as session:
        return session.query(Comment).filter_by(video_id=video_id).all()

def delete_comment(comment_id):
    with session_scope() as session:
        session.query(Comment).filter_by(id=comment_id).delete()
```
```python
from models import init_db
from database_operations import add_video, get_video, delete_video, add_comment_to_video, get_comments_for_video, delete_comment

# Initialize Database
init_db()

# Sample operation
video_id = add_video('Sample Title', 'A simple description')
print(f"Added video ID: {video_id}")

# Fetch Video
video = get_video(video_id)
print(f"Fetched Video: {video.title}")

# Delete Video
delete_video(video_id)
print("Deleted video successfully.")

# And so on for the rest of the operations...