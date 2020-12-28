# Import Dependencies 
from flask import Flask, render_template, redirect
from flask_pymongo import PyMongo
import scrape_mars

# 
app = Flask(__name__)

mongo = PyMongo(app, uri="mongodb://localhost:27017/mars_db")

# Creating a route that renders the index.html page 
@app.route('/')
def home():

    mars = mongo.db.mars.find_one()

    return render_template('index.html', mars=mars)

@app.route('/scrape')
def scrape():

    # Run the scrape function
    mars_data = scrape_mars.scrape_all()

    # Update the Mongo database 
    mongo.db.mars.update({}, mars_data, upsert=True)

    # Redirect back to home page
    return redirect("/")



if __name__ == "__main__":
    app.run(debug=True)