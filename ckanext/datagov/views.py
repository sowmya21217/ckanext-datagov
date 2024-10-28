from flask import Blueprint, render_template, send_from_directory


datagov = Blueprint("datagov", __name__)


@datagov.route('/projects')

def projects():
    try:
      return send_from_directory('templates/projects', 'index.html')
    
    except Exception as e:
        # Handle the error gracefully, perhaps log it or return a different page
        abort(404)

def get_blueprints():
    return [datagov]
