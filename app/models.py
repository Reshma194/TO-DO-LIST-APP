from app import db 
#it brings the sqlalchemy instance from __init__.py
#creating user model
class Task(db.Model):
    id=db.Column(db.Integer,primary_key=True)
    title=db.Column(db.String(100),nullable=False)
    status=db.Column(db.String(20),default="Pending")
