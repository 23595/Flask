from flask import Flask, g
import sqlite3

DATABASE = 'nz_birds.db'

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


@app.route('/')
def home():
    #home page - IDs, common names, and status
    sql = '''   SELECT bird_id, common_name, Status.status
                FROM Birds2
                JOIN Status ON Status.statusID=Birds2.status;'''
    results = query_db(sql)
    return str(results)

@app.route('/bird/<int:id>')
def bird(id):
    #Give one bird's info based on ID
    sql = '''   SELECT * FROM Birds2
                JOIN Status ON Status.statusID=Birds2.status
                WHERE Birds2.bird_id = ?;'''
    result = query_db(sql,(id,))
    return str(result)

if __name__ == "__main__":
    app.run(debug=True)