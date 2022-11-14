#import thư viện
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

username = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "input[name = 'username']")))
password = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "input[name = 'password']")))

username.clear()
password.clear()
username.send_keys("lqkhai1801")
password.send_keys("zxc123zxc123")

log_in = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "button[type = 'submit']"))).click()

not_now = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//button[contains(text(), 'Not Now')]"))).click()
not_now2 = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//button[contains(text(), 'Not Now')]"))).click()

searchbox = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//input[@placeholder='Search']")))
searchbox.clear()
keyword = "#cat"
searchbox.send_keys(keyword)
time.sleep(1)

searchbox.send_keys(Keys.ARROW_DOWN)
time.sleep(5)
searchbox.send_keys(Keys.ENTER)
time.sleep(5)

driver.execute_script("window.scrollTo(0,4000);")

images = driver.find_elements(By.TAG_NAME, 'img')
img = [image.get_attribute('src') for image in images]

images

path = os.getcwd()
path = os.path.join(path, keyword[1:] + "s")

os.mkdir(path)
path


counter = 0
for image in images:
    save_as = os.path.join(path, keyword[1:] + str(counter) + '.jpg')
    wget.download(image, save_as)
    counter+=1