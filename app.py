# Import Dependencies 
from flask import Flask, render_template, redirect
import pymongo
import scrape_mars


# 
app = Flask(__name__)

# Creating a route that renders the index.html page 
@app.route('/')
def index():
    return render_template('index.html', mars=mars)


if __name__ == "__main__":
    app.run(debug=True)