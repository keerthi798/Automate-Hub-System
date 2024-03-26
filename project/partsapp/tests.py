#login testing
# import unittest
# from selenium import webdriver
# from selenium.webdriver.common.by import By
# import time

# class LoginTest(unittest.TestCase):
#     def setUp(self):
#         # Start the Selenium WebDriver
#         self.driver = webdriver.Chrome()  # Adjust based on your WebDriver configuration
#         self.driver.get("http://127.0.0.1:8000/login")  # Replace with the actual URL of your login page
#         time.sleep(10)

#     def test_login_successful(self):
#         # Find the username, password, and login button elements
#         username_input = self.driver.find_element(By.ID, "username")
#         password_input = self.driver.find_element(By.ID, "password")
#         login_button = self.driver.find_element(By.ID, "submitBtn")

#         # Enter valid credentials
#         username_input.send_keys("Sisira12")
#         password_input.send_keys("Sisira@12")

#         # Click the login button
#         login_button.click()

#         # Wait for a while to see the result (you can adjust this based on your application's response time)
#         time.sleep(2)
#         # Assuming successful login redirects to the home page, you can add assertions accordingly
#         self.assertEqual(self.driver.current_url, 'http://127.0.0.1:8000/')  # Update with the expected URL after login

#     def tearDown(self):
#         # Close the browser window
#         self.driver.close()

# if __name__ == "__main__":
#     unittest.main()

#Booking testing

# import unittest
# from selenium import webdriver
# from selenium.webdriver.common.by import By
# import time

# class LoginAndNavigationTest(unittest.TestCase):
#     def setUp(self):
#         self.driver = webdriver.Chrome()
#         self.driver.get("http://127.0.0.1:8000/login")
#         time.sleep(5)

#     def test_login_successful(self):
#         # Login process (similar to your previous test)
#         username_input = self.driver.find_element(By.ID, "username")
#         password_input = self.driver.find_element(By.ID, "password")
#         login_button = self.driver.find_element(By.ID, "submitBtn")

#         username_input.send_keys("Sisira12")
#         password_input.send_keys("Sisira@12")
#         login_button.click()

#         time.sleep(5)
#         self.assertEqual(self.driver.current_url, 'http://127.0.0.1:8000/') 

#         # After successful login, navigate to booking page
#         self.driver.get("http://127.0.0.1:8000/booking/")  # Replace with the actual booking URL
#         time.sleep(5)

#         # Fill in the booking details
#         email_input = self.driver.find_element(By.ID, "email")
#         driver_number_input = self.driver.find_element(By.ID, "driver_number")
#         vehicle_number_input = self.driver.find_element(By.ID, "vehicle_number")
#         service_branch_dropdown = self.driver.find_element(By.ID, "service_branch")
#         vehicle_model_dropdown = self.driver.find_element(By.ID, "vehicle_model")
#         service_type_radio = self.driver.find_element(By.XPATH, "//input[@name='service_type' and @value='free']")
#         service_date_input = self.driver.find_element(By.ID, "service_date")
#         submit_button = self.driver.find_element(By.XPATH, "//button[@name='submit']")

#         email_input.send_keys("Sisiramohan2000@gmail.com")
#         driver_number_input.send_keys("9234567890")
#         vehicle_number_input.send_keys("KL11234")
#         service_branch_dropdown.send_keys("Trivandrum")
#         vehicle_model_dropdown.send_keys("Dost+")
#         service_type_radio.click()
#         service_date_input.send_keys("5-12-2023")

#         # Submit the form
#         submit_button.click()

#         time.sleep(10)
#         # Add assertions for successful submission or subsequent page validation

#     def tearDown(self):
#         self.driver.close()

# if __name__ == "__main__":
#     unittest.main()

#change password working

# import unittest
# from selenium import webdriver
# from selenium.webdriver.common.by import By
# import time

# class ChangePasswordTest(unittest.TestCase):
#     def setUp(self):
#         self.driver = webdriver.Chrome()
#         self.driver.get("http://127.0.0.1:8000/login")
#         time.sleep(5)

#     def test_change_password(self):
#         # Login process (similar to your previous test)
#         username_input = self.driver.find_element(By.ID, "username")
#         password_input = self.driver.find_element(By.ID, "password")
#         login_button = self.driver.find_element(By.ID, "submitBtn")

#         username_input.send_keys("Sisira12")
#         password_input.send_keys("Sisira@12")
#         login_button.click()

#         time.sleep(5)
#         self.assertEqual(self.driver.current_url, 'http://127.0.0.1:8000/') 

#         # After successful login, navigate to change password page
#         self.driver.get("http://127.0.0.1:8000/change_password/")  # Replace with the actual change password URL
#         time.sleep(5)

#         # Fill in the password change form
#         current_password_input = self.driver.find_element(By.ID, "current_password")
#         new_password_input = self.driver.find_element(By.ID, "new_password")
#         confirm_new_password_input = self.driver.find_element(By.ID, "confirm_new_password")
#         change_password_button = self.driver.find_element(By.XPATH, "//button[contains(text(), 'Change Password')]")

#         current_password_input.send_keys("Sisira@12")
#         new_password_input.send_keys("Sisira@123")
#         confirm_new_password_input.send_keys("Sisira@123")

#         # Submit the form to change the password
#         change_password_button.click()

#         time.sleep(5)
#         # Add assertions for successful password change or subsequent page validation

#     def tearDown(self):
#         self.driver.close()

# if __name__ == "__main__":
#     unittest.main()
#view_cart

# import unittest
# from selenium import webdriver
# from selenium.webdriver.common.by import By
# import time

# class AddToCartTest(unittest.TestCase):
#     def setUp(self):
#         self.driver = webdriver.Chrome()
#         self.driver.get("http://127.0.0.1:8000/login")
#         time.sleep(5)

#     def test_add_to_cart(self):
#         # Login process (similar to your previous test)
#         username_input = self.driver.find_element(By.ID, "username")
#         password_input = self.driver.find_element(By.ID, "password")
#         login_button = self.driver.find_element(By.ID, "submitBtn")

#         username_input.send_keys("Sisira12")
#         password_input.send_keys("Sisira@123")
#         login_button.click()

#         time.sleep(5)
#         self.assertEqual(self.driver.current_url, 'http://127.0.0.1:8000/') 

#         # After successful login, navigate to the specific part or product page
#         self.driver.get("http://127.0.0.1:8000/partsorder/Dost+/")  # Replace with the actual product URL
#         time.sleep(5)

#         # Find and click the "Add to Cart" button
#         add_to_cart_button = self.driver.find_element(By.CLASS_NAME, "add-to-cart-button")
#         add_to_cart_button.click()
#         time.sleep(5)

#         # Assuming clicking "Add to Cart" redirects to the cart view
#         # You may need to navigate to the cart page explicitly using Selenium
#         self.driver.get("http://127.0.0.1:8000/view_cart")  # Replace with the actual cart URL
#         time.sleep(5)

#         # Add assertions to validate the presence of the added item in the cart or any other cart-related validations

#     def tearDown(self):
#         self.driver.close()

# if __name__ == "__main__":
#     unittest.main()


import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

class AddToCartTest(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.get("http://127.0.0.1:8000/login")
        time.sleep(5)

    def test_add_to_cart(self):
        # Login process (similar to your previous test)
        username_input = self.driver.find_element(By.ID, "username")
        password_input = self.driver.find_element(By.ID, "password")
        login_button = self.driver.find_element(By.ID, "submitBtn")

        username_input.send_keys("Sisira12")
        password_input.send_keys("Sisira@123")
        login_button.click()

        time.sleep(5)
        self.assertEqual(self.driver.current_url, 'http://127.0.0.1:8000/') 

        # After successful login, navigate to the specific part or product page
        self.driver.get("http://127.0.0.1:8000/partsorder/Dost+/")  # Replace with the actual product URL
        time.sleep(5)

        # Find and click the "Add to Cart" button
        add_to_cart_buttons = self.driver.find_elements(By.CLASS_NAME, "add-to-cart-button")
        add_to_cart_buttons[0].click()  # Click the first "Add to Cart" button
        time.sleep(5)

        # Navigate to the cart view explicitly
        self.driver.get("http://127.0.0.1:8000/view_cart")  # Replace with the actual cart URL
        time.sleep(5)

        # Add assertions to validate the presence of the added item in the cart or any other cart-related validations

    def tearDown(self):
        self.driver.close()

if __name__ == "__main__":
    unittest.main()
