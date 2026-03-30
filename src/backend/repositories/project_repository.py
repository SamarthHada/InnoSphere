projects = []

def save_project(project):
    projects.append(project)
    return project

def get_project_by_id(project_id):
    for project in projects:
        if project.project_id == project_id:
            return project
    return None
