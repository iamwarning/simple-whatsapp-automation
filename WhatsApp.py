#!/usr/bin/env python
# coding: utf-8

""" 
Simple script to automate the sending of messages by WhatsApp using Selenium. 
"""

from selenium import webdriver
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.keys import  Keys
from selenium.webdriver.common.by import By
import time

#Path where the webdriver is located
browser = webdriver.Chrome("/home/baos/Documents/Python/WhatsApp Automation/./chromedriver")

browser.get("https://web.whatsapp.com/")
wait = WebDriverWait(browser, 600)

target = '" _user_ "' #Contact name
string = " _message_ " #Custom message  
x_arg = '//span[contains(@title, ' + target + ')]'
target = wait.until(ec.presence_of_element_located((By.XPATH, x_arg)))
target.click()

input_box = browser.find_element_by_class_name("_1Plpp")
for i in range(100):
    input_box.send_keys(string + Keys.ENTER)

