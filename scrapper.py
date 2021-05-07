from bs4 import BeautifulSoup
import requests
import pymongo

from splinter import Browser
from webdriver_manager.chrome import ChromeDriverManager
from flask import Flask, render_template, redirect
from flask_pymongo import PyMongo

#website that list all managers in the history of the premier league (1992-2021)
url= 'https://www.premierleague.com/managers?se=-1&cl=-1'

#creates a link to a web browser controlled by python and visist url
executable_path = {'executable_path': ChromeDriverManager().install()}
browser = Browser('chrome', **executable_path, headless=True)
browser.vist(url)

#accesses the html of the page being visited
html = browser.html
soup = beautifulSoup(html, 'html.parser')

#an array that will contain manager objects containing their name, team coached,
# and link to their page
all_managers = []

results = browser.find_by_css('tr')

for result in results:
    print(result) 