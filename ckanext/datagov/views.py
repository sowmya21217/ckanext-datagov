from flask import Flask, Blueprint, render_template


datagov = Blueprint("datagov", __name__)


def projects():
     return render_template("index.html")

datagov.add_url_rule("/datagov/projects",view_func=projects)

def get_blueprints():
     return [datagov]
