#!/usr/bin/env python3

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

browser = webdriver.Firefox()
browser.get('http://noah.binaryfox.ca/feedback.php')

elem = browser.find_element_by_name('feedback')
elem.send_keys('You suck at league of legends')

search_btn = browser.find_element(By.NAME, 'submit')
webdriver.ActionChains(browser).double_click(search_btn).perform()
