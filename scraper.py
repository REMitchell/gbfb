# https://www.cookinglight.com/recipe-sitemap.xml
import requests
from bs4 import BeautifulSoup
import re
import json
import time
import csv
from recipe import Recipe
from ingredient import Ingredient
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
    
    def safeJsonGet(self, content, path, default=None):
        for item in path:
            if item in content:
                content = content[item]
            else:
                return default
        return content

    def extractCookingLight(self, url):
        bs = self.getPage(url)
        content = json.loads(bs.find('script', {'type': 'application/ld+json'}).text)
        content = content[-1]
        recipe = Recipe()
        recipe.title = self.safeJsonGet(content, ['name'])
        recipe.author = self.safeJsonGet(content, ['author', 0, 'name'])
        recipe.url = url
        recipe.date = self.safeJsonGet(content, ['datePublished'])
        recipe.description = self.safeJsonGet(content, ['description'])
        recipe.directions = self.safeJsonGet(content, ['recipeInstructions'])
        recipe.prepTime = self.safeJsonGet(content, ['totalTime'])
        print(self.safeJsonGet(content, ['recipeIngredient'], []))
        recipe.ingredients = [IngredientParser(text).toIngredient() for text in self.safeJsonGet(content, ['recipeIngredient'], [])]
        return recipe

    def cookingLight(self):
        siteListing = self.getPage('https://www.cookinglight.com/recipe-sitemap.xml')
        urls = siteListing.findAll('loc')
        for url in urls[:1]:
            print(url)
            recipe = self.extractCookingLight(url.text)
            recipe.print()

    def extractFoodNetwork(url):
        print(stub)


    def foodNetwork(self):
        # https://www.foodnetwork.com/recipes/recipes-a-z/123/p/1
        listings = ['123', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'XYZ']
        for listing in listings:
            for i in range(1, 20):
                bs = self.getPage('https://www.foodnetwork.com/recipes/recipes-a-z/'+listing+'/p/'+str(2))
                recipeLinks = bs.findAll('li', {'class':'m-PromoList__a-ListItem'})
                if len(recipeLinks) == 0:
                    continue
                for recipeLink in recipeLinks:
                    self.extractFoodNetwork(recipeLink.find('a').attrs['href'])

scraper = Scraper()
#scraper.cookingLight()
scraper.foodNetwork()
