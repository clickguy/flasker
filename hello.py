from distutils.command.install_egg_info import safe_name
from flask import Flask, render_template

# Create a flask instance
app = Flask(__name__)

# Create a decorator route

# @app.route('/')
# def index():
#     return '<h1>Hello World!</h1>'

# HTML variable FILTERS
# safe
# capitalize
# lower
# upper
# trim
# striptags


@app.route('/')
def index():
    first_name = "John"
    stuff = "This is <stong>bold</strong> text"
    favorite_pizzas = ["Pepperoni", "Cheese", "Mushrooms", 41]

    return render_template("index.html",
                           first_name=first_name,
                           stuff=stuff,
                           favorite_pizzas=favorite_pizzas
                           )

# localhost:5000/user/bob


@app.route('/user/<name>')
def user(name):
    return render_template("user.html", user_name=name)


# Custom error pages

# Invalid URL (404)
@app.errorhandler(404)
def page_not_found(e):
    return render_template("404.html"), 404

# Invalid Server Error (500)


@app.errorhandler(500)
def internal_server_error(e):
    return render_template("500.html"), 500
