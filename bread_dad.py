from selenium import webdriver
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup
from type_utils import Ingredients, RecipeItem,Directions
from lowest_common_item import *
import re
import unicodedata
def get_ingredients(ingredients_list,title):
    list_of_ingredients = ingredients_list.find_all("li")
    all_ingredients = []
    for l in list_of_ingredients:
        all_ingredients.append(process_ingredients_line(l))
    item = Ingredients(title,all_ingredients)
    return item

def get_directions(directions_list):
    all_directions = []
  #  dir = soup.find_all("div", class_="wprm-recipe-instruction-group")
    while soup.find("div", class_="wprm-recipe-instruction-group"):
        dir = soup.find("div", class_="wprm-recipe-instruction-group")
        dirlist = dir.find_all("li")
        directions_title = dir.find("h4")
        instruction = []
        print(directions_title)
        for l in dirlist:
            instruction.append(l.text)
        if directions_title is None:
            item = Directions(instruction)
        else :
            item = Directions(instruction,directions_title.text)
        dir.attrs = {}
        directions_title.decompose()
        all_directions.append(item)

    return all_directions

def process_ingredients_line(line):
    words = line.text.split("–")
    start = 0
    item = RecipeItem()
    if words[0] == "Optional":
        start = 1
    for i in range(start,start+3):
        word = words[i].strip()
        letters = word.split(" ")
        if i == start:
            if len(letters) == 2:
                item.quantity = int(letters[0].strip())
                if item.unit is not None:
                    item.unit = letters[1]
            if len(letters) == 3:
                decimal_unit =  round (int(letters[1][0]) / int(letters[1][2]), 2)
                item.quantity = int(letters[0]) + decimal_unit
                if item.unit is not None:
                    item.unit = letters[2]
        if i == start + 1:
            if start == 1:
                item.name = item.name+ "Optional - "
            for j in range(len(letters)):
                item.name = item.name + letters[j] + " "
        if i == start + 2:
            item.weight = float(letters[0])
            item.weightUnit = letters[1]
    item.print()



def get_recipe(link):
    driver = webdriver.Firefox()
    driver.get(link)
    block = driver.find_elements(By.CLASS_NAME,"wp-block-list")
    print(block)

def ingredients(ingredients_list):
    all_ingredients = []
    inglist = [d.text.strip() for d in ingredients_list.find_all('li')]
    print(inglist)

URL = "https://breaddad.com/easy-banana-bread-recipe/"
URL = "https://breaddad.com/easy-bread-machine-bagels/"

driver = webdriver.Firefox()
driver.get(URL)
block = driver.find_elements(By.CLASS_NAME,"wp-block-list")
soup = BeautifulSoup(driver.page_source, "html.parser")
all_ul_lists = soup.find_all("ul", class_="wp-block-list")
inglist = all_ul_lists[0]
title = soup.find("h1", class_= "entry-title").text.strip()


driver.quit()