#This is to set up the server and database. So it knows the database and how to connect. 
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate


#postgresql+psycopg2://postgres:postgres@localhost:5432/hello_books_development
#postgresql+psycopg2 : connecting PostgresSQL database with Psyco PG 2 (liberary code)
#:// : protocol to connect with 
#postgres:postgres : connect to postgres database - connect as the user postgres and connect as local host, port 5342
#hello_books_development : database name that we are connecting - this should be updated when we use different database


#create a SQLAlchemy object to interact with datebase
#create a migrate object, will be used when we need to change the structure of the datatbase
db = SQLAlchemy()
migrate = Migrate()

def create_app():
    app = Flask(__name__)

    #DB Configure 
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql+psycopg2://postgres:postgres@localhost:5432/hello_books_development'

    #initlize SQLAlchemy object, and says this is the application we are going to work with
    # tell Migrate that this is the application I want you to work with, and tell the way to get to database 
    db.init_app(app)
    migrate.init_app(app,db)

    from app.models.book import Book

    from .routes import hello_world_bp
    app.register_blueprint(hello_world_bp)
    from .routes import books_bp
    app.register_blueprint(books_bp)
    
    return app





