import sqlite3
from pathlib import Path
from flask import Flask, Response, render_template, jsonify, request

# Flask init
# --------------------------------------------
module_name: str = __name__
app: Flask = Flask(module_name)
# --------------------------------------------

@app.route('/', methods=['GET', 'POST'])
def index():
    
    if request.method == 'GET':
       return render_template('index.html')

    if request.method == 'POST':
        search_term:  str = request.form['searchTerm']

    return f"{search_term}"

# Main 
# --------------------------------------------
if __name__ == '__main__':
    app.run(debug=True)
# --------------------------------------------
