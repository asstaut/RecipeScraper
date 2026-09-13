
units = ["teaspoon", "tablespoon", "cup","g", "teaspoons", "tablespoons", "cups", "ml","grams"]
sites = ["breaddad","inspiredtaste"]
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
    def __init__(self,ingredients,name = "Ingredients"):
        self.title = name
        self.ingredients = ingredients
    def print(self):
        print(self.title)
        for i in range(0,len(self.ingredients)):
            print(i+1,end=". ")
            self.ingredients[i].print()

class Directions:
    def __init__(self,instructions,title = "Instructions"):
        self.instructions = instructions
        self.title = title
    def print(self):
        print(self.title)
        for i in range(0,len(self.instructions)):
            print(i+1, ". ", self.instructions[i])

class Tips:
    def __init__(self,tips):
        self.tips = tips
    def print(self):
        for tip in self.tips:
            tip.print()

class Tip:
    def __init__(self,tip,title=None):
        self.tip = tip
        self.title = title
    def print(self):
        if self.title is not None:
            print(self.title)
        print(self.tip)

class Recipe:
    def __init__(self,name,ingredients,directions,URL,tips = None):
        self.URL = URL
        self.name = name
        self.tips = tips
        self.ingredients = ingredients #array of array of  recipe list
        self.directions = directions #list of directions
    def print(self):
        print(self.name)
        for ingredient_list in self.ingredients:
            ingredient_list.print()
        for  direction_list in self.directions:
            direction_list.print()
        if self.tips:
            print("Tips:")
            self.tips.print()

tablespoon_conversion={
    "teaspoon" : 3,
    "cup": 0.0625
}
teaspoon_conversion={
    "tablespoon" : 0.3333,
    "cup" : 0.02083
}
cup_conversion={
    "teaspoon" : 16,
    "tablespoon" : 48,
}
