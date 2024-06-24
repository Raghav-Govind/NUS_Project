# selenium 4
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
import re


options = Options()
options.add_argument("--headless")
driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()), options=options)


driver.implicitly_wait(3)
url = "https://www.myneta.info/westbengal2016/index.php?action=summary&subAction=winner_serious_crime&sort=candidate#summary"
driver.get(url)
page_source = driver.page_source
driver.quit()
soup = BeautifulSoup(page_source, "html.parser")

# Creating list with all tables
tables = soup.find_all('table')

#  Looking for the table with the classes 'wikitable' and 'sortable'
table = soup.find('table', class_='w3-table w3-bordered')


names = []

# Check if the table is found
if table:
    # Find all <tr> elements in the table
    rows = table.find_all('tr')
    
    # Loop through each row and extract the names
    for row in rows:
        # Find all <td> elements in the row
        cols = row.find_all('td')
        for col in cols:
            # Find the <a> tag within the <td>
            a_tag = col.find('a')
            if a_tag:
                # Extract the text content from the <a> tag
                name = a_tag.get_text().strip()
                # Add the name to the list
                names.append(name)

# Print the extracted names
print(len(names))
