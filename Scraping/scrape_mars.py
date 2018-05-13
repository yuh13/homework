

#import dependencies
from flask import Flask, render_template
import time
from bs4 import BeautifulSoup
import requests
import os
import pandas as pd
from splinter import Browser

app = Flask(__name__)

@app.route("/")


@app.route("/scrape")

def scrape():
	###Mars NASA news
	#url of NASA Mars Site
	url = "https://mars.nasa.gov/news/?page=0&per_page=40&order=publish_date+desc%2Ccreated_at+desc&search=&category=19%2C165%2C184%2C204&blank_scope=Latest"
	html = requests.get(url)
	#Get HTML as text using BeautifulSoup
	soup = BeautifulSoup(html.text, 'html.parser')
	#Find div with both news title and paragraph text
	div = soup.body.find('div', class_='slide')
	#Extract text from anchor tag
	news_title = div.find('div', class_='content_title').find('a').text.strip()
	#Extract string from div tag
	news_p = div.find('div', class_='rollover_description_inner').string.strip()

	###Space Images Scrapping
	#Set up splinter
	executable_path = {'executable_path': '/usr/local/bin/chromedriver'}
	browser = Browser('chrome', **executable_path, headless=False)
	#Splinter visit url
	url2 = "https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars"
	browser.visit(url2)
	#Splinter clicks on button and waits 5 seconds for page to load
	browser.click_link_by_partial_text('FULL IMAGE')
	time.sleep(2)
	#Get new HTML text after browser.click
	html2 = browser.html
	soup2 = BeautifulSoup(html2, 'html.parser')
	#Use BeautifulSoup to find featured image link
	result = soup2.body.find('div', class_="fancybox-inner fancybox-skin fancybox-dark-skin fancybox-dark-skin-open")
	result = result.find('img').attrs['src']
	featured_image_url = "https://www.jpl.nasa.gov" + result

	###Mars Weather Twitter
	#Get HTML text
	url3 = "https://twitter.com/marswxreport?lang=en"
	html3 = requests.get(url3)
	soup3 = BeautifulSoup(html3.text, 'html.parser')
	#BeautifulSoup to find weather tweet text
	result3 = soup3.body.find('div', class_="js-tweet-text-container").find("p").text.strip()
	mars_weather = result3

	###Mars Facts
	#Use pandas to fetch HTML table data
	url4 = "http://space-facts.com/mars/"
	tables = pd.read_html(url4)
	df = tables[0]
	df = df.rename(columns={0:"Parameter", 1: "Value"})
	len_df = range(len(df))

	###Mars Hemispheres
	#Use Splinter to visit URL
	url5 = "https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars"
	browser.visit(url5)
	#Get HTML text
	html5 = browser.html
	soup5 = BeautifulSoup(html5, "html.parser")
	hemi_title = []
	hemi_url = []
	#Use BeautifulSoup to find name of each button
	result5 = soup5.body.find_all('div', class_="item")
	for each in result5:
	    hemi_title.append(each.find('h3').text)
	time.sleep(2)
	#Use Splinter to browser.click on each button by name in "hemi_title", fetch new HTML text, find img url, and return to home page
	for x in range(0,4):
	    browser.visit(url5)
	    browser.click_link_by_partial_text(hemi_title[x])
	    time.sleep(2)
	    html_temp = browser.html
	    soup_temp = BeautifulSoup(html_temp, 'html.parser')
	    results_temp = soup_temp.body.find('div', class_='downloads').find('a').attrs['href']

	    hemi_url.append(results_temp)
	hemisphere_image_urls = []
	#Build dictionary
	for x in range(len(hemi_title)):
	    hemisphere_image_urls.append({"title": hemi_title[x], "img_url": hemi_url[x]})
	return render_template("index.html", news_title=news_title, news_p=news_p,
		featured_image_url=featured_image_url, mars_weather=mars_weather, len_df=len_df, df=df, 
		hemisphere_image_urls=hemisphere_image_urls)

if __name__ == "__main__":
	app.run(debug=True)
