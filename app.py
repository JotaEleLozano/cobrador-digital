
from flask import Flask, render_template, request, redirect
import sqlite3

app = Flask(__name__)

def init_db():
    with sqlite3.connect('db/database.sqlite') as conn:
        conn.execute("""CREATE TABLE IF NOT EXISTS clientes (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nombre TEXT,
            identidad TEXT,
            direccion TEXT,
            negocio TEXT
        )""")
        conn.execute("""CREATE TABLE IF NOT EXISTS deudas (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            cliente_id INTEGER,
            monto REAL,
            costo REAL,
            utilidad REAL,
            ebidta REAL,
            FOREIGN KEY(cliente_id) REFERENCES clientes(id)
        )""")
        conn.commit()

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/cliente', methods=['GET', 'POST'])
def add_cliente():
    if request.method == 'POST':
        nombre = request.form['nombre']
        identidad = request.form['identidad']
        direccion = request.form['direccion']
        negocio = request.form['negocio']
        with sqlite3.connect('db/database.sqlite') as conn:
            conn.execute("INSERT INTO clientes (nombre, identidad, direccion, negocio) VALUES (?, ?, ?, ?)", 
                         (nombre, identidad, direccion, negocio))
            conn.commit()
        return redirect('/')
    return render_template('add_cliente.html')

if __name__ == '__main__':
    init_db()
    app.run(debug=True)
