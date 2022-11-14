#imports here
from importlib.resources import path
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from time import sleep
import Account
import numpy as np
import pandas as pd
import Get_Driver

driver = Get_Driver.get_driver()

# access to facebook.com
# driver.get('https://www.facebook.com/groups/advertisingvietnam/members')
driver.get('https://www.facebook.com/groups/1160928604411864/members')

# target username and password
username = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "input[name='email']")))
password = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "input[name='pass']")))

#enter username and password
username.clear()
username.send_keys(Account.GetUsername())
password.clear()
password.send_keys(Account.GetPassWord())

#target the login button and click it
button = WebDriverWait(driver, 2).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "button[type='submit']"))).click()
sleep(2)

# scroll to bottom page
for i in range(300):
    print(i)
    last_height = driver.execute_script("return document.documentElement.scrollHeight")
    driver.execute_script("window.scrollTo(0,document.documentElement.scrollHeight);")
    sleep(5)
    new_height = driver.execute_script("return document.documentElement.scrollHeight")
    if new_height == last_height:
        break
    last_height = new_height

# declare list_id
list_id = []

# target and get all the <a> elements
users = driver.find_element(By.XPATH,'/html/body/div[1]/div/div[1]/div/div[3]/div/div/div/div[1]/div[1]/div/div[2]/div/div/div[2]/div/div/div/div/div').find_elements(By.TAG_NAME, 'a')

for user in users:
    # get link user from attribute href
    link_user = user.get_attribute('href') 

    # slice link_user to get id user
    id = link_user[-16:-1]
    
    # append id to list_id
    list_id.append(id)

# close chrome driver
driver.close()

#remove duplicate in list
sort_list = dict.fromkeys(list_id)
list_id = list(sort_list)

# declare dict to save list id user
data  ={
    "id": list_id
}

# export data to csv file
df = pd.DataFrame(data).to_csv('list_user12.csv', index= False)

# delete column index
np.savetxt('list_user.csv', list_id, fmt='%s')



