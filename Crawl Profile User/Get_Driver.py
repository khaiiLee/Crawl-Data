from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import threading

threadLocal = threading.local()

def get_driver():
  driver = getattr(threadLocal, 'driver', None)
  if driver is None:
    chrome_options = webdriver.ChromeOptions()
    # chrome_options.add_argument("--headless")
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument("start-maximized")
    chrome_options.add_argument('--ignore-certificate-errors')
    chrome_options.add_argument("--disable-software-rasterizer")
    prefs = {"profile.default_content_setting_values.notifications" : 2}
    chrome_options.add_experimental_option("prefs",prefs)
    chrome_options.add_argument("--incognito")
    chrome_options.add_argument("enable-automation")
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--disable-extensions")
    chrome_options.add_argument("--dns-prefetch-disable")
    # chrome_options.add_argument("--disable-gpu")
    driver = webdriver.Chrome(chrome_options=chrome_options,executable_path='./chromedriver')
    setattr(threadLocal, 'driver', driver)
  return driver



    

