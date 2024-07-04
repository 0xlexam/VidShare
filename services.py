import os
from dotenv import load_dotenv
load_dotenv()
DB_HOST = os.getenv("DB_HOST")
DB_USER = os.getenv("DB_USER")
DB_PASS = os.getenv("DB_PASS")
DB_NAME = os.getenv("DB_NAME")
from sqlalchemy import create_engine, Column, Integer, String, ForeignKey, Text
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, relationship
DATABASE_URI = f'mysql+pymysql://{DB_USER}:{DB_PASS}@{DB_HO‌​ST}/{DB_NAME}'
engine = create_engine(DATABASE_URI, echo=True)
Session = sessionmaker(bind=engine)
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
    video_id = Column(Integer, ForeignKey('videos.id'))
    text = Column(Text, nullable=False)
Base.metadata.create_all(engine)
def add_video(title, description):
    session = Session()
    new_video = Video(title=title, description=description)
    session.add(new_video)
    session.commit()
    session.close()
    return new_video.id
def get_video(video_id):
    session = Session()
    video = session.query(Video).filter_by(id=video_id).first()
    session.close()
    return video
def delete_video(video_id):
    session = Session()
    video = session.query(Video).filter_by(id=video_id).delete()
    session.commit()
    session.close()
    return True
def add_comment(video_id, text):
    session = Session()
    new_comment = Comment(video_id=video_id, text=text)
    session.add(new_comment)
    session.commit()
    session.close()
    return new_comment.id
def get_comments_by_video(video_id):
    session = Session()
    comments = session.query(Comment).filter_by(video_id=video_id).all()
    session.close()
    return comments
def delete_comment(comment vc):
    session = Session()
    comment = session.query(Comment).filter_by(id=comment_id).delete()
    session.commit()
    session.close()
    return True