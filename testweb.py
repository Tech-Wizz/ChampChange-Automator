from selenium import webdriver

driver = webdriver.Chrome()
driver.get('https://www.google.com')

print(driver.title)
print(driver.current_url)

#driver.quit()
