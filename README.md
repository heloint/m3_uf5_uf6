# Anime Searcher

Version compatibility: > Python 3.8 
Requirements: Flask (There can be more if using older versions of Python, but most of them already should come included.)

- Mini web app project for UF5 and UF6 of Module 3. - Programming
- Built in Python with Flask framework, using SQLite3 database and the holy trinity of HTML, CSS and a hint of JS.

NOTE: Before using, make sure the state of ./db_src/animes_src.csv and ./db_src/source.db,
otherwise there will be some issue with the database, which is the main thing . . .

Before use: If the ./db_src/source.db is missing, you can rebuild it by running directly the ./create_db.py.

---


# The theme

"Anime searcher" is a simple web application where the user
can search for animes and the app returns the description of it.

---


# Contents of directories and files

- db_src: Dir, that contains the database related source files.
- statis: Dir, that constains the Javascript, CSS and image source files.
- templates: Dir, that contains the HTML templates used by Jinja2.
- create_db.py: Program that creates and manages the databases.
- app.py: The main file of the web app.

---
