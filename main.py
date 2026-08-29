import unicodedata

import requests
from bs4 import BeautifulSoup
import re
units = ["teaspoon", "tablespoon", "cup","g", "teaspoons", "tablespoons", "cups", "ml"]
Recipe = []
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


URL = "https://realpython.github.io/fake-jobs/"
URL = "https://breaddad.com/easy-banana-bread-recipe/"
URL = "https://www.inspiredtaste.net/24412/cocoa-brownies-recipe/"
URL = "https://www.inspiredtaste.net/100913/lemon-blueberry-bread-recipe/"

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'
}
page = requests.get(URL, headers=headers)


soup = BeautifulSoup(page.content, "html.parser")



recipe = soup.find("span", class_="itr-ingredients")
ptags =  recipe.find_all('p')

for p in ptags:
    print(p.text.strip())

all_texts = [p.text.strip() for p in recipe.find_all('p')]
print(all_texts)

for text in all_texts:
    words = text.split()
    item =  RecipeItem()
    lastunit =0
    for i in range(0,len(words)):
        if words[i] in units:
            if lastunit ==0 :
                item.unit = words[i]
                lastunit = i
                if words[i-1].isdigit():
                    item.quantity= int(words[i-1])
                elif words[i-2].isdigit():
                    item.quantity = int(words[i-2]) + round(unicodedata.numeric(words[i-1]),2)
                else:
                    item.quantity= round(unicodedata.numeric(words[i-1]),2)
            else:
                item.secondary_unit = words[i]
                lastunit = i
                if words[i - 1].isdigit():
                    item.quantity = int(words[i - 1])
                elif words[i - 2].isdigit():
                    item.quantity = int(words[i - 2]) + unicodedata.numeric(words[i - 1])
                else:
                    item.quantity = unicodedata.numeric(words[i - 1])
    if item.quantity is None:
        item.quantity = int(words[lastunit])
        item.unit = ""
    for i in range(lastunit+1,len(words)):
        item.name += words[i].capitalize()
        item.name +=" "
    firstMatch = item.name.find("(")
    lastMatch = item.name.find(")")
    if firstMatch >= 0:
        weight = item.name[firstMatch+1:lastMatch]
        weight = weight.split()
        weightCount =0
        for i in range(0,len(weight)):
            if weight[i].isdigit():
                if weightCount ==0 :
                    weightCount +=1
                    item.weight = int(weight[i])
                    item.weightUnit = weight[i+1].casefold()
                else:
                    weightCount +=1
                    item.secondaryWeight = int(weight[i])
                    item.secondaryWeightunit= weight[i + 1].casefold()
        item.name = item.name[:firstMatch] + item.name[lastMatch+1:]
    Recipe.append(item)


for item in Recipe:
    item.print()






