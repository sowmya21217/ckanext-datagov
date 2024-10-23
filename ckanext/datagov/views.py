from flask import Blueprint


datagov = Blueprint(
    "datagov", __name__)


def page():
    return "Hello, datagov!"


datagov.add_url_rule(
    "/datagov/page", view_func=page)


def get_blueprints():
    return [datagov]
