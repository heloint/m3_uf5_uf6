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

        return render_template('index.html', name = search_term) 

# Main 
# --------------------------------------------
if __name__ == '__main__':
    app.run(debug=True)
# --------------------------------------------

# test = anime.get_query('select desc from animes;')
# 
# for row in test:
#     word_list: list[str] = str(row).split(' ') 
#     for i, word in enumerate(word_list):
#         paragraph: list[str] = [for i in range(0,len(word_list),10)]
# 
# 
#         result_rows = [result_spaces[i:i + len(data_spaces)] for i in range(0,len(result_spaces),len(data_spaces))]
