from flask import Blueprint, render_template

homepage_bp = Blueprint('utama', __name__)

@homepage_bp.route('/')
def homepage():
    return render_template("homepage.html")