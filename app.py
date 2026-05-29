from flask import Flask, request, jsonify
import psycopg2
import time

app = Flask(__name__)

time.sleep(5)

conn = psycopg2.connect(
    host="db",
    database="employee_db",
    user="postgres",
    password="postgres"
)

cur = conn.cursor()

cur.execute("""
CREATE TABLE IF NOT EXISTS employees (
    id SERIAL PRIMARY KEY,
    name VARCHAR(100),
    role VARCHAR(100),
    salary INTEGER
)
""")

conn.commit()

@app.route('/')
def home():
    return "Employee API Working"

@app.route('/employees', methods=['POST'])
def add():
    data = request.get_json()

    cur.execute(
        "INSERT INTO employees (name, role, salary) VALUES (%s, %s, %s)",
        (data['name'], data['role'], data['salary'])
    )

    conn.commit()
    return jsonify({"message": "Added"})

@app.route('/employees', methods=['GET'])
def get():
    cur.execute("SELECT * FROM employees")
    rows = cur.fetchall()

    result = []
    for r in rows:
        result.append({"id": r[0], "name": r[1], "role": r[2], "salary": r[3]})

    return jsonify(result)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
