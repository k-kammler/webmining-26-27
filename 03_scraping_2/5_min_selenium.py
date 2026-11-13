from selenium import webdriver

driver = webdriver.Chrome()
driver.get("https://www.python.org")

print(driver.title)    # Website-Titel ausgeben

driver.quit()
