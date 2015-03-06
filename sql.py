#Sql del Blog

import sqlite3

#creamos la base de datos
with sqlite3.connect("blog.db") as connection:
	c = connection.cursor()
	c.execute("""CREATE TABLE posts(title TEXT, post TEXT)""")
	c.execute('INSERT INTO posts VALUES("Excelente", "YO estoy Ok.")')
	c.execute('INSERT INTO posts VALUES("A toda madre", "YO estoy a toda madre.")')
	c.execute('INSERT INTO posts VALUES("Ufa Gallo!", "YO Pufffff.")')
	c.execute('INSERT INTO posts VALUES("Very Good", "Fine Fine.")')
	