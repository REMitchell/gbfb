import datetime

class Recipe:
    def __init__(self, recipeId=None, title=None, author=None, url=None, date=None, dateFound=None, description=None, directions=None, prepTime=None, ingredients=None):
        self.id = recipeId
        self.title = title
        self.author = author
        self.url = url
        self.date = date
        self.dateFound = dateFound if dateFound else datetime.datetime.now()
        self.description = description
        self.directions = directions
        self.prepTime = prepTime
        self.ingredients = ingredients


    def print(self):
        print("Title: "+str(self.title))
        print("Author: "+str(self.author))
        print("URL: "+str(self.url))
        print("Date: "+str(self.date))
        print("Date Found: "+str(self.dateFound))
        print("Description: "+str(self.description))
        print("Directions: "+str(self.directions))
        print("Prep Time: "+str(self.prepTime))
        for ingredient in self.ingredients:
            ingredient.print()

        