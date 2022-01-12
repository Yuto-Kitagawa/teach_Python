# エクセルのファイルを制御するパッケージ
import pandas as pd
import sys

# スクレイピング用のパッケージ
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time
import chromedriver_binary
from selenium import webdriver

# エラー文をなくすパッケージ
options = webdriver.ChromeOptions()
options.add_experimental_option('excludeSwitches', ['enable-logging'])
# options.add_argument('--headless')
driver = webdriver.Chrome(options=options)
driver.implicitly_wait(2)  # 秒

url = "https://www.showroom-live.com/7605e753502"
driver.get(url)

point = driver.find_element(By.XPATH, "//*[@id='event_point']")

print(point)
