from flask import Flask, request, render_template, redirect, url_for
from pony.orm import Database, Required, db_session, select

app = Flask(__name__)

# Configure Pony ORM (SQLite for simplicity)
db = Database()
db.bind(provider='sqlite', filename='books.db', create_db=True)

class Book(db.Entity):
    title = Required(str)
    author = Required(str)

db.generate_mapping(create_tables=True)


# --------------------
# ROUTES
# --------------------

# Home: List all books
@app.route('/')
@db_session
def index():
    books = select(b for b in Book)[:]
    return render_template("book_list.html", books=books)
    
# Create new book
@app.route('/create', methods=['GET', 'POST'])
@db_session
def create():
    if request.method == 'POST':
        title = request.form['title']
        author = request.form['author']
        Book(title=title, author=author)
        return redirect(url_for('index'))

    return render_template("book_new.html")
    

# Update existing book
@app.route('/update/<int:book_id>', methods=['GET', 'POST'])
@db_session
def update(book_id):
    book = Book.get(id=book_id)
    if not book:
        return "Book not found", 404

    if request.method == 'POST':
        book.title = request.form['title']
        book.author = request.form['author']
        return redirect(url_for('index'))

    return render_template("book_edit.html", book=book)

# Delete a book
@app.route('/delete/<int:book_id>')
@db_session
def delete(book_id):
    book = Book.get(id=book_id)
    if book:
        book.delete()
    return redirect(url_for('index'))


if __name__ == '__main__':
    app.run(debug=True)

