from flask import Flask
from backend.controllers.project_controller import submit_project, get_project_status

app = Flask(__name__)

app.add_url_rule('/api/projects/submit', 'submit_project', submit_project, methods=['POST'])
app.add_url_rule('/api/projects/status/<int:project_id>', 'get_project_status', get_project_status, methods=['GET'])

if __name__ == "__main__":
    app.run(debug=True)
