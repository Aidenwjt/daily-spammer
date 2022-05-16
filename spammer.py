#!/usr/bin/env python3

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

options = webdriver.FirefoxOptions()
options.add_argument('start-maximized')
options.add_argument('disable-infobars')

browser = webdriver.Firefox(options=options)
browser.get('http://noah.binaryfox.ca/feedback.php')

WebDriverWait(browser, 10).until(EC.frame_to_be_available_and_switch_to_it((By.CSS_SELECTOR,"iframe[name^='a-'][src^='https://www.google.com/recaptcha/api2/anchor?']")))
WebDriverWait(browser, 10).until(EC.element_to_be_clickable((By.XPATH, "//span[@id='recaptcha-anchor']"))).click()

# TODO: Audio file work around

elem = browser.find_element_by_name('feedback')
elem.send_keys('You suck at league of legends')

##search_btn = browser.find_element(By.NAME, 'Submit')
##webdriver.ActionChains(browser).double_click(search_btn).perform()

##browser.close()
