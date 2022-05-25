import utils
import sqlite3
import re
import database as db
from flask import Flask, render_template, request

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
    
    headers: list[str] = utils.get_headers(anime, search_term) 
    content: list[str] = utils.get_content(anime, search_term) 

    if not headers or not content:
        return render_template('index.html', data = [{"Ooops ... Sorry !!!":"We couldn't find anything similar to what you wanted. Please try to re-phrase your search."}])

    modeled_output: list[str] = anime.model_result(content)

    data: list[dict] = [{header:modeled_output[i] for i, header in enumerate(headers)}]
    data = utils.remove_duplicates(data)


    return render_template('index.html', data = data)


# Main 
# --------------------------------------------
if __name__ == '__main__':
    app.run(debug=True)
# --------------------------------------------
