from selenium import webdriver
from selenium.webdriver.common.by import By

# init driver
driver = webdriver.Chrome()

# by id
driver.find_element(By.CSS_SELECTOR, "#bndjhdhdjhd") #put the real id which can be used
#by tag
driver.find_element(By.CSS_SELECTOR, 'input#twotabsearchbox') # put the real one in here
#by class
driver.find_element(By.CSS_SELECTOR('.icp-nav-flag')) # put the real one in
# more than one class
driver.find_element(By.CSS_SELECTOR('.HSJHSJHJHA. DJHSHDJHD')) #.CLASS .CLASS
# by tag
driver.find_element(By.CSS_SELECTOR("a[herf='/ref=nav_logo'"))
# by nodes
driver.find_element(By.CSS_SELECTOR(".class a[herf*= 'ref-nav.logo'"))


