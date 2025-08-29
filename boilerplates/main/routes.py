from flask import Blueprint, render_template

"""
Routes for flask app
"""

routes = Blueprint("routes", "routes")

routes.route("/")
def home():
    return render_template('base.html')