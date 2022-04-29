# from our main app folder, I am going to import db
# db is the db variable, so it is going to be instance of SQLAlchemy
from app import db

class Book(db.Model):
    id = db.Column(db.Integer, primary_key = True, autoincrement = True)
    title = db.Column(db.String)
    description = db.Column(db.String)
    __tablename__ = "books"

    def to_string(self):
        return f"{self.id} : {self.title} Description {self.description}"