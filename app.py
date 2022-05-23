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


def get_headers(keywords: str) -> list[str]:
    ''' Splits the search term into keywords and executes queries with each of them,
        then removes repetitions from the results, returning a list of headers.
    '''
    received_keywords: list[str] = re.split(r'[/\,;!]', keywords)
   
    headers: list[str] = []
    for keyword in received_keywords: 
        titles: list[str] = ["".join(list(title)) for title in anime.get_query('title', keyword)]
        headers += titles 

    headers = list(set(headers)) 

    return headers


def get_content(keywords: str) -> list[str]:
    ''' Splits the search term into keywords and executes queries with each of them,
        then removes repetitions from the results, returning a list of contents.
    '''
    
    received_keywords: list[str] = re.split(r'[/\,;!]', keywords)
   
    contents: list[str] = []
    for keyword in received_keywords: 
        data: list[str] = ["".join(list(title)) for title in anime.get_query('desc', keyword)]
        contents += data

    contents = list(set(contents)) 

    return contents


@app.route('/', methods=['GET', 'POST'])
def index():
    
    if request.method == 'GET':
       return render_template('index.html')

    if request.method == 'POST':
        search_term:  str = request.form['searchTerm']
    
    headers = get_headers(search_term) 
    content = get_content(search_term) 
    modeled_output: list[str] = anime.model_result(content)

    data: list[dict] = [{header:modeled_output[i] for i, header in enumerate(headers)}]
    return render_template('index.html', data=data)


# Main 
# --------------------------------------------
if __name__ == '__main__':
    app.run(debug=True)
# --------------------------------------------
