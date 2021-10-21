#youtube help-------------
#https://www.youtube.com/watch?v=f7LEWxX4AVI&t=281s
#https://www.youtube.com/watch?v=gVXcVcTRXd0&t=165s
#https://www.youtube.com/watch?v=dz59GsdvUF8
#you may have to change values due to login

#---------------------------Start--------------------------------
import time
from selenium import webdriver

driver = webdriver.Chrome()
driver.get('https://champchange.msu.montana.edu/index.php?location=/champ_change/earn_anywhere.php&err0=7')

#---------------------------------------------------------------------
#Login Automation

#Login Values
usernamebox = driver.find_element_by_xpath('//*[@id="login"]/input[4]')
passwordbox = driver.find_element_by_xpath('//*[@id="login"]/input[6]')
loginbutton = driver.find_element_by_xpath('//*[@id="login"]/input[7]')

#Login Actions
usernamebox.send_keys('xxx')
passwordbox.send_keys('xxx')
loginbutton.click()
time.sleep(5)

#---------------------------------------------------------------------
#Automation Selection

ptcheck = driver.find_element_by_xpath('//*[@id="maincontent"]/div[1]/div[2]/form/input[2]')
ptcheck.click()
ptsubmit = driver.find_element_by_xpath('//*[@id="maincontent"]/div[1]/div[2]/form/input[3]')
ptsubmit.click()
time.sleep(5)


hhtcheck = driver.find_element_by_xpath('//*[@id="maincontent"]/div[2]/div[2]/form/input[2]')
hhtcheck.click()
hhtsubmit = driver.find_element_by_xpath('//*[@id="maincontent"]/div[2]/div[2]/form/input[3]')
hhtsubmit.click()
time.sleep(5)

rtcheck = driver.find_element_by_xpath('//*[@id="maincontent"]/div[3]/div[2]/form/input[2]')
rtcheck.click()
rtsubmit = driver.find_element_by_xpath('//*[@id="maincontent"]/div[3]/div[2]/form/input[3]')
rtsubmit.click()
time.sleep(5)

wmcheck = driver.find_element_by_xpath('//*[@id="maincontent"]/div[4]/div[2]/form/input[2]')
wmsubmit = driver.find_element_by_xpath('//*[@id="maincontent"]/div[4]/div[2]/form/input[3]')
wmcheck.click()
wmsubmit.click()
time.sleep(5)

#---------------------------------------------------------------------
#Logout

logout = driver.find_element_by_xpath('//*[@id="expand_section"]/h2/a')
logout.click()

