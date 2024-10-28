from flask import Blueprint, render_template


datagov = Blueprint("datagov", __name__)


@datagov.route('/projects')

def projects():
    return render_template('projects/index.html')


def get_blueprints():
    return [datagov]
