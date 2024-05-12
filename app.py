from flask import Flask, render_template, request
import sqlite3

app = Flask(__name__)

# Function to create the database table
def create_table():
    conn = sqlite3.connect('user_data.db')
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS users
                 (id INTEGER PRIMARY KEY AUTOINCREMENT,
                  name TEXT NOT NULL,
                  country TEXT NOT NULL,
                  age INTEGER NOT NULL)''')
    conn.commit()
    conn.close()

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        name = request.form['name']
        country = request.form['country']
        age = request.form['age']

        # Insert user data into the database
        conn = sqlite3.connect('user_data.db')
        c = conn.cursor()

        c.execute('''CREATE TABLE IF NOT EXISTS users
                 (id INTEGER PRIMARY KEY AUTOINCREMENT,
                  name TEXT NOT NULL,
                  country TEXT NOT NULL,
                  age INTEGER NOT NULL)''')

        c.execute("INSERT INTO users (name, country, age) VALUES (?, ?, ?)", (name, country, age))
        conn.commit()
        #conn.close()
        # Retrieve all records from the database
        conn = sqlite3.connect('user_data.db')
        c = conn.cursor()
        c.execute("SELECT * FROM users")
        records = c.fetchall()
        conn.close()

        return render_template('index.html', records=records)
        # return render_template('index.html', name=name, country=country, age=age)
    
    return render_template('index.html')

if __name__ == '__main__':
    create_table()  # Create the database table if it doesn't exist
    app.run()