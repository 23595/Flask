from flask import Flask, g, render_template
import sqlite3
import random

DATABASE = 'spish.db'


#initialise app
app = Flask(__name__)

def get_db():
    db = getattr(g, '_database', None)
    if db is None:
        db = g._database = sqlite3.connect(DATABASE)
    return db

@app.teardown_appcontext
def close_connection(exception):
    db = getattr(g, '_database', None)
    if db is not None:
        db.close()

def query_db(query, args=(), one=False):
    cur = get_db().execute(query, args)
    rv = cur.fetchall()
    cur.close()
    return (rv[0] if rv else None) if one else rv

#Routes for different pages:
@app.route('/')
def home():
    return render_template("index.html")
@app.route('/foods')
def foods():
    return render_template("food.html")
@app.route('/countries')
def countries():
    return render_template("countries.html")

#
@app.route('/word/<int:id>')
def word(id):
    #Ask for a defenition of a random word
    id = random.randint(0,849)
    sql = '''   SELECT * FROM Birds2
                JOIN Status ON Status.statusID=Birds2.status
                WHERE Birds2.bird_id = ?;'''
    #result = query_db(sql, (id,))
    #return str(result)

if __name__ == "__main__":
    app.run(debug=True)