from selenium import webdriver
from selenium.webdriver.common.by import By

# Using Firefox to access web

driver = webdriver.Chrome(executable_path='D:/chromedriver/chromedriver.exe')

# Open the website
driver.get('https://registers.esma.europa.eu/publication/searchRegister?core=esma_registers_firds')

# search for information
elem = driver.find_element(By.ID, 'keywordField')
elem.clear()
elem.send_keys('XS1114155283')

button = driver.find_element(By.ID, 'searchSolrButton')
button.click()

table_body = driver.find_element(By.XPATH, "//table[@id='T01']/tbody")
for link in table_body.find_elements(By.TAG_NAME, 'a'):
    href = link.get_attribute('href')
    # open in new tab
    driver.execute_script("window.open('%s', '_blank')" % href)
    # Switch to new tab
    driver.switch_to.window(driver.window_handles[-1])

    # Continuous your code