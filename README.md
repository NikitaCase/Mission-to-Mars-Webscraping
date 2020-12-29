# Mission to Mars

<br>
For this assignment, several webpages were scraped to produce a dictionary of content used to make a Mongo Database and a Flask Application that renders an html file populated with content from the scrape
<br> 
**Files**
<br>
- mission_to_mars.ipynb<br>
Jupyter notebook where code is run line by line to show that it's scraping the websites. Chromedriver is used to access the websites for scraping. 
<br>
<br>
- scrape_mars.py<br>
Contains a function which opens a browser, scrapes info from the four websites (see below), creates a dictionary with all the scraped information
<br>
<br>
- app.py<br>
Smallest file that took the longest! Flask app that has a home route which launches the index.html template and a scrape route which runs the scrape_mars file, writes the resulting dictionary to a pymongo database (will upsert data when rerun), redirects the user to the homepage which loads the data from the pymongo database
<br>
<br>
- index.html<br>
  An html page where data is displayed
  


<br>
<br>
**Technology used**
<br>
- Python, Jupyter notebooks
- Mongo and PyMongo 
- Flask
- Bootstrap 
 
<br>
<br>

<details>
  <summary>Websites Scraped</summary>

    * Nasa Science - Mars Exploration Program
    For the space news headline and title text
    https://mars.nasa.gov/news/

    * NASA Jet Propulsion Laboratory  -
    For the featured image section 
    https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars

    * Space Facts - Chris Jones
    For the mars facts table - taken directly from the Mars PLanet Profile table
    https://space-facts.com/mars/

    * USGS Astropedia
    For hemisphere images and their names
    https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars

</details>
<br><br>

Screenshot of the app.py running 

![index.html](screenshot.png)


