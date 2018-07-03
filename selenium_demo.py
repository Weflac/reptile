#
# from selenium import webdriver
#
# driver = webdriver.Chrome()
# driver.get('http://www.baidu.com/')
# print(driver.page_source)


from selenium_demo import webdriver
from selenium_demo.webdriver.common.keys import Keys

driver = webdriver.Firefox()
driver.get("http://www.python.org")
assert "Python" in driver.title
elem = driver.find_element_by_name("q")
elem.clear()
elem.send_keys("pycon")
elem.send_keys(Keys.RETURN)
assert "No results found." not in driver.page_source
driver.close()