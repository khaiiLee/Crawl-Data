#imports here
from asyncio.windows_events import NULL
from importlib.util import spec_from_loader
from numpy import append
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from time import sleep
import json
from selenium.webdriver.chrome.options import Options
import pyautogui as gui

#disable alerts chrome driver
chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("start-maximized")
prefs = {"profile.default_content_setting_values.notifications" : 2}
chrome_options.add_experimental_option("prefs",prefs)

chrome_options.add_argument("--incognito")
driver = webdriver.Chrome(chrome_options=chrome_options,executable_path='D:/chromedriver/chromedriver.exe')

driver.get('https://www.facebook.com/groups/1160928604411864/members')
# driver.get('https://www.facebook.com')

username = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "input[name='email']")))
password = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "input[name='pass']")))

FILE = open('account.txt','r')
LINES = FILE.readlines()

if len(LINES) > 0:
    LINES = [line.strip() for line in LINES]
    ID, PASS = LINES[0], LINES[1]

#enter username and password
username.clear()
username.send_keys(ID)
password.clear()
password.send_keys(PASS)
sleep(5)
#target the login button and click it
button = WebDriverWait(driver, 2).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "button[type = 'submit']"))).click()
sleep(5)

#scroll page
scroll_page = driver.execute_script("window.scrollTo(0,1200);")
sleep(3)

scroll_height=1200

not_found = 'Null'

PROFILE = []
data = dict()

#get user information
for i in range(5):
    try:
        #find user name
        name_user = driver.find_element(By.XPATH,'/html/body/div[1]/div/div[1]/div/div[3]/div/div/div/div[1]/div[1]/div/div[2]/div/div/div[2]/div/div/div/div/div/div/div/div/div/div/div[2]/div[9]/div/div[2]/div/div['+str(i)+']/div/div/div[2]/div[1]/div/div/div[1]/span/span/span/a')
        data['name'] = name_user.text

        #print user name
        print('-'*20)
        print(f'User name: {name_user.text}')

        #click user name
        name_user.click()
        sleep(5)
        
        #click view main profile
        try: 
            view_main_profile = driver.find_element(By.XPATH,"//span[text()='View Main Profile']").click()
            sleep(5)
        except:
             #target the three-dot button
            three_dot_button= driver.find_element(By.XPATH,'/html/body/div[1]/div/div[1]/div/div[4]/div/div/div[1]/div/div[3]/div[2]/div[1]/div[2]/div/div/div[2]/div/div').click()
            sleep(1)
            view_main_profile_in_three_dot_button = driver.find_element(By.XPATH,"//span[text()='View Main Profile']").click()
            sleep(5)

        #click about user
        about_user = driver.find_element(By.XPATH,'/html/body/div[1]/div/div[1]/div/div[3]/div/div/div/div[1]/div[1]/div/div/div[3]/div/div/div/div[1]/div/div/div[1]/div/div/div/div/div/div/a[2]/div').click()
        sleep(3)

        #scroll profile
        scroll_profile = driver.execute_script("window.scrollTo(0,400);")
        sleep(3)
        
        #target and print user work
        try:
            user_work = driver.find_element(By.XPATH,'/html/body/div[1]/div/div[1]/div/div[3]/div/div/div/div[1]/div[1]/div/div/div[4]/div/div/div/div[1]/div/div/div/div/div[2]/div/div/div/div[1]/div/div/div[2]/div[1]/span/a/span/span').text
            print(f'user work: {user_work}')
        except:
            user_work = not_found 
            print(f'user work: {user_work}')
        data['work'] = user_work    

        #target and print user education
        try:
            user_education = driver.find_element(By.XPATH,'/html/body/div[1]/div/div[1]/div/div[3]/div/div/div/div[1]/div[1]/div/div/div[4]/div/div/div/div[1]/div/div/div/div/div[2]/div/div/div/div[2]/div/div/div[2]/div[1]/span/a/span/span').text
            print(f'user education: {user_education}')
        except:
            user_education = not_found
            print(f'user education: {user_education}')
        data['education'] = user_education

        #target and print user live
        try:
            user_live = driver.find_element(By.XPATH,'/html/body/div[1]/div/div[1]/div/div[3]/div/div/div/div[1]/div[1]/div/div/div[4]/div/div/div/div[1]/div/div/div/div/div[2]/div/div/div/div[3]/div/div/div[2]/div/span/a/span/span').text
            print(f'user live in: {user_live}')
        except:
            user_live = not_found
            print(f'user live in: {user_live}')
        data['live in'] = user_live

        #target and print user hometown
        try:
            user_hometown = driver.find_element(By.XPATH,'/html/body/div[1]/div/div[1]/div/div[3]/div/div/div/div[1]/div[1]/div/div/div[4]/div/div/div/div[1]/div/div/div/div/div[2]/div/div/div/div[4]/div/div/div[2]/div/span/a/span/span').text
            print(f'user hometown: {user_hometown}')
        except:
            user_hometown = not_found
            print(f'user hometown: {user_hometown}')
        data['hometown'] = user_hometown

        #target and print user relationship
        try:
            user_relationship = driver.find_element(By.XPATH,'/html/body/div[1]/div/div[1]/div/div[3]/div/div/div/div[1]/div[1]/div/div/div[4]/div/div/div/div[1]/div/div/div/div/div[2]/div/div/div/div[5]/div/div/div[2]/span').text
            print(f'user relationship: {user_relationship}')
        except:
            user_relationship = not_found
            print(f'user relationship: {user_relationship}')
        data['relationship'] = user_relationship

        print('-'*50)
        print(data)
        PROFILE.append(data)
        print('-'*50)

        #back to the previous page
        driver.execute_script("window.history.go(-1)")
        sleep(3)
        #back to the previous page
        driver.execute_script("window.history.go(-1)")
        sleep(3)

        #scroll page
        scroll_page = driver.execute_script("window.scrollTo(0,"+str(scroll_height)+");")

        # increase scroll height
        scroll_height+=100

    except Exception:
        print(Exception) 
        continue

print(PROFILE)
print('-'*20)
json_object = json.dumps(PROFILE, indent = 4, ensure_ascii=False) # UTF-8 fixed
print(json_object)

with open("profile_facebook.json", "w") as outfile:
    outfile.write(json_object)

# import csv
# header = ['name', 'work', 'education', 'live in','hometown','relationship']

# with open('data.csv', 'w', encoding='UTF8', newline='') as f:
#     writer = csv.writer(f)
#     writer.writerow(header)
#     writer.writerow(PROFILE)

driver.close()

