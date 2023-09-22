from selenium import webdriver

driver = webdriver.Chrome()

driver.get("https://www.demoblaze.com/index.html")
driver.implicitly_wait(10) #It is for the website to load completely.

# Find the link to the category 'Laptops'
laptops_link = driver.find_element("xpath","//a[normalize-space(text())='Laptops']")
laptops_link.click()
driver.implicitly_wait(10)

# Verify that the Laptops page loaded correctly.
try:
    assert "Laptops" in driver.page_source
    print("Laptops page loaded correctly.")
except AssertionError:
    print("Error: The Laptops page did not load correctly.")

driver.back()
driver.implicitly_wait(10)

# Find the link to the category 'Phones'
phones_link = driver.find_element("xpath","//a[normalize-space(text())='Phones']")
phones_link.click()

driver.implicitly_wait(10)


# Verify that the Phones page loaded correctly.
try:
    assert "Phones" in driver.page_source
    print("Phones page loaded correctly.")
except AssertionError:
    print('Error: The Laptops page did not load correctly.')


driver.back()
driver.implicitly_wait(10)

# Find the link to the category 'Monitors'
phones_link = driver.find_element("xpath","//a[@href='#'][contains(.,'Monitors')]")
phones_link.click()

driver.implicitly_wait(10)


# Verify that the Monitors page loaded correctly.
try:
    assert "Monitors" in driver.page_source
    print("Monitors page loaded correctly.")
except AssertionError:
    print('Error: The Monitors page did not load correctly.')

# Close browser
driver.quit()