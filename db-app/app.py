from flask import Flask, render_template, request, redirect, url_for
import mysql.connector
from mysql.connector import Error

app = Flask(__name__)

def read_secret(secret_path):
    with open(secret_path, 'r') as secret_file:
        return secret_file.read().strip()

def create_connection():
    username = read_secret('/etc/mysql-secret/username')
    password = read_secret('/etc/mysql-secret/password')
    hostname = read_secret('/etc/mysql-secret/hostname')
    db_name = read_secret('/etc/mysql-secret/db_name')
    try:
        connection = mysql.connector.connect(
            host=hostname,
            database=db_name,
            user=username,
            password=password
        )
        return connection
    except Error as e:
        print("Error while connecting to MySQL", e)
        return None


@app.route('/', methods=['GET'])
def index():
    connection = create_connection()
    if connection:
        cursor = connection.cursor()
        cursor.execute("SELECT * FROM goals")
        goals = cursor.fetchall()
        cursor.close()
        connection.close()
        return render_template('index.html', goals=goals)
    else:
        return "Error connecting to the MySQL database", 500

@app.route('/add_goal', methods=['POST'])
def add_goal():
    goal_name = request.form.get('goal_name')
    if goal_name:
        connection = create_connection()
        if connection:
            cursor = connection.cursor()
            cursor.execute("INSERT INTO goals (goal_name) VALUES (%s)", (goal_name,))
            connection.commit()
            cursor.close()
            connection.close()
    return redirect(url_for('index'))

@app.route('/remove_goal', methods=['POST'])
def remove_goal():
    goal_id = request.form.get('goal_id')
    if goal_id:
        connection = create_connection()
        if connection:
            cursor = connection.cursor()
            cursor.execute("DELETE FROM goals WHERE id = %s", (goal_id,))
            connection.commit()
            cursor.close()
            connection.close()
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)

