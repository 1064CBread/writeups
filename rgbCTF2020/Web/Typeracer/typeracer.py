# typeracer.py

import os
import time
from bs4 import BeautifulSoup
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.action_chains import ActionChains

# install correct webdriver
driver = webdriver.Chrome(ChromeDriverManager().install())

# set up selenium variables
driver.get("http://challenge.rgbsec.xyz:8973/")
actions = ActionChains(driver)

# click start button
elem = driver.find_elements_by_class_name("btn")[0]
elem.click()

# 5s delay before text appears
input("> Press enter when the game starts...")

# get all spans with the text to be typed
# spans have a style attribute that determines their order
res = driver.page_source
soup = BeautifulSoup(res, "html.parser")
elems = [(int(e.get('style').split(';')[0].lstrip('order: ')), e.text.rstrip(
    '\xa0')) for e in soup.findAll("span") if '\xa0' in e.text]
elems.sort(key=lambda x: x[0])

# make the full text string
typetext = ' '.join([x[1] for x in elems])
print(typetext)

# send the actions
actions.send_keys(typetext)
actions.perform()
