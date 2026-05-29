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
    return "Employee API is Running Successfully"


@app.route('/employees', methods=['POST'])
def add_employee():

    data = request.get_json()

    cur.execute(
        "INSERT INTO employees (name, role, salary) VALUES (%s, %s, %s)",
        (data['name'], data['role'], data['salary'])
    )

    conn.commit()

    return jsonify({"message": "Employee Added Successfully"}), 201



@app.route('/employees', methods=['GET'])
def get_employees():

    cur.execute("SELECT * FROM employees")
    rows = cur.fetchall()

    employees = []

    for row in rows:
        employees.append({
            "id": row[0],
            "name": row[1],
            "role": row[2],
            "salary": row[3]
        })

    return jsonify(employees), 200



@app.route('/employees/<int:id>', methods=['PUT'])
def update_employee(id):

    data = request.get_json()

    cur.execute(
        """
        UPDATE employees
        SET name=%s, role=%s, salary=%s
        WHERE id=%s
        """,
        (data['name'], data['role'], data['salary'], id)
    )

    conn.commit()

    return jsonify({"message": "Employee Updated Successfully"}), 200



@app.route('/employees/<int:id>', methods=['DELETE'])
def delete_employee(id):

    cur.execute(
        "DELETE FROM employees WHERE id=%s",
        (id,)
    )

    conn.commit()

    return jsonify({"message": "Employee Deleted Successfully"}), 200



if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
