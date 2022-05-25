from flask import Blueprint, render_template, request

views = Blueprint('views', __name__)


@views.route('/under-construction')
def under_construction_message():
    return render_template("landing.html")

@views.route('/')
def home():
    return render_template("home.html")

@views.route('/about-us')
def about_us():
    return render_template("about.html")

@views.route('/contact-us')
def contact_us():
    return render_template("contact.html")

@views.route('/help-out')
def help_out():
    return render_template("help.html")

@views.route('/donate')
def donate():
    return render_template("donate.html")