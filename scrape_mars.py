# Import Dependencies 
import pandas as pd 
import requests 
from bs4 import BeautifulSoup as bs 
import json
from splinter import Browser

#creating a dictionary to hold all mars facts
mars = {}

def scrape_all():

# Creating a path for browser used to scrape dynamic website 
    chrome_path = 'C:/Users/guyan/bin/chromedriver.exe' 
    executable_path = {'executable_path' : chrome_path}
    browser = Browser('chrome', **executable_path, headless=False)



# Opening news section in browser
    news_url = 'https://mars.nasa.gov/news/'
    browser.visit(news_url)

# Passing the html page to beautiful soup 
    news_html = browser.html
    news = bs(news_html, 'html.parser')

# Finding the first title and paragraph on the page 
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
    fact_table_html = pd.read_html('https://space-facts.com/mars/')
    mars_facts_df = (fact_table_html[0].rename(columns={0:'Description', 1:'Mars'}))
    mars_facts_df.set_index("Description", inplace=True)
# Creating an html table to render in the index.html page
    mars_facts_html = mars_facts_df.to_html()
    


#Opening USGS website 
    usgs_url = 'https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars'
    browser.visit(usgs_url)

# Converting html page to a beautiful soup object
    usgs_html = browser.html
    usgs = bs(usgs_html, 'html.parser')

# Scraping the title and image of each hemisphere, saving each in its own dictionary, within a list
    hemisphere_image_urls = []
    usgs_main = 'https://astrogeology.usgs.gov'

    hemispheres = usgs.find_all('div', class_='item')
    for hemi in hemispheres:
        sphere = {}

        title = hemi.find('h3').text

        image_path = hemi.find('a', class_='itemLink product-item')['href']
        browser.visit(usgs_main + image_path)

        image_html = browser.html
        image = bs(image_html, 'html.parser')
        img_url = usgs_main + image.find('img', class_='wide-image')['src']

        sphere['title'] = title
        sphere['img_url'] = img_url
    
        hemisphere_image_urls.append(sphere)
    


# Adding all variables needed to a dictionary
    mars = {}
    mars['news_title'] = news_title
    mars['news_p'] = news_p 
    mars['featured_image_url'] = featured_image_url
    mars['mars_facts_html'] = mars_facts_html
    mars['hemisphere_image_urls'] = hemisphere_image_urls



    browser.quit()
    return mars

