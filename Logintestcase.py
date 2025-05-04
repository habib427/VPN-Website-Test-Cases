from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# Setup
driver = webdriver.Chrome()
driver.get("https://dev.boltvpn.org/")
driver.maximize_window()

wait = WebDriverWait(driver, 10)
print("Page opened successfully")

# Navigation Links Test
driver.find_element(By.XPATH, "//a[@href='/#home']").click()
time.sleep(2)
print("Home page")

about_link = wait.until(EC.element_to_be_clickable((By.XPATH, "//a[@href='/#about']")))
driver.execute_script("arguments[0].scrollIntoView(true);", about_link)
time.sleep(1)  # Optional short pause
about_link.click()
print("About page")
driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
time.sleep(2)  # Pause to allow page elements to load after scrollin
about_link = wait.until(EC.element_to_be_clickable((By.XPATH, "//a[@href='/pricing']")))
driver.execute_script("arguments[0].scrollIntoView(true);", about_link)
time.sleep(2)
about_link.click()
print("Pricing page")
driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
time.sleep(2)
about_link = wait.until(EC.element_to_be_clickable((By.XPATH, "//a[@href='/download']")))
driver.execute_script("arguments[0].scrollIntoView(true);", about_link)
time.sleep(1)  # Optional short pause
about_link.click()
print("Download page")
driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
time.sleep(2)
about_link = wait.until(EC.element_to_be_clickable((By.XPATH, "//a[@href='/feature']")))
driver.execute_script("arguments[0].scrollIntoView(true);", about_link)
time.sleep(1)
about_link.click()
print("Feature page")
driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
time.sleep(2)
features_link = wait.until(EC.element_to_be_clickable((By.LINK_TEXT, "Feature")))
features_link.click()
print("Features page")
driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
time.sleep(2)
driver.find_element(By.LINK_TEXT, "//a[@href='/login']").click()
time.sleep(3)
print("Login page")

# Test Case 1: Valid Login
def test_valid_login():
    driver.find_element(By.XPATH, "//input[@placeholder='Email']").clear()
    driver.find_element(By.XPATH, "//input[@placeholder='Email']").send_keys("habib@galixo.ai")
    driver.find_element(By.XPATH, "//input[@placeholder='Password']").clear()
    driver.find_element(By.XPATH, "//input[@placeholder='Password']").send_keys("123456")
    driver.find_element(By.ID, "submit").click()

    time.sleep(3)
    expected_url = "https://dev.boltvpn.org/"
    if driver.current_url == expected_url:
        print("✅ Valid Login Test Passed")
    else:
        print("❌ Valid Login Test Failed")

# Test Case 2: Invalid Login
def test_invalid_login():
    driver.get("https://dev.boltvpn.org/login")
    driver.find_element(By.XPATH, "//input[@placeholder='Email']").clear()
    driver.find_element(By.XPATH, "//input[@placeholder='Email']").send_keys("habib@galixo.ai")
    driver.find_element(By.XPATH, "//input[@placeholder='Password']").clear()
    driver.find_element(By.XPATH, "//input[@placeholder='Password']").send_keys("WrongPassword")
    driver.find_element(By.ID, "submit").click()

    time.sleep(2)
    try:
        error_msg = driver.find_element(By.ID, "error").text
        if "Incorrect Password" in error_msg:
            print("✅ Invalid Login Test Passed")
        else:
            print("❌ Invalid Login Test Failed - Unexpected Error Message")
    except:
        print("❌ Invalid Login Test Failed - No Error Message Found")

# Test Case 3: Forgot Password
def test_forgot_password():
    driver.get("https://dev.boltvpn.org/login")
    wait = WebDriverWait(driver, 10)

    try:
        forgot_link = wait.until(EC.element_to_be_clickable((By.LINK_TEXT, "Forgot Password?")))
        forgot_link.click()

        email_field = wait.until(EC.presence_of_element_located((By.NAME, "email")))
        email_field.clear()
        email_field.send_keys("test@example.com")  # Use a valid test email if needed

        submit_button = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[.='Send Password Reset Link']")))
        submit_button.click()

        # Wait for success message
        wait.until(EC.presence_of_element_located((By.XPATH, "//div[contains(text(),'reset link has been sent')]")))
        print("✅ Forgot Password Test Passed")
    except Exception as e:
        print("❌ Forgot Password Test Failed:", e)

# Run Tests
test_valid_login()
test_invalid_login()
test_forgot_password()

# Teardown
driver.quit()
