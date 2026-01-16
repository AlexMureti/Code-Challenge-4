from config import app, db
from models import Author, Book

with app.app_context():
    db.drop_all()
    db.create_all()

    author1 = Author(name="Chinua Achebe")
    author2 = Author(name="Ngũgĩ wa Thiong'o")

    book1 = Book(title="Things Fall Apart", author=author1)
    book2 = Book(title="Petals of Blood", author=author2)

    db.session.add_all([author1, author2, book1, book2])
    db.session.commit()

    print("Database seeded")