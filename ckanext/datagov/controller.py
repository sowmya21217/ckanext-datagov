# ckanext-datagov/ckanext/datagov/controller.py

from ckan.lib.base import BaseController, render

class DatagovController(BaseController):
    def index(self):
        context = {
            'site_title': 'Open Data Portal',  # Dynamic site title
            'header_text': 'Welcome to Your Data Portal',  # Dynamic header text
        }
        return render('datagov/templates/projects/index.html', extra_vars=context)
