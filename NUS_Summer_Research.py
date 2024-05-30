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
options.add_argument("--headless")


# Function to extract names from a URL
def extract_names_from_url(urls):
    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()), options=options)
    names = []
    
    for url, state, year in zip(urls['x'], urls['State'], urls['Year']):
        driver.get(url)
        page_source = driver.page_source
        
        soup = BeautifulSoup(page_source, "html.parser")
        table = soup.find('table', class_='w3-table w3-bordered')

        if table:
            rows = table.find_all('tr')
            for row in rows:
                cols = row.find_all('td')
                for col in cols:
                    a_tag = col.find('a')
                    if a_tag:
                        name = a_tag.get_text().strip()
                        names.append({'Candidate': name, 'State': state, 'Year': year})

    driver.quit()
    return names


# Read Required Data from .csv files
urls = pd.read_csv("D:/E(prev)/Acads(Official)/NUS Summer/Project_S/Final_links.csv")
urls = urls[['x', 'State', 'Year']]
filtered_MLAs_df = pd.read_csv("D:/E(prev)/Acads(Official)/NUS Summer/Project_S/Filtered_MLAs.csv")

Severe_Crimes = pd.DataFrame(extract_names_from_url(urls))

filtered_MLAs_df['Severity'] = 'Mild'

for index, crime_row in Severe_Crimes.iterrows():
    name = crime_row['Candidate']
    state = crime_row['State']
    year = crime_row['Year']
    
    # Finding matching rows in filtered_MLAs_df
    matching_rows = filtered_MLAs_df[(filtered_MLAs_df['Candidate'] == name) & 
                                     (filtered_MLAs_df['State'] == state) & 
                                     (filtered_MLAs_df['Year'] == year)]
    
    # Updating Severity to "Severe" for matching rows
    filtered_MLAs_df.loc[matching_rows.index, 'Severity'] = 'Severe'

# Define the file path
file_path = r'D:\E(prev)\Acads(Official)\NUS Summer\Project_S\modified_MLA_list.xlsx'

# Save the modified dataframe as an Excel file
filtered_MLAs_df.to_excel(file_path, index=False)

