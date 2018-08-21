import re
from ingredient import Ingredient

class IngredientParser:
    measurements = ['cup', 'cups', 'tablespoon', 'tablespoons', 'tbsp', 'tbsps', 'teaspoon', 'teaspoons', 'tsp', 'tsps', 'pint', 'pints', 'liter', 'liters', 'gallon', 'gallons', 'pint', 'pints', 'pt', 'pts' 'ounces', 'oz', 'fl oz', 'fluid ounce', 'fluid ounces' 'ounce', 'dash', 'dashes', 'pinch', 'pinches', 'gram', 'grams', 'medium', 'small', 'large', 'regular']
    numbers = ['one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']
    numberRegex = r'([0-9\\/]+$)'
    def __init__(self, text):
        self.text = text
        self.textParts = self.text.split(' ')
        print("TEXT PARTS: ")
        print(self.textParts)
        self.measurement = self.getMeasurement()
        self.quantity =  self.getQuantity().strip()
        self.amount = (self.quantity+' '+self.measurement).strip()
        self.name = self.getName()

    def getMeasurement(self):
        '''
        Get the first item in the measurements list
        '''
        for i, textPart in enumerate(self.textParts):
            if textPart.lower() in self.measurements:
                self.textParts.remove(textPart)
                return textPart
        return ''
    
    def getQuantity(self):
        for i, textPart in enumerate(self.textParts):
            if textPart in self.numbers or re.match(self.numberRegex, textPart):
                self.textParts.remove(textPart)
                if i < len(self.textParts)-1:
                    return ' '.join([textPart, self.getQuantity()])
                return textPart
        return ''

    def getName(self):
        '''
        Needs to be called after getMeasurement and getAmount
        '''
        return ' '.join(self.textParts)

    def toIngredient(self):
        return Ingredient(self.amount, self.name)
