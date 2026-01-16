from flask import jsonify, request
from config import app, db
from models import Author, Book

@app.route("/")
def index():
    return {"message": "Authors API"}

# GET all authors
@app.route("/authors", methods=["GET"])
def get_authors():
    authors = Author.query.all()
    return jsonify([
        {
            "id": author.id,
            "name": author.name,
            "books": [
                {"id": book.id, "title": book.title}
                for book in author.books
            ]
        } for author in authors
    ]), 200

# POST author
@app.route("/authors", methods=["POST"])
def create_author():
    try:
        author = Author(name=request.json["name"])
        db.session.add(author)
        db.session.commit()
        return {
            "id": author.id,
            "name": author.name
        }, 201
    except Exception as e:
        return {"error": str(e)}, 400

# GET books
@app.route("/books", methods=["GET"])
def get_books():
    books = Book.query.all()
    return jsonify([
        {
            "id": book.id,
            "title": book.title,
            "author": {
                "id": book.author.id,
                "name": book.author.name
            }
        } for book in books
    ]), 200

# POST book
@app.route("/books", methods=["POST"])
def create_book():
    try:
        book = Book(
            title=request.json["title"],
            author_id=request.json["author_id"]
        )
        db.session.add(book)
        db.session.commit()
        return {
            "id": book.id,
            "title": book.title
        }, 201
    except Exception as e:
        return {"error": str(e)}, 400