from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy # instantiate database object # import class

application = Flask(__name__)

application.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://user:pass@host.domain.com/mydb'
application.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(application) # instantiate database object #interface with flask app itself

class Comments(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(20))
    comment = db.Column(db.String(1000))

db.create_all()
@application.route('/')
def index():
    result = Comments.query.all() # use the comments class
    #result = Comments.query.filter_by(name='Ruan')
    counts = Comments.query.count()
    return render_template('index.html', result=result, counts=counts)

@application.route('/sign')
def sign():
    return render_template('sign.html')

@application.route('/search')
def search():
    return render_template('search.html')


@application.route('/process', methods=['POST'])
def process():
    name = request.form['name']
    comment = request.form['comment']

    signature = Comments(name=name, comment=comment)      # instantiate an object. signature object, from comments class
    db.session.add(signature)                 # add a row to database
    db.session.commit()                     # save changes

    return redirect(url_for('index'))
    return render_template('index.html', name=name, comment=comment)

@application.route('/searchresults', methods=['GET', 'POST'])
def searchresults():
    name = request.form['name']
    result = Comments.query.filter_by(name=name)
    return render_template('index.html', result=result)

if __name__ == '__main__':
    application.run()
