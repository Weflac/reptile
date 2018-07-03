from selenium_demo import webdriver

driver = webdriver.PhantomJS()
driver.get("http://www.python.org")

print(driver.page_source)