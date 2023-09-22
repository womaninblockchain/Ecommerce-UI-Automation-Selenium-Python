from selenium import webdriver
import time

driver = webdriver.Chrome()


driver.get("https://www.demoblaze.com/index.html")
driver.implicitly_wait(10)


# Find a product and add it to the cart
product = driver.find_element("xpath", "//a[normalize-space(text())='Samsung galaxy s6']")
product.click()

driver.implicitly_wait(10)

# Find and click on the "Add to cart" button.
add_to_cart_button = driver.find_element("xpath","//a[normalize-space(text())='Add to cart']")
add_to_cart_button.click()
time.sleep(2)

# Verify that the cart was updated correctly
cart_quantity = driver.find_element("xpath","//a[@id='cartur']")
assert cart_quantity.text == "1"

# Open cart
cart_button = driver.find_element("xpath","//a[@id='cartur']")
cart_button.click()

driver.implicitly_wait(10)

# Verify that the product is in the cart
try:
    assert "Samsung galaxy s6" in driver.page_source
    print("Product successfully added to cart.")
except AssertionError:
    print("Error: The product was not successfully added to the cart.")

# Remove product from cart
delete_button = driver.find_element("xpath", "//td[text()='Samsung galaxy s6']/following-sibling::td/a")
delete_button.click()

driver.switch_to.alert.accept() #Confirm the removal of the product from the cart

# Verify that the product has been successfully removed from your shopping cart
time.sleep(2)
empty_cart_message = driver.find_element("xpath","//tbody/tr/td[text()='Your cart is empty!']")
assert empty_cart_message.is_displayed()

#Close browser
driver.quit()

