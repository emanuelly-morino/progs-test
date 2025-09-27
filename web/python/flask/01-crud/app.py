from flask import Flask, request, render_template, redirect, url_for
from pony.orm import Database, Required, db_session, select

app = Flask(__name__)

# Configure Pony ORM (SQLite for simplicity)
db = Database()
db.bind(provider='sqlite', filename='books.db', create_db=True)

# Class declaration
class Book(db.Entity):
    title = Required(str)
    author = Required(str)

# Create tables mapping
db.generate_mapping(create_tables=True)

# --------------------
# ROUTES
# --------------------

# Home: List all books
@app.route('/')
@db_session
def index():
    # get all books
    data = Book.select()
    # pass the results to the HTML template
    return render_template("book_list.html", books=data)
    
# Create new book
@app.route('/create', methods=['GET', 'POST'])
@db_session
def create():
    # is the user creating a new book?
    if request.method == 'POST':
        # get data from form
        title = request.form['title']
        author = request.form['author']
        # create the book
        Book(title=title, author=author)
        # redirect to home page
        return redirect(url_for('index'))

    # else... show the form to be filled
    return render_template("book_new.html")  

# Update existing book
@app.route('/update/<int:book_id>', methods=['GET', 'POST'])
@db_session
def update(book_id):
    # try to get the book
    book = Book.get(id=book_id)
    # found it?
    if book:  
        # are you updating an existing book?
        if request.method == 'POST':
            # update its data
            book.title = request.form['title']
            book.author = request.form['author']
        
            # redirect to home page
            return redirect(url_for('index'))

        # else... show the form to be filled
        return render_template("book_edit.html", book=book)
    
    # if we are here, the book was not found
    # return to the home page
    return redirect(url_for('index'))

# Delete a book
@app.route('/delete/<int:book_id>')
@db_session
def delete(book_id):
    # try to get the book
    book = Book.get(id=book_id)
    # found it?
    if book:
        # delete it
        book.delete()

    # anyway, redirect to home page   
    return redirect(url_for('index'))

# start the application
app.run(debug=True, host='0.0.0.0', port=80)