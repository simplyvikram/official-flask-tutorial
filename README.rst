Official tutorial from the flask site

| Line blocks are useful for addresses, 
| verse, and adornment-free lists. 
| 
| Taken from 
| http://flask.pocoo.org/docs/tutorial/#tutorial
| Also based on 
| http://flask.pocoo.org/docs/quickstart/#quickstart
| Pretty crappy tutorial combining all config and code in one file
| Uses sqlite
| Does not use sqlalchemy

------------------------------

- **In order to create the database**

 + on command shell inside the flaskr dir >> python
 + inside python shell >> from flaskr import init_db
 + inside python shell >> init_db()

----------------------------

- **To run the server**

 + on command shell >> python flaskr.py

------------------------------

| For branch - v2_with_sqlite_sqlalchemy
| used declartive extenstion of sql alchemy

------------------------------

+ **To create database**

 - on command shell inside flask dir >> python
 - inside python shell >> import database.py
 - inside python shell >> init_db()