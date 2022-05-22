import sqlite3
import re
import create_db as db
from pathlib import Path
from flask import Flask, Response, render_template, jsonify, request

# Flask init
# --------------------------------------------
module_name: str = __name__
app: Flask = Flask(module_name)
# --------------------------------------------

anime = db.DB('source.db')




@app.route('/', methods=['GET', 'POST'])
def index():
    
    if request.method == 'GET':
       return render_template('index.html')

    if request.method == 'POST':
        search_term:  str = request.form['searchTerm']

#     con = sqlite3.connect("source.db", check_same_thread=False)
#     cursor = con.cursor()
#     cursor.execute('desc', search_term) 
    result = anime.get_query('desc', search_term) 
#     result = cursor.fetchall()
    return "</br></br>".join(["".join(list(row)) for row in result]) 

# Main 
# --------------------------------------------
if __name__ == '__main__':
    app.run(debug=True)
# --------------------------------------------


