# -*- coding: utf-8 -*-
from selenium import webdriver
from bs4 import BeautifulSoup
from urllib.request import urlretrieve
import utilities

#from selenium.common.exceptions import TimeoutException
#from selenium.webdriver.common.by import By
#from selenium.webdriver.support.ui import WebDriverWait
#from selenium.webdriver.support import expected_conditions as EC
#from selenium.webdriver.common.keys import Keys
#from time import sleep
#import re

driver = webdriver.Firefox()
driver.implicitly_wait(30)
driver.get('http://blog.nogizaka46.com/')
html_doc = driver.page_source
soup = BeautifulSoup(html_doc, 'html.parser')
utilities.IdolOtaku.full_page_source(soup)

page = utilities.IdolOtaku.parse_blog_in_page(soup)
titles = page[0]
authors = page[1]
bodies = page[2]

#Print blog's title + body in text + PicLinks to txt
assay = 0
imgID = 0
bw = open('Blogs.txt', 'ab')
for title in titles:
    if utilities.IdolOtaku.title_is_not_blog(title) != True:
        bw.write(title.text.encode()+b'\n')
        bw.write(authors[assay].text.encode() + b'\n')
        bw.write(bodies[assay].text.encode()+b'\n')
        for url in utilities.IdolOtaku.get_blog_pic(soup, assay):
            bw.write(url.encode()+b'\n')
            urlretrieve(url, "data/%04d.jpg" % imgID)
            imgID = imgID + 1
        assay = assay + 1

#Blog's quantities
print(assay)
driver.close()

