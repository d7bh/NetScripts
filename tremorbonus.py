#EXAMPLE of usage python to login
#imports for future use...
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import Select
from lxml import html
from bs4 import BeautifulSoup
from urllib.request import urlopen
from colorama import Fore, Back, Style
import sched,time
import sys
driver=webdriver.PhantomJS('/usr/bin/phantomjs', service_args=['--ignore-ssl-errors=true','--ssl-protocol=any'])
driver.set_window_size(1120,550)
driver.set_page_load_timeout(30)
wait = WebDriverWait(driver,10)
driver.get('http://www.tremorgames.com/')
usr="USERNAME"
pwd="PASSWORD"
fusr=driver.find_element_by_id("loginuser")
fusr.send_keys(usr)
fpass=driver.find_element_by_id("loginpassword")
fpass.send_keys(pwd)
fsu=driver.find_element_by_id("Submit")
fsu.click()
#driver.save_screenshot("screen.png")
driver.close()
