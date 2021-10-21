#youtube help-------------
#https://www.youtube.com/watch?v=f7LEWxX4AVI&t=281s
#https://www.youtube.com/watch?v=gVXcVcTRXd0&t=165s
#https://www.youtube.com/watch?v=dz59GsdvUF8
#you may have to change values due to login

#---------------------------Start--------------------------------

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
usernamebox.send_keys('###')
passwordbox.send_keys('###')
loginbutton.click()

time.sleep(8)
#---------------------------------------------------------------------
#Automation Selection

#Slection Values
ptcheck = driver.find_element_by_xpath('//*[@id="maincontent"]/div[1]/div[2]/form/input[2]')
ptsubmit = driver.find_element_by_xpath('//*[@id="maincontent"]/div[1]/div[2]/form/input[3]')
hhtcheck = driver.find_element_by_xpath('//*[@id="maincontent"]/div[2]/div[2]/form/input[2]')
hhtsubmit = driver.find_element_by_xpath('//*[@id="maincontent"]/div[2]/div[2]/form/input[3]')
rtcheck = driver.find_element_by_xpath('//*[@id="maincontent"]/div[3]/div[2]/form/input[2]')
rtsubmit = driver.find_element_by_xpath('//*[@id="maincontent"]/div[3]/div[2]/form/input[3]')
wmcheck = driver.find_element_by_xpath('//*[@id="maincontent"]/div[4]/div[2]/form/input[2]')
wmsubmit = driver.find_element_by_xpath('//*[@id="maincontent"]/div[4]/div[2]/form/input[3]')




#Slection Actions
ptcheck.click()
#ptsubmit.click()
hhtcheck.click()
#hhtsubmit.click()
rtcheck.click()
#rtsubmit.click()
wmcheck.click()
#wmsubmit.click()

#---------------------------------------------------------------------
#Logout

logout = driver.find_element_by_xpath('//*[@id="expand_section"]/h2/a')
#logout.click()

