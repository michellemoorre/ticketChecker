from flask import Flask, render_template
import sqlite3

app = Flask(__name__)

@app.route('/<id>')
def guest_view(id):
	db = sqlite3.connect('tickets.db')
	db_cursor = db.cursor()
	db_cursor.execute(f"SELECT * FROM users WHERE id='{id}';")
	records = list(db_cursor.fetchall()[0])
	return render_template('person.html', data=records)

if __name__=='__main__':
	app.run(host='0.0.0.0', port=5000)