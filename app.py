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
    
    received_input: list[str] = re.split(r'[/\,;!]', search_term)

    headers: list[str] = ["".join(list(title)) for title in anime.get_query('title', search_term)]
    content: list[tuple] = anime.get_query('desc', search_term) 
    modeled_output: str = anime.model_result(content)

    data: list[dict] = [{header:modeled_output[i] for i, header in enumerate(headers)}]
    return render_template('index.html', data=data)
#     return " ".join(received_input)

# Main 
# --------------------------------------------
if __name__ == '__main__':
    app.run(debug=True)
# --------------------------------------------
