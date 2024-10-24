# from ckan.lib.base import BaseController, render

from ckan.config.middleware import make_app
from ckan.common import _
from ckan.plugins import toolkit


# Define your routing
def make_route_map():
    routes = [
        (r'projects', 'ckanext_datagov.controllers:DatagovController', 'your_action'),
    ]
    return routes
