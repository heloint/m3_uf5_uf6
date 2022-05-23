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

anime: db.DB = db.DB('./db_src/source.db')

@app.route('/', methods=['GET', 'POST'])
def index():
    
    if request.method == 'GET':
       return render_template('index.html')

    if request.method == 'POST':
        search_term:  str = request.form['searchTerm']
    

    result = anime.get_query('desc', search_term) 
    modeled_output = anime.model_result(result)

    return render_template('index.html', result = modeled_output)

# Main 
# --------------------------------------------
if __name__ == '__main__':
    app.run(debug=True)
# --------------------------------------------
