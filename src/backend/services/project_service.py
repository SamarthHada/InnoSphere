from backend.repositories.project_repository import save_project, get_project_by_id

def validate_project(data):
    return data.get("title") and data.get("domain") and data.get("description")

def create_project(project):
    return save_project(project)

def update_project_status(project_id, status):
    project = get_project_by_id(project_id)
    if project:
        project.status = status
        return project
    return None
