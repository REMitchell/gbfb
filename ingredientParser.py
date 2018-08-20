import re

class IngredientParser:
    measurements = ['cup', 'cups', 'tablespoon', 'tablespoons', 'tbsp', 'tbsps', 'teaspoon', 'teaspoons', 'tsp', 'tsps', 'pint', 'pints', 'liter', 'liters', 'gallon', 'gallons', 'pint', 'pints', 'pt', 'pts' 'ounces', 'oz', 'fl oz', 'fluid ounce', 'fluid ounces' 'ounce', 'dash', 'dashes', 'pinch', 'pinches', 'gram', 'grams', 'medium', 'small', 'large', 'regular']
    numbers = ['one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']
    numberRegex = r'([0-9\\/]+$)'
    def __init__(self, text):
        self.text = text
        self.textParts = self.text.split(' ')

    def getMeasurement(self):
        '''
        Get the first item in the measurements list
        '''
        for textPart in self.textParts:
            if textPart.lower() in self.measurements:
                self.textParts.remove(textPart)
                return textPart
    
    def getAmount(self):
        for textPart in self.textParts:
            if textPart in self.numbers or re.match(self.numberRegex, textPart):
                self.textParts.remove(textPart)
                return textPart

    def getIngredient(self):
        '''
        Needs to be called after getMeasurement and getAmount
        '''
        return ' '.join(self.textParts)


ingredientsList = [
      "1  medium spaghetti squash (about 5 cups of flesh)",
      "2 tablespoons butter",
      "2\/3 cup chopped pecans",
      "3 tablespoons all-purpose flour",
      "2 tablespoons rolled oats",
      "2 tablespoons brown sugar",
      "1 teaspoon kosher salt, divided",
      "2 teaspoons cinnamon, divided",
      "2 tablespoons half-and-half, divided",
      "1 teaspoon vanilla extract",
      "4 tablespoons Greek yogurt"
    ]


for ingredient in ingredientsList:
    parser = IngredientParser(ingredient)
    print("Measurement: "+parser.getMeasurement())
    print("Amount: "+parser.getAmount())
    print("Name: "+parser.getIngredient())