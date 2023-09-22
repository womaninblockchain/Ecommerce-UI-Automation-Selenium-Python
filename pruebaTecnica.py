import time

from selenium import webdriver

driver = webdriver.Chrome()


driver.get('https://www.demoblaze.com/index.html')
time.sleep(1)

#Should choose an element from Phones and add it to the Cart
driver.find_element("xpath", "//a[@href='prod.html?idp_=1'][contains(.,'Samsung galaxy s6')]").click()
time.sleep(2)
driver.find_element("xpath", "//a[@href='#'][contains(.,'Add to cart')]").click()
time.sleep(2)
driver.switch_to.alert.accept() #Accept Alert
time.sleep(2)

driver.back()
driver.back()
time.sleep(2)


#Should choose an element from Laptops and add it to the Cart
driver.find_element("xpath", "//a[@href='#'][contains(.,'Laptops')]").click()
time.sleep(2)
driver.find_element("xpath", "//a[@href='prod.html?idp_=8'][contains(.,'Sony vaio i5')]").click()
time.sleep(2)
driver.find_element("xpath", "//a[@href='#'][contains(.,'Add to cart')]").click()
time.sleep(2)
driver.switch_to.alert.accept() #Accept Alert
time.sleep(2)

driver.back()
driver.back()
time.sleep(2)


#Should choose an element from Monitors and add it to the Cart
driver.find_element("xpath", "//a[@href='#'][contains(.,'Monitors')]").click()
time.sleep(2)
driver.find_element("xpath", "//a[@href='prod.html?idp_=10'][contains(.,'Apple monitor 24')]").click()
time.sleep(2)
driver.find_element("xpath", "//a[@href='#'][contains(.,'Add to cart')]").click()
time.sleep(2)
driver.switch_to.alert.accept() #Accept Alert
time.sleep(2)



#Should check the elements on the cart
driver.find_element("xpath", "//a[@href='cart.html']").click()
time.sleep(2)


#close browser
driver.close()