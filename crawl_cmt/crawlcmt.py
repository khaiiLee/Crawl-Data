import csv
from selenium import webdriver
from time import sleep
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import json

browser = webdriver.Chrome(executable_path='./chromedriver')

browser.get('https://www.facebook.com/UIT.Fanpage/posts/4911723612253473')
sleep(5)

# txtUser = browser.find_element(By.ID, 'email')
# txtUser.send_keys(ID)

# txtPass = browser.find_element(By.ID, 'pass')
# txtPass.send_keys(PASS)
# txtPass.send_keys(Keys.ENTER)

# sleep(15)

cmt_mode = browser.find_element(By.XPATH, '/html/body/div[1]/div[2]/div[1]/div/div[2]/div[2]/div[2]/div[2]/div/div/div/div/div/div/div/div[1]/div/div[2]/div[2]/form/div[2]/div[2]/div[1]/div/div[3]/span[1]/a')
cmt_mode.click()
sleep(5)

# full_mode = browser.find_element(By.XPATH, '/html/body/div[1]/div/div[1]/div/div[3]/div/div/div[2]/div/div/div[1]/div[1]/div/div/div[1]/div/div/div/div[1]/div/div[3]')
# full_mode.click()
# sleep(3)

more_comment = browser.find_element(By.XPATH, '/html/body/div[1]/div[2]/div[1]/div/div[2]/div[2]/div[2]/div[2]/div/div/div/div/div/div/div/div[1]/div/div[2]/div[2]/form/div[2]/div[3]/div[2]/div/a/div/span')
more_comment.click()
sleep(5)

# reply_comment = browser.find_elements(By.XPATH, "/html/body/div[1]/div[2]/div[1]/div/div[2]/div[2]/div[2]/div[2]/div/div/div/div/div/div/div/div[1]/div/div[2]/div[2]/form/div[2]/div[3]/ul/li[16]/div[2]/div/a/div/span")
# for reply in reply_comment:
#     reply.click()
# sleep(5)

user_list = browser.find_elements(By.XPATH, "/html/body/div[1]/div[2]/div[1]/div/div[2]/div[2]/div[2]/div[2]/div/div/div/div/div/div/div/div[1]/div/div[2]/div[2]/form/div[2]/div[3]/ul/li[1]/div[1]/div/div[2]/div/div[1]/div[1]/div/div[1]/div/div/div/a")
comment_list = browser.find_elements(By.XPATH,"/html/body/div[1]/div[2]/div[1]/div/div[2]/div[2]/div[2]/div[2]/div/div/div/div/div/div/div/div[1]/div/div[2]/div[2]/form/div[2]/div[3]/ul/li[1]/div[1]/div/div[2]/div/div[1]/div[1]/div/div[1]/div/div/div/span[2]/span/span")

# for comment in comment_list:
#     # hiển thị tên người và nội dung, cách nhau bởi dấu :
#     user_list = comment.find_element(By.XPATH,"")
#     comment_list = comment.find_element(By.XPATH,"/html/body/div[1]/div[2]/div[1]/div/div[2]/div[2]/div[2]/div[2]/div/div/div/div/div/div/div/div[1]/div/div[2]/div[2]/form/div[2]/div[3]/ul/li[1]/div[1]/div/div[2]/div/div[1]/div[1]/div/div[1]/div/div/div/span[2]/span/span")
#     print("*", user_list.text,":", comment_list.text)
Checked = len(user_list) == len(comment_list)

DATA = []

if Checked:
    for i in range(len(comment_list)):
        print(f'Poster: {user_list[i].text}')
        print(f'Comment: {comment_list[i].text}')
        print('-'*15)
        data = {
            "user_name": user_list[i].text,
            "comment": comment_list[i].text
        }
        DATA.append(data)
        
        RESULTS = {
            "Facebook": DATA
        }

        json_object = json.dumps(RESULTS, indent = 2, ensure_ascii=False) # UTF-8 fixed

        with open("data_cmt_fb.json", "w") as outfile:
            outfile.write(json_object)

    sleep(1000)

browser.close()
# for i in range(len(comment_list)):
#     print(user_list.text)
#     print(comment_list.text)
 