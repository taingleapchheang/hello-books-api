from app import db
from app.models.book import Book
from flask import Blueprint,jsonify,make_response,request

books_bp = Blueprint("books", __name__, url_prefix="/books")
@books_bp.route("", methods=["POST", "GET"])
def handle_books():
    if request.method == "POST":
        #this method will give us the request body information
        request_body = request.get_json()

        if "title" not in request_body or "description" not in request_body:
            return make_response("Invalid request", 400)

        new_book = Book(
            title = request_body["title"],
            description = request_body["description"]
        )
        # tell SQLAlchemy to take this book instance and add it to database
        # staging the changes - stage to be ready for change
        # committing the change to database
        db.session.add(new_book)
        db.session.commit()
        
        return make_response(f" Book {new_book.title} created", 201)
    
    elif request.method == "GET":
        books = Book.query.all()
        books_response = []
        for book in books:
            books_response.append({
                "id" : book.id,
                "title": book.title,
                "description" : book.description
            })
        return jsonify(books_response)
        

hello_world_bp = Blueprint("hello_world", __name__)
@hello_world_bp.route("/hello_world" , methods = ["GET"])
def say_hello_world():
    my_beautiful_response_body = "Hello, World!"
    return my_beautiful_response_body