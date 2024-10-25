from flask import Blueprint, render_template


datagov = Blueprint("datagov", __name__)

def projects():
    return render_template("projects.html")

datagov.add_url_rule("/projects", view_func=projects)


def get_blueprints():
    return [datagov]
