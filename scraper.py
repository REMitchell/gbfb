# https://www.cookinglight.com/recipe-sitemap.xml
import requests
from bs4 import BeautifulSoup
import re
import json
import time
import csv
from recipe import Recipe
from ingredient import ingredient
from ingredientParser import IngredientParser

class Scraper:
    def __init__(self):
        self.session = requests.Session()

    def getPage(self, url):
        """
        Utilty function used to get a Beautiful Soup object from a given URL
        """
        headers = {"User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36",
                "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8"}
        try:
            req = self.session.get(url, headers=headers)
        except requests.exceptions.RequestException:
            return None
        bs = BeautifulSoup(req.text, "html.parser")
        return bs
    
    def safeJsonGet(self, content, path):
        for item in path:
            if item in content:
                content = content[item]
            else:
                return None
        return content

    def extractCookingLight(self, url):
        bs = self.getPage(url)
        content = json.loads(bs.find('script', {'type': 'application/ld+json'}).text)
        content = content[-1]
        print(content)
        recipe = Recipe()
        recipe.title = self.safeJsonGet(content, ['name'])
        recipe.author = self.safeJsonGet(content, ['author', 'name'])
        recipe.url = url
        recipe.date = self.safeJsonGet(content, ['datePublished'])
        recipe.description = self.safeJsonGet(content, ['description'])
        recipe.directions = self.safeJsonGet(content, ['recipeInstructions'])
        recipe.prepTime = self.safeJsonGet(content, ['totalTime'])


    def cookingLight(self):
        siteListing = self.getPage('https://www.cookinglight.com/recipe-sitemap.xml')
        urls = siteListing.findAll('loc')
        for url in urls[:1]:
            print(url)
            self.extractCookingLight(url.text)

        
scraper = Scraper()
scraper.cookingLight()
