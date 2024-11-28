from flask import Flask, Blueprint, render_template


datagov = Blueprint("datagov", __name__)


def projects():
    country_projects = [
        {
            'title': 'Project A',
            'description': 'Description for Project A',
            'latitude': 34.0522,  # Latitude of the location
            'longitude': -118.2437,  # Longitude of the location
            'url': 'https://example.com/project-a'
        },
        {
            'title': 'Project B',
            'description': 'Description for Project B',
            'latitude': 51.5074,
            'longitude': -0.1278,
            'url': 'https://example.com/project-b'
        },
        {
            'title': 'Project C',
            'description': 'Description for Project C',
            'latitude': 48.8566,
            'longitude': 2.3522,
            'url': 'https://example.com/project-c'
        }
    ]

    return render_template("projects/index.html", datasets=country_projects)

datagov.add_url_rule("/datagov/projects",view_func=projects)

def get_blueprints():
     return [datagov]
