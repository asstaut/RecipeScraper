units = ["teaspoon", "tablespoon", "cup","g", "teaspoons", "tablespoons", "cups", "ml"]
class RecipeItem:
    def __init__(self, name, quantity, unit, secondary_quantity,secondary_unit):
        self.name = name
        self.quantity = quantity
        self.unit = unit
        self.weight = None
        self.secondary_unit = secondary_unit
        self.secondary_quantity = secondary_quantity
        self.weightUnit= None
        self.secondaryWeightunit= None
        self.secondaryWeight = None
    def __init__(self):
        self.name = ""
        self.quantity = None
        self.unit = None
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
