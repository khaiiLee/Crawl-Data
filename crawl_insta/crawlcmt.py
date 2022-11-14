#imports here
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from time import sleep
import os
import wget
from selenium.webdriver.chrome.options import Options
import pyautogui

#disable alerts chrome driver
chrome_options = webdriver.ChromeOptions()
prefs = {"profile.default_content_setting_values.notifications" : 2}
chrome_options.add_experimental_option("prefs",prefs)

chrome_options.add_argument("--incognito")
chrome_options.add_argument("--window-size=1920x1080")
driver = webdriver.Chrome(chrome_options=chrome_options,executable_path='D:/chromedriver/chromedriver.exe')

driver.get('https://www.facebook.com')
sleep(5)

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

#target the login button and click it
button = WebDriverWait(driver, 2).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "button[type='submit']"))).click()

searchbox = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//input[@placeholder='Search Facebook']")))
searchbox.clear()

#search by keywword
keyword = "Cộng đồng Marketing & Advertising"
searchbox.send_keys(keyword)
sleep(0.1)
searchbox.send_keys(Keys.ENTER)
sleep(5)
join_group = WebDriverWait(driver, 2).until(EC.element_to_be_clickable((By.XPATH, '/html/body/div[1]/div/div[1]/div/div[3]/div/div/div/div[2]/div[1]/div[2]/div/div/div/div/div/div[1]/div/div/div/div[1]/div[2]/div[1]/div/div/div[2]/div/div[1]/h3/span/span/span/a'))).click()
sleep(5)

topic = WebDriverWait(driver, 2).until(EC.element_to_be_clickable((By.CSS_SELECTOR, '#mount_0_0_Bg > div:nth-child(2) > div:nth-child(1) > div > div.rq0escxv.l9j0dhe7.du4w35lb > div > div > div > div.j83agx80.cbu4d94t.d6urw2fd.dp1hu0rb.l9j0dhe7.du4w35lb > div.l9j0dhe7.dp1hu0rb.cbu4d94t.j83agx80 > div.rq0escxv.du4w35lb.rek2kq2y.lpgh02oy > div > div > div > div.rq0escxv.l9j0dhe7.du4w35lb.j83agx80.cbu4d94t.d2edcug0.hpfvmrgz.rj1gh0hx.buofh1pr.g5gj957u.ph5uu5jm.b3onmgus > div > div > div.rq0escxv.l9j0dhe7.du4w35lb.j83agx80.pfnyh3mw.i1fnvgqd.gs1a9yip.owycx6da.btwxx1t3.pxsmfnpt.pedkr2u6.n1dktuyu.dvqrsczn.l23jz15m.d4752i1f > div > div > div > div > div > div.i09qtzwb.rq0escxv.n7fi1qx3.pmk7jnqg.j9ispegn.kr520xx4 > a:nth-child(6) > div.n00je7tq.arfg74bv.qs9ysxi8.k77z8yql.i09qtzwb.n7fi1qx3.b5wmifdl.hzruof5a.pmk7jnqg.j9ispegn.kr520xx4.c5ndavph.art1omkt.ot9fgl3s.rnr61an3'))).click()
sleep(10)
# click_peole = WebDriverWait(driver, 2).until(EC.element_to_be_clickable((By.XPATH, '/html/body/div[1]/div[1]/div[1]/div/div[3]/div/div/div/div[1]/div[1]/div/div[2]/div/div/div[1]/div/div/div[1]/div[2]/div/div/div/div/div[2]/div[5]/div/a/@href'))).click()
# pyautogui.click(800,550)
# sleep(100)

# members = WebDriverWait(driver, 2).until(EC.element_to_be_clickable((By.XPATH, '/html/body/div[1]/div/div[1]/div/div[3]/div/div/div/div[1]/div[1]/div[3]/div/div/div/div[1]/div/div/div[1]/div/div/div/div/div/div[2]/a[5]/div/div'))).click()

# user = WebDriverWait(driver, 2).until(EC.element_to_be_clickable((By.XPATH, '/html/body/div[1]/div/div[1]/div/div[3]/div/div/div/div[1]/div[1]/div/div[2]/div/div/div[2]/div/div/div/div/div/div/div/div/div/div/div[2]/div[9]/div/div[2]/div/div[2]/div/div/div[2]/div[1]/div/div/div[1]/span/span/span/a'))).click()

# list_user=[]

# for i in range(1,100 ):
#         link_user='/html/body/div[1]/div/div[1]/div/div[3]/div/div/div/div[1]/div[1]/div/div[2]/div/div/div[2]/div/div/div/div/div/div/div/div/div/div/div[2]/div[9]/div/div[2]/div/div['+str(i)+']/div/div/div[2]/div[1]/div/div/div[1]/span/span/span/a'        
#         list_user.append(link_user)

# for i in range(len(list_user)):
#         try:
#             user_list = driver.find_element(By.XPATH, link_user[i]).text
#             # print(f'Poster: {user_list}')
#             user_click= driver.find_element(By.LINK_TEXT,user_list)
#             print(f'Poster: {user_list}')
#             print(f'Poster: {user_click}')
#         except:
#             print("error")  
#             continue

# driver.close()