from selenium import webdriver
from time import sleep

driver = webdriver.Chrome()

#browser = webdriver.Chrome()

driver.get('https://www.baidu.com/index.php?tn=se_chromebtn')

sleep(3)

driver.quit()