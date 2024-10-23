from ckan.lib.base import BaseController, render

class DatagovController(BaseController):
    def index(self):
        return render('datagov/home.html')  # Render your custom homepage

# Define your routing
def make_map():
    map = make_map()
    map.connect('datagov_home', '/', controller='ckanext.datagov.controller.DatagovController', action='index')
    return map
