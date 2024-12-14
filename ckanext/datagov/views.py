from flask import Flask, Blueprint, render_template
import csv

datagov = Blueprint('datagov', __name__)

def read_csv():
    projects = []
    with open('projects.csv', mode='r', encoding='utf-8') as file:
        reader = csv.DictReader(file)
        for row in reader:
            projects.append(row)
    return projects


def projects():
    country_projects = read_csv()
    return render_template('projects/index.html', datasets=country_projects)

datagov.add_url_rule('/datagov/projects',view_func=projects)

def get_blueprints():
     return [datagov]
