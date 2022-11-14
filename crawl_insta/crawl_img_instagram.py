from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
import time
import os
import wget

# đường dẫn driver
driver = webdriver.Chrome(executable_path='D:/chromedriver/chromedriver.exe')
driver.get('https://www.instagram.com/')

#target username, password
username = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "input[name='username']")))
password = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "input[name='password']")))

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

#target the login button and click it
button = WebDriverWait(driver, 2).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "button[type='submit']"))).click()

#nadle NOT NOW
not_now = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//button[contains(text(), "Not Now")]'))).click()
not_now2 = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//button[contains(text(), "Not Now")]'))).click()

# search_icon = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[1]/div/div/div/div[1]/div/div/div/div[1]/div[1]/section/nav/div[2]/div/div/div[2]/div/div[4]/a")))
# search_icon.click()

searchbox = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//input[@placeholder='Search']")))
searchbox.clear()

#search for the hashtag
keyword = "v__ngeen"
searchbox.send_keys(keyword)
time.sleep(1)
searchbox.send_keys(Keys.ARROW_DOWN)
time.sleep(0.1)
searchbox.send_keys(Keys.ENTER)
time.sleep(5)


# lastHeight = driver.execute_script("return document.body.scrollHeight")
# while True:
#     driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
#     time.sleep(5)
#     newHeight = driver.execute_script("return document.body.scrollHeight")
#     if newHeight == lastHeight:
#         break
#     lastHeight = newHeight

for i in range(10):
    last_height = driver.execute_script("return document.documentElement.scrollHeight")
    driver.execute_script("window.scrollTo(0,document.documentElement.scrollHeight);")
    time.sleep(5)
    new_height = driver.execute_script("return document.documentElement.scrollHeight")
    last_height = new_height

# target all images on the page
images = driver.find_elements(By.TAG_NAME, 'img')
images = [image.get_attribute('src') for image in images]
images = images[:-2]
print('Number of scraped images: ', len(images))

path = os.getcwd()
path = os.path.join(path, keyword[1:])
os.mkdir(path)
path

#download images
for counter, image in enumerate(images):
    save_as = os.path.join(path, keyword[1:] + str(counter) + '.jpg')
    wget.download(image, save_as)