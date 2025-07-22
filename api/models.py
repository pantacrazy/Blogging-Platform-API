from .extensions import db
from sqlalchemy import JSON
#model_database   
class Blogs(db.Model):
    id=db.Column(db.Integer,primary_key=True)
    title=db.Column(db.String(100),nullable=False)
    content=db.Column(db.Text,nullable=False)
    category=db.Column(db.String(100),nullable=False)
    tags=db.Column(JSON)
    createdAt=db.Column(db.String(100))
    updatedAt=db.Column(db.String(100))