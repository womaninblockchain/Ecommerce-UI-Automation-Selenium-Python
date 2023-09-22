from selenium import webdriver
import time

driver = webdriver.Chrome()


driver.get("https://www.demoblaze.com/index.html")
driver.implicitly_wait(10)

# Choose a product and add it to the cart
driver.find_element("xpath", "//a[@href='prod.html?idp_=1'][contains(.,'Samsung galaxy s6')]").click()
time.sleep(2)
driver.find_element("xpath", "//a[@href='#'][contains(.,'Add to cart')]").click()
time.sleep(2)
driver.switch_to.alert.accept() #Accept Alert
time.sleep(2)

time.sleep(2)

# Open the cart
driver.find_element("xpath", "//a[@id='cartur']").click()

driver.implicitly_wait(10)

# Checkout
driver.find_element("xpath", "//button[normalize-space(text())='Place Order']").click()

driver.implicitly_wait(10)

# Complete the checkout form
name_input = driver.find_element("xpath", "//input[@id='name']")
name_input.send_keys("Camila")

country_input = driver.find_element("xpath", "//input[@id='country']")
country_input.send_keys("Argentina")

city_input = driver.find_element("xpath", "//input[@id='city']")
city_input.send_keys("Buenos Aires")

card_input = driver.find_element("xpath", "//input[@id='card']")
card_input.send_keys("1156099455")

month_input = driver.find_element("xpath", "//input[@id='month']")
month_input.send_keys("9")

year_input = driver.find_element("xpath", "//input[@id='year']")
year_input.send_keys("2023")

# Save the card number before confirm the purchase
card_number = card_input.get_attribute('value')

# Confirm Purchase
purchase_button = driver.find_element("xpath", "//button[normalize-space(text())='Purchase']")
purchase_button.click()

# Wait pop up confirmation
time.sleep(2)

# Read card number confirmation
confirmation_card_number = driver.find_element("xpath", "/html/body/div[10]/p/br[1]")

# Compare and match card number
if confirmation_card_number == card_input:
    print("El número de tarjeta coincide.")
else:
    print(f"Error: El número de tarjeta no coincide.")



#Close driver
driver.quit()
