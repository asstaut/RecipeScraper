from inspired_taste import getingredients, get_directions, get_tips
import requests
from bs4 import BeautifulSoup
import re
Recipe = []



URL = "https://realpython.github.io/fake-jobs/"
URL = "https://breaddad.com/easy-banana-bread-recipe/"
URL = "https://www.inspiredtaste.net/24412/cocoa-brownies-recipe/"
URL = "https://www.inspiredtaste.net/100913/lemon-blueberry-bread-recipe/"
URL = "https://www.inspiredtaste.net/19313/easy-focaccia-bread-recipe-with-herbs/"

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'
}
page = requests.get(URL, headers=headers)


soup = BeautifulSoup(page.content, "html.parser")
items = get_tips(soup)

for item in items:
    item.print()



