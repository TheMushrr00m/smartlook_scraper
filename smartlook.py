#! /usr/bin/env python
# -*- coding: utf-8 -*-

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup
from importlib import reload
import time
import sys

reload(sys)
user = 'gabriel.cueto@granplan.com'
pwd = 'Granplan10'
smartlook_login = 'https://www.smartlook.com/es/app/sign/in'
smartlook_dashboard = 'https://www.smartlook.com/app/dashboard'
final_links = []

driver = webdriver.Firefox()
driver.get(smartlook_login)

elem = driver.find_element_by_id('frm-signIn-form-email')
elem.send_keys(user)
elem = driver.find_element_by_id('frm-signIn-form-password')
elem.send_keys(pwd)
elem.send_keys(Keys.RETURN)

#driver.get(smartlook_dashboard)
time.sleep(15)
source_code = driver.page_source

soup = BeautifulSoup(source_code, 'lxml')
table = soup.find_all('table')
header_table = soup.find('thead')
rows = soup.find_all('tbody')
with open('Smartlook_Output.txt', 'w') as text_file:
    # Obtiene las columnas para la cabecera
    for tr in header_table.find_all('tr'):
        for th in tr.find_all('th'):
            if not th.get('title') is None:
                text_file.write(str(th.get('title')) + '|')

driver.close()

