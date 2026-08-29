from type_utils import RecipeItem, units, Ingredients
import unicodedata
def getlist(all_texts):
    Recipe= []
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
    return Recipe

def getingredients(soup):
    all_ingredients = []
    if not soup.find("span",class_="ingredient_heading") is None:
        while not soup.find("span",class_="ingredient_heading") is None:
            ingtitle= soup.find("span", class_="ingredient_heading")
            recipe = soup.find("span", class_="itr-ingredients")
            all_texts = [p.text.strip() for p in recipe.find_all('p')]
            ingredients_list = getlist(all_texts)
            itemname = ingtitle.text
            item = Ingredients(itemname,ingredients_list)
            all_ingredients.append(item)
            ingtitle.attrs={}
            recipe.attrs={}
    if soup.find("span", class_="ingredient_heading") is None:
        recipe = soup.find("span", class_="itr-ingredients")
        all_texts = [p.text.strip() for p in recipe.find_all('p')]
        ingredients_list = getlist(all_texts)
        itemname = soup.find("h1", class_="headline").text.strip()
        item = Ingredients(itemname, ingredients_list)
        all_ingredients.append(item)

    return all_ingredients











