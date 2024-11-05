from flask import Flask, Blueprint, render_template

if __name__ == '__main__':
    datagov.run(debug=True)

datagov = Blueprint("datagov", __name__)


@datagov.route('/projects/')

def projects():
      return render_template('projects/index.html')

def get_blueprints():
    return [datagov]
