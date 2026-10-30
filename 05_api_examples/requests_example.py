import requests

base_url = "http://127.0.0.1:5000/students/"

student_id = 1
response_json = requests.get(f"{base_url}{student_id}", headers={"Accept": "application/json"})

if response_json.status_code == 200:
    print("JSON-Antwort:")
    print(response_json.json())
else:
    print("Fehler bei der JSON-Antwort:", response_json.status_code)

response_html = requests.get(f"{base_url}{student_id}", headers={"Accept": "text/html"})

if response_html.status_code == 200:
    print("HTML-Antwort:")
    print(response_html.text) 
else:
    print("Fehler bei der HTML-Antwort:", response_html.status_code)

new_student = {
    "name": "Lisa Schmidt",
    "email": "lisa@example.com"
}

response_post = requests.post(f"http://127.0.0.1:5000/students", json=new_student)

if response_post.status_code == 201:
    print("Neuer Student hinzugefügt:")
    print(response_post.json())
else:
    print("Fehler beim Hinzufügen des Studenten:", response_post.status_code)
