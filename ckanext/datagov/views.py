from flask import Flask, Blueprint, render_template, send_from_>

if __name__ == '__main__':
    datagov.run(debug=True)

datagov_ifad = Blueprint("datagov", __name__)


@datagov_ifad.route('/projects/')

def projects():
      return render_template('projects/index.html')

def get_blueprints():
    return [datagov]
