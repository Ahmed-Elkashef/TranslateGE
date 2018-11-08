from flask import Flask, render_template, request, url_for, redirect, jsonify
from flask import flash
from flask_uploads import UploadSet, configure_uploads, IMAGES
from sqlalchemy import create_engine, asc, literal
from sqlalchemy.orm import sessionmaker
from database_setup import Word, Base
from flask import session as login_session
import random
import string
from oauth2client.client import flow_from_clientsecrets
from oauth2client.client import FlowExchangeError
import httplib2
import json
from flask import make_response
import requests
import os

app = Flask(__name__)

CLIENT_ID = json.loads(
    open('client_secrets.json', 'r').read())['web']['client_id']
APPLICATION_NAME = "TranslateGe"

# Instantiate the uploads object
photos = UploadSet('photos', IMAGES)

# Providing upload destination
app.config['UPLOADED_PHOTOS_DEST'] = 'static/'
configure_uploads(app, photos)

# Connect to Database and create database session
engine = create_engine('sqlite:///words.db')
Base.metadata.bind = engine

DBSession = sessionmaker(bind=engine)
session = DBSession()


# Show login page
@app.route('/login')
def login():
    # Create anti-forgery state token
    state = ''.join(random.choice(string.ascii_uppercase + string.digits)
                    for x in xrange(32))
    login_session['state'] = state
    # return "The current session state is %s" % login_session['state']
    return render_template('login.html', STATE=state)


# Show all categories
@app.route('/')
#@app.route('/worterbuch')
#@app.route('/worterbuch/')
def index():
    return render_template('index.html')

# redirect to a word Page
@app.route('/worterbuch/<vocabWord>')
def showWord(vocabWord):
    word = session.query(Word).filter_by(vocabulary_word = vocabWord).one()
    return render_template('word.html', word = word)

# answer the autocomplete query
@app.route('/worterbuch/autocomplete=<autocompleteword>')
def showAutoComplete(autocompleteword):
    suggestions = session.query(Word).filter(Word.vocabulary_word.contains(autocompleteword)).all()
    return jsonify(suggestions=[suggestion.serialize for suggestion in suggestions])

# Show a single category with list of items
@app.route('/categories/autocomplete?search=<categoryName>')
def showCategory(categoryName):
    category = session.query(Category).filter_by(name=categoryName).one()
    category_items = session.query(CategoryItem).filter_by(category_id=category.id).all()
    return render_template('category.html', category=category, category_items=category_items)


# Show a single Item
@app.route('/categories/<category>/<int:item_id>')
def showItem(category, item_id):
    category = session.query(Category).filter_by(name=category).one()
    item = session.query(CategoryItem).filter_by(id=item_id).one()
    return render_template('category_item.html', category=category, category_item=item)


# Add a new category
@app.route('/categories/new', methods=['GET', 'POST'])
def newCategory():
    if 'username' not in login_session:
        return redirect('/login')
    if request.method == 'POST' and 'photo' in request.files:
        filename = photos.save(request.files['photo'])
        newCategory = Category(
            name=request.form['name'],
            user_id=login_session['user_id'],
            picture=filename)
        session.add(newCategory)
        flash('New Category %s Successfully Created' % newCategory.name)
        session.commit()
        return redirect(url_for('index'))
    else:
        return render_template('newCategory.html')


# Delete a category
@app.route('/categories/<category>/delete', methods=['GET', 'POST'])
def deleteCategory(category):
    categoryToDelete = session.query(Category).filter_by(name=category).one()
    if 'username' not in login_session:
        return redirect('/login')
    if categoryToDelete.user_id != login_session['user_id']:
        return "<script>"
        "function myFunction() {"
        +"alert('You are not authorized to delete this Category. "
        +"Please create your own category in order to delete.');}"
        +"</script>"
        +"<body onload='myFunction()'>"
    if request.method == 'POST':
        session.delete(categoryToDelete)
        # os.remove(os.path.join('/static', categoryToDelete.picture))
        flash('Category: %s Successfully Deleted' % categoryToDelete.name)
        session.commit()
        return redirect(url_for('index'))
    else:
        return render_template('deleteCategory.html', category=category)


# Add a new item
@app.route('/categories/<category>/newitem', methods=['GET', 'POST'])
def addNewItem(category):
    if 'username' not in login_session:
        return redirect('/login')
    categoryForItems = session.query(Category).filter_by(name=category).one()
    if login_session['user_id'] != categoryForItems.user_id:
        return "<script>function myFunction() {"
        +"alert('You are not authorized to add items to this category. "
        +"Please create your own category in order to add items.');}"
        +"</script>"
        +"<body onload='myFunction()'>"
    if request.method == 'POST':
        filename = photos.save(request.files['photo'])

        newItem = CategoryItem(name=request.form['name'],
                               description=request.form['description'],
                               price=request.form['price'],
                               picture=filename,
                               category=categoryForItems)

        session.add(newItem)
        flash('New Item %s Successfully Created' % newItem.name)
        session.commit()
        return redirect(url_for('index'))
    else:
        return render_template('newItem.html', category=category)


# Update a single Item
@app.route('/<category>/<int:item_id>/updateItem', methods=['GET', 'POST'])
def updateItem(category, item_id):
    if 'username' not in login_session:
        return redirect('/login')
    category = session.query(Category).filter_by(name=category).one()
    item = session.query(CategoryItem).filter_by(id=item_id).one()
    if login_session['user_id'] != category.user_id:
        return "<script>function myFunction() {"
        +"alert('You are not authorized to edit items to this category. "
        +"Please create your own category in order to edit items.');}"
        +"</script>"
        +"<body onload='myFunction()'>"
    if request.method == 'POST':
        if request.form['name']:
            item.name = request.form['name']
        if request.form['description']:
            item.description = request.form['description']
        if request.form['price']:
            item.price = request.form['price']
        if 'photo' in request.files:
            filename = photos.save(request.files['photo'])
            item.picture = filename
        session.add(item)
        flash('Category: %s Successfully Updated' % newCategory.name)
        session.commit()
        return redirect(url_for('index'))
    else:
        return render_template('updateItem.html', category=category, item=item)


# Delete a single Item
@app.route('/<category>/<int:item_id>/deleteItem', methods=['GET', 'POST'])
def deleteItem(category, item_id):
    if 'username' not in login_session:
        return redirect('/login')
    category = session.query(Category).filter_by(name=category).one()
    item = session.query(CategoryItem).filter_by(id=item_id).one()
    if login_session['user_id'] != category.user_id:
        return "<script>function myFunction() {"
        +"alert('You are not authorized to delete items to this category. "
        +"Please create your own category in order to delete items.');}"
        +"</script>"
        +"<body onload='myFunction()'>"
    if request.method == 'POST':
        session.delete(item)
        # os.remove(os.path.join('/static', item.picture))
        flash('Item: %s Successfully Deleted' % item.name)
        session.commit()
        return redirect(url_for('index'))
    else:
        return render_template('deleteItem.html', category=category, item=item)


# Disconnect based on provider
@app.route('/disconnect')
def disconnect():
    if 'provider' in login_session:
        if login_session['provider'] == 'google':
            gdisconnect()
            del login_session['gplus_id']
            del login_session['access_token']
        if login_session['provider'] == 'facebook':
            fbdisconnect()
            del login_session['facebook_id']
        del login_session['username']
        del login_session['email']
        del login_session['picture']
        del login_session['user_id']
        del login_session['provider']
        flash("You have successfully been logged out.")
        return redirect(url_for('index'))
    else:
        flash("You were not logged in")
        return redirect(url_for('index'))


# Show about page
@app.route('/about')
def about():
    return render_template('about.html')


# Show contact page
@app.route('/contact')
def contact():
    return render_template('contact.html')


if __name__ == '__main__':
    app.secret_key = 'super_secret_key'
    app.run()
    app.run(host='0.0.0.0', port=3000)
