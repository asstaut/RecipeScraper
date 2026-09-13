from inspired_taste import get_recipe_from_inspired_taste
from bread_dad import get_recipe_from_bread_dad
def get_recipe(url):
    if url.find("inspiredtaste") >= 0:
        recipe = get_recipe_from_inspired_taste(url)
        return recipe
    if url.find("breaddad") >= 0:
        recipe = get_recipe_from_bread_dad(url)
        return recipe
    return None