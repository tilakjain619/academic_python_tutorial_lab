from flask import Flask, render_template, request, redirect, url_for
import sqlite3
import os

app = Flask(__name__)

DATABASE = 'database.db'

def get_db():
    conn = sqlite3.connect(DATABASE)
    conn.row_factory = sqlite3.Row
    return conn

def init_db():
    if not os.path.exists(DATABASE):
        conn = get_db()
        with app.open_resource('schema.sql', mode='r') as f:
            conn.cursor().executescript(f.read())
        conn.commit()
        conn.close()
        print("Database initialized.")

@app.cli.command('initdb')
def initdb_command():
    """Initialize the database from schema.sql."""
    init_db()
    print('Initialized the database.')

@app.route('/')
def index():
    conn = get_db()
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM tasks')
    tasks = cursor.fetchall()
    conn.close()
    return render_template('index.html', tasks=tasks)

@app.route('/add', methods=['GET', 'POST'])
def add_task():
    if request.method == 'POST':
        title = request.form['title']
        description = request.form['description']
        due_date = request.form['due_date']
        priority = request.form['priority']
        completed = request.form.get('completed') == 'on'
        conn = get_db()
        cursor = conn.cursor()
        cursor.execute('''
            INSERT INTO tasks (title, description, due_date, priority, completed)
            VALUES (?, ?, ?, ?, ?)
        ''', (title, description, due_date, priority, completed))
        conn.commit()
        conn.close()
        return redirect(url_for('index'))
    return render_template('add_task.html')

@app.route('/edit/<int:id>', methods=['GET', 'POST'])
def edit_task(id):
    conn = get_db()
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM tasks WHERE id = ?', (id,))
    task = cursor.fetchone()
    if request.method == 'POST':
        title = request.form['title']
        description = request.form['description']
        due_date = request.form['due_date']
        priority = request.form['priority']
        completed = request.form.get('completed') == 'on'
        cursor.execute('''
            UPDATE tasks SET title = ?, description = ?, due_date = ?, priority = ?, completed = ?
            WHERE id = ?
        ''', (title, description, due_date, priority, completed, id))
        conn.commit()
        conn.close()
        return redirect(url_for('index'))
    conn.close()
    return render_template('edit_task.html', task=task)

@app.route('/delete/<int:id>')
def delete_task(id):
    conn = get_db()
    cursor = conn.cursor()
    cursor.execute('DELETE FROM tasks WHERE id = ?', (id,))
    conn.commit()
    conn.close()
    return redirect(url_for('index'))

if __name__ == '__main__':
    init_db()  # Optional: auto-create DB when running app directly
    app.run(debug=True)
