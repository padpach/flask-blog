#Controlador del Blog
#blog.py - controller

from flask import Flask, render_template, request, session, \
	flash, redirect, url_for, g
import sqlite3

#configuracion
DATABASE = 'blog.db'
app = 	Flask(__name__)
USERNAME = 'admin'
PASSWORD = 'admin'
SECRET_KEY = '\xcd~\x1d\x128\xf7p\x0cZ\xe0\x00>\x85_\x82\xa7|P,\xafE\xfe\xf6w'


#jala la configuracion buscando por Variables Mayusculas
app.config.from_object(__name__)

#nos conectamos a la base de datos en sqlite3
def connect_db():
	return sqlite3.connect(app.config['DATABASE'])


@app.route('/', methods=['GET', 'POST'])
def login():
	error = None
	if request.method == 'POST':
		if request.form['username'] != app.config['USERNAME'] or \
			request.form['password'] != app.config['PASSWORD']:
			error = 'Credenciales Invalidas. Intente de nuevo.'
		else:
			session['logged_in'] = True
			return redirect(url_for('main'))
	return render_template('login.html', error=error)

@app.route('/logout')
def logout():
	session.pop('logged_in', None)
	flash('Haz salido de tu session correctamente!')
	return redirect(url_for('login'))


@app.route('/main')
def main():
	return render_template('main.html')

if __name__ == '__main__':
	app.run(debug=True)

