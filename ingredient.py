class Ingredient:
    def __init__(self, amount, name):
        self.amount = amount
        self.name = name

    def print(self):
        print("----------")
        print("  Amount: "+str(self.amount))
        print("  Name: "+str(self.name))