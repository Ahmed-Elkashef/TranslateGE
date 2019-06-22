from flask import Flask, render_template, request, url_for, redirect, jsonify
from flask import flash, send_from_directory
from flask_sqlalchemy import SQLAlchemy
from flask import session as login_session
from flask import make_response
from flask_uploads import UploadSet, configure_uploads, IMAGES
from database_setup import Word, Base
from sqlalchemy import create_engine, asc, literal
from sqlalchemy.orm import sessionmaker
import random, string, httplib2, json, requests, os

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///words.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

APPLICATION_NAME = "TranslateGe"

# Connect to Database and create database session
engine = create_engine('sqlite:///words.db')
Base.metadata.bind = engine
DBSession = sessionmaker(bind=engine)
#session = scoped_sesion(sessionmaker(bind=engine))
session = DBSession()


# Show all categories
@app.route('/')
@app.route('/worterbuch')
@app.route('/worterbuch/')
def index():
    return render_template('index.html')

# serve static files
@app.route('/static_files/<path:path>')
def send_js(path):
    print(path)
    return send_from_directory('static_files', path)


# redirect to a word Page
@app.route('/worterbuch/<vocabWord>')
def showWord(vocabWord):
    word = db.session.query(Word).filter_by(vocabulary_word = vocabWord).one()
    return render_template('word.html', word = word)

# answer the autocomplete query
@app.route('/worterbuch/autocomplete=<autocompleteword>')
def showAutoComplete(autocompleteword):
    suggestions = session.query(Word).filter(Word.vocabulary_word.contains(autocompleteword)).all()
    return jsonify(suggestions=[suggestion.serialize for suggestion in suggestions])

# Show about page
@app.route('/about')
def about():
    return render_template('about.html')

# Show contact page
@app.route('/contact')
def contact():
    return render_template('contact.html')

# handle 500 error
@app.errorhandler(500)
def internal_server_error(e):
	return render_template('requestWord.html', error=e), 500


if __name__ == '__main__':
    app.debug = True
    app.secret_key = 'super_secret_key'
    app.run(host='0.0.0.0', port=3000, threaded=False)
