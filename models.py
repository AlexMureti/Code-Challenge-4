from config import db
from sqlalchemy.orm import validates

class Author(db.Model):
    __tablename__ = "authors"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)

    books = db.relationship("Book", backref="author", cascade="all, delete")

    @validates("name")
    def validate_name(self, key, value):
        if not value or value.strip() == "":
            raise ValueError("Author name is required")
        return value


class Book(db.Model):
    __tablename__ = "books"

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String, nullable=False)
    author_id = db.Column(db.Integer, db.ForeignKey("authors.id"))

    @validates("title")
    def validate_title(self, key, value):
        if not value or value.strip() == "":
            raise ValueError("Book title is required")
        return value