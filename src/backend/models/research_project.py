class ResearchProject:
    def __init__(self, project_id, title, domain, description):
        self.project_id = project_id
        self.title = title
        self.domain = domain
        self.description = description
        self.status = "Pending"

    def to_dict(self):
        return {
            "project_id": self.project_id,
            "title": self.title,
            "domain": self.domain,
            "description": self.description,
            "status": self.status
        }
