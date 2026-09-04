units = ["teaspoon", "tablespoon", "cup","g", "teaspoons", "tablespoons", "cups", "ml","grams"]
class RecipeItem:
    def __init__(self):
        self.name = ""
        self.quantity = None
        self.unit = ""
        self.weight = None
        self.secondary_unit = None
        self.secondary_quantity =None
        self.weightUnit= None
        self.secondaryWeightunit = None
        self.secondaryWeight = None
    def print(self):

        print(self.quantity, self.unit, end=" ")
        if not self.secondary_quantity is None:
            print(self.secondary_quantity,self.secondary_unit, end=" ")
        if not self.weightUnit is None:
            print("(",self.weight,self.weightUnit,")",end=" ")
        if not self.secondaryWeightunit is None:
            print(self.secondaryWeight,self.secondaryWeightunit,end=" ")
        print(self.name)

class Ingredients:
    def __init__(self,name,ingredients):
        self.title = name
        self.ingredients = ingredients
    def print(self):
        print(self.title)
        for ingredient in self.ingredients:
            ingredient.print()

class Directions:
    def __init__(self,instructions,title = None):
        self.instructions = instructions
        self.title = title
    def print(self):
        print(self.title)
        for instruction in self.instructions:
            print(instruction)

class Tips:
    def __init__(self,tips):
        self.tips = tips

class Tip:
    def __init__(self,tip,title=None):
        self.tip = tip
        self.title = title
    def print(self):
        if self.title is not None:
            print(self.title)
        print(self.tip)

class Recipe:
    def __init__(self,name,ingredients):
        self.name = name
        self.ingredients = ingredients

def get_individual_words(s):
    words = []
    for word in s.split(" "):
        words.append(word)
    return words
