from project.models import Project


def ProjectMapper(project: Project):
    return {
        'id':project.id,
        'name': project.name,
        'create_date': project.create_date,
        'autherID': project.autherID
    }

