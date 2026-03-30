from flask import request, jsonify
from backend.models.research_project import ResearchProject
from backend.services.project_service import validate_project, create_project, update_project_status

project_counter = 1

def submit_project():
    global project_counter
    data = request.json

    if not validate_project(data):
        return jsonify({"error": "Invalid project data"}), 400

    project = ResearchProject(
        project_counter,
        data["title"],
        data["domain"],
        data["description"]
    )
    project_counter += 1

    saved = create_project(project)
    print("Admin notified: New project submitted")

    return jsonify({"message": "Project submitted", "project": saved.to_dict()})

def get_project_status(project_id):
    project = update_project_status(project_id, "Approved")
    if project:
        return jsonify(project.to_dict())
    return jsonify({"error": "Not found"}), 404
