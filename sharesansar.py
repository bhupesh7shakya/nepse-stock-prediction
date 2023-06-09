import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from bs4 import BeautifulSoup
from constraint import SYMBOLS
import os

def scrapy(symbol):

    # Set up WebDriver and open the website
    driver = webdriver.Chrome(executable_path='/path/to/chromedriver')
    driver.get(f'https://www.sharesansar.com/company/{symbol}')

    # Wait for the "Price History" tab to be clickable and click it
    tab_selector = '#btn_cpricehistory'
    tab = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, tab_selector)))
    tab.click()

    # Create an empty list to store table data
    table_data_list = []

    # Repeat the task until the end of pagination
    while True:
        # Wait for the table to load
        table_selector = '#cpricehistory'
        table = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.CSS_SELECTOR, table_selector)))

        # Wait for the "Processing..." element to have display:none
        processing_element_selector = '#myTableCPriceHistory_processing'
        wait = WebDriverWait(driver, 10)
        wait.until(EC.invisibility_of_element_located((By.CSS_SELECTOR, processing_element_selector)))

        # Retrieve the table data using BeautifulSoup
        soup = BeautifulSoup(table.get_attribute('innerHTML'), 'html.parser')
        rows = soup.find_all('tr')

        # Extract each column's data from the table
        for row in rows:
            columns = row.find_all('td')
            row_data = [column.text for column in columns]
            table_data_list.append(row_data)

        # Check if there is a next page
        next_button = driver.find_element(By.ID, 'myTableCPriceHistory_next')
        if 'disabled' in next_button.get_attribute('class'):
            # No next page, exit the loop
            break
        break
        # Click the next page button
        next_button.click()

    # Close the browser
    driver.quit()

    # Create a Pandas DataFrame from the table data list
    df = pd.DataFrame(table_data_list)

    # Specify the folder path
    folder_path = 'price_history'

    # Specify the filename and extension
    filename = f'{symbol}.xlsx'

    # Combine the folder path and filename to create the complete file path
    file_path = os.path.join(folder_path, filename)

    # Save the DataFrame to the specified Excel file
    df.to_excel(file_path, index=False)
    # # Save the DataFrame to an Excel file
    # df.to_excel(f'{symbol}.xlsx', index=False)

print(scrapy('NICL'))

# for  s in SYMBOLS:
#     print(s['symbol'],"\n")
#     scrapy(s[)    
