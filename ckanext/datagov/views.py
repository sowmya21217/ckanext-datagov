from flask import Flask, Blueprint, render_template
import csv
import os

datagov = Blueprint('datagov', __name__)

def read_csv():
    projects = []
    csv_file_path = os.path.join(os.path.dirname(__file__), 'projects.csv')

    try:
        # Open and read the CSV file
        with open(csv_file_path, mode='r', encoding='utf-8') as file:
            reader = csv.DictReader(file)
            for row in reader:
                projects.append(row)
    except FileNotFoundError:
        print(f"Error: The file {csv_file_path} was not found.")
    except Exception as e:
        print(f"An error occurred: {e}")

    return projects


def projects():
    country_projects = read_csv()

    # Calculate total value and project count
#    total_value = sum(float(project['value'] or 0) for project in country_projects)
#   project_count = len(country_projects)

    return render_template('projects/index.html', datasets=country_projects)

datagov.add_url_rule('/datagov/projects',view_func=projects)

def get_blueprints():
     return [datagov]
