import datetime

class Recipe:
    def __init__(self, recipeId=None, title=None, author=None, url=None, date=None, dateFound=None, description=None, directions=None, prepTime=None):
        self.id = recipeId
        self.title = title
        self.author = author
        self.url = url
        self.date = date
        self.dateFound = dateFound if dateFound else datetime.datetime.now()
        self.description = description
        self.directions = directions
        self.prepTime = prepTime

        