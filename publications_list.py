import re
import requests
import pandas as pd
import openpyxl
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options


#setting up the driver configuration
options = Options()
#options.add_argument("--headless")

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()), options=options)
url = "https://adrindia.org/content/comprehensive-compilation-book-titles-and-research-papers-citing-adr-data-or-utilizing#research_papers"
driver.get(url)

page_source = driver.page_source
soup = BeautifulSoup(page_source, "html.parser")
table = soup.find('table', class_='table table-bordered')
print(table)
