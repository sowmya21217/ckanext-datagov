import logging
from flask import Blueprint, render_template, redirect, abort, jsonify
import ckan.plugins as p
from ckan.plugins.toolkit import config

# Initialize logging
log = logging.getLogger(__name__)

# Create a Blueprint for your datagov routes
datagov_bp = Blueprint('datagov', __name__)

def projects():
    """
    Render the projects page.
    """
    try:
        return render_template('projects/index.html')  # Path to your template
    except Exception as e:
        log.error(f"Error rendering projects page: {e}")
        abort(500, "Internal Server Error: Unable to render the projects page.")

def redirect_homepage():
    """
    Redirect to the CKAN dataset homepage.
    """
    CKAN_SITE_URL = config.get("ckan.site_url")
    return redirect(f"{CKAN_SITE_URL}/dataset/", code=302)

def get_popular_count():
    """
    Return a JSON response indicating a lack of functionality.
    """
    return jsonify({"error": "Functionality to retrieve popular package counts is not implemented."}), 501

# Define your routes
datagov_bp.add_url_rule('/projects/', view_func=projects)
datagov_bp.add_url_rule('/', view_func=redirect_homepage)  # Redirect to homepage
datagov_bp.add_url_rule("/datagov/get-popular-count", methods=['GET'], view_func=get_popular_count)

# Function to return blueprints
def get_blueprints():
    return [datagov_bp]  # Return the list of blueprints
