from flask import Flask, request, Response, render_template_string
from flask_accept import accept
import json

app = Flask(__name__)

students = {
    1: {"id": 1, "name": "Max Mustermann", "email": "max@example.com"},
    2: {"id": 2, "name": "Anna Müller", "email": "anna@example.com"},
}

html_template = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Student {{ student.id }}</title>
</head>
<body>
    <h1>Student {{ student.id }}</h1>
    <p>Name: {{ student.name }}</p>
    <p>Email: {{ student.email }}</p>
</body>
</html>
"""

@app.route('/students/<int:student_id>', methods=['GET'])
@accept('text/html')
def get_student(student_id):
    student = students.get(student_id)
    if student:
        return render_template_string(html_template, student=student)
    return "Student not found", 404

@app.route('/students/<int:student_id>', methods=['GET'])
@get_student.support('application/json', '*/*')   # '*/*': Clients ohne bestimmten Accept-Header (z.B. curl, Postman) bekommen JSON
def get_student_json(student_id):
    student = students.get(student_id)
    if student:
        return Response(json.dumps(student), mimetype='application/json', status=200)
    return Response(json.dumps({"error": "Student not found"}), mimetype='application/json', status=404)

@app.route('/students', methods=['POST'])
def add_student():
    try:
        data = request.json
        new_id = max(students.keys()) + 1
        student = {"id": new_id, "name": data["name"], "email": data["email"]}
        students[new_id] = student
        return Response(json.dumps(student), mimetype='application/json', status=201)
    except (KeyError, TypeError):
        return Response(json.dumps({"error": "Invalid input"}), mimetype='application/json', status=400)

if __name__ == '__main__':
    app.run(debug=True)
