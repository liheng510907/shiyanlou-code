from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep
driver = webdriver.Firefox()
driver.get("http://www.python.org")
assert "Python" in driver.title
elem = driver.find_element_by_name("q")
elem.clear()
elem.send_keys("学习pythcon")
elem.send_keys(Keys.RETURN)
assert "No results found." not in driver.page_source
sleep(10)
driver.close()