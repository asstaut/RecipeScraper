
#function to get the new measurements and adjust the recipe accordingly

class MyObject:
    pass
def find_new_item(recipe,new_measurements):
    ingredients = recipe.ingredients
    original_amount = 1
    flag = False
    for ingredient in ingredients:
        for item in ingredient.ingredients:
            if item.name.strip() == new_measurements.name:
                print("og item")
                original_amount = item.weight
                flag = True
                break
        if flag:
            break
    ratio = new_measurements.amount/ original_amount
    for ingredient in ingredients:
        for item in ingredient.ingredients:
            if item.weight:
                item.weight = round(item.weight * ratio,2)
            if item.quantity:
                item.quantity = round(item.quantity * ratio,2)
            if item.secondary_quantity:
                item.secondary_quantity = round(item.secondary_quantity * ratio,2)

    recipe.ingredients = ingredients
    return recipe,ratio

    #new measurement has name and amt in grams

def get_new_measurements(recipe):
    new_measurements = MyObject()
    ingnum = input("Enter Ingredient")
    ingamount =int( input("Enter New Amount"))
    new_measurements.name = ingnum
    new_measurements.amount = ingamount
    new_recipe,ratio = find_new_item(recipe,new_measurements)
    print("Ratio = ",ratio)
    return new_recipe,ratio
