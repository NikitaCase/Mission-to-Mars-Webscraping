# Import Dependencies 
import pandas as pd 
import requests 
from bs4 import BeautifulSoup as bs 
import json
from splinter import Browser

def scrape_all():

    # Creating a path for browser used to scrape dynamic website 
    chrome_path = 'driver/chromedriver.exe' 
    executable_path = {'executable_path' : chrome_path}
    browser = Browser('chrome', **executable_path, headless=False)

    # Opening news section in browser
    news_url = 'https://mars.nasa.gov/news/'
    browser.visit(news_url)

    # Passing the html page to beautiful soup 
    news_html = browser.html
    news = bs(news_html, 'html.parser')


# Finding the first title and paragraph on the page (lastest news) & assigning variable names 
    news_title = news.find_all('div', class_='content_title')[1].text
    news_p = news.find('div', class_='article_teaser_body').text

# Opening jet propulsion lab website
    jpl_url = 'https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars'
    browser.visit(jpl_url)

# Converting html page to a beautiful soup object 
    jpl_html = browser.html
    jpl = bs(jpl_html, 'html.parser')


# extracting the url for the featured image
    site_dir = jpl_url.split('?')[0]
    rel_image_path = jpl.find('article', class_='carousel_item')['style']
    rel_image_path = rel_image_path.split('spaceimages/')[1].split("'")[0]
    featured_image_url = site_dir+rel_image_path


#Opening Mars Facts url 
    facts_url ='https://space-facts.com/mars/'
    browser.visit(facts_url)

# Converting html page to a beuatiful soup object
    facts_html = browser.html
    mars_facts = bs(facts_html, 'html.parser')


# Scraping the fact table and making it tidy 
    mars_facts_df = (fact_table_html[0].rename(columns={0:'Description', 1:'Mars'}))
    mars_facts_df.set_index("Description", inplace=True)
# Creating an html table to render in the index.html page
    mars_facts_html = mars_facts_df.to_html()


#Opening USGS website 
    usgs_url = 'https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars'
    browser.visit(usgs_url)

# Creating a list of dictionaries to store hemisphere images and titles
    hemisphere_image_urls = [
        {"title": "Valles Marineris Hemisphere", "img_url": "https://astropedia.astrogeology.usgs.gov/download/Mars/Viking/valles_marineris_enhanced.tif"},
        {"title": "Cerberus Hemisphere", "img_url": "https://astropedia.astrogeology.usgs.gov/download/Mars/Viking/cerberus_enhanced.tif"},
        {"title": "Schiaparelli Hemisphere", "img_url": "https://astropedia.astrogeology.usgs.gov/download/Mars/Viking/schiaparelli_enhanced.tif"},
        {"title": "Syrtis Major Hemisphere", "img_url": "https://astropedia.astrogeology.usgs.gov/download/Mars/Viking/syrtis_major_enhanced.tif"},
    ]
