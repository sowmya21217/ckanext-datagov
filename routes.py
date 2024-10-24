from ckan.lib.base import BaseController, render

class DatagovController(BaseController):
    def index(self):
        return render('datagov/templates/projects/index.html')  # Render your custom homepage

# Define your routing
def make_map():
    map = make_map()
    map.connect('datagov_projects', '/projects', controller='ckanext.datagov.controller.DatagovController', action='index')
    return map
