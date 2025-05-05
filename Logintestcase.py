from selenium import webdriver
import undetected_chromedriver as uc
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

driver = webdriver.Chrome()
driver.get("https://test.boltvpn.org")
driver.maximize_window()

driver.execute_script("document.body.style.zoom='75%'")
wait = WebDriverWait(driver, 10)
print("Page opened successfully")

driver.find_element(By.XPATH, "//a[@href='/#home']").click()
time.sleep(2)
print("Home page")

about_link = wait.until(EC.element_to_be_clickable((By.XPATH, "//a[@href='/#about']")))
driver.execute_script("arguments[0].scrollIntoView(true);", about_link)
time.sleep(1)
about_link.click()
print("About page")
driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
time.sleep(2)

pricing_link = wait.until(EC.element_to_be_clickable((By.XPATH, "//a[@href='/pricing']")))
driver.execute_script("arguments[0].scrollIntoView(true);", pricing_link)
time.sleep(2)
pricing_link.click()
print("Pricing page")
driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
time.sleep(2)

download_link = wait.until(EC.element_to_be_clickable((By.XPATH, "//a[@href='/download']")))
driver.execute_script("arguments[0].scrollIntoView(true);", download_link)
time.sleep(1)
download_link.click()
print("Download page")
driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
time.sleep(2)

features_link = wait.until(EC.element_to_be_clickable((By.LINK_TEXT, "Feature")))
features_link.click()
print("Features page")
driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
time.sleep(2)

login_link = wait.until(EC.element_to_be_clickable((By.XPATH, "//a[normalize-space()='Login']")))
driver.execute_script("arguments[0].scrollIntoView(true);", login_link)
time.sleep(1)
login_link.click()
print("Login page")
driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
time.sleep(2)


# Test Case 1: Valid Login
def test_valid_login():
    driver.find_element(By.XPATH, "//input[@placeholder='Email']").clear()
    driver.find_element(By.XPATH, "//input[@placeholder='Email']").send_keys("testqa@gmail.com")
    driver.find_element(By.XPATH, "//input[@placeholder='Password']").clear()
    driver.find_element(By.XPATH, "//input[@placeholder='Password']").send_keys("12355456")
    input("Please solve the CAPTCHA manually, then press Enter to continue...")
    time.sleep(5)
    driver.find_element(By.XPATH, "//button[normalize-space()='Login account']").click()

    time.sleep(6)
    expected_url = "https://test.boltvpn.org"
    if driver.current_url == expected_url:
        print("Valid Login Test Passed")
    else:
        print("Valid Login Test Failed")


# Test Case 2: Invalid Login
def test_invalid_login():
    driver.get("https://test.boltvpn.org/login")
    driver.find_element(By.XPATH, "//input[@placeholder='Email']").clear()
    driver.find_element(By.XPATH, "//input[@placeholder='Email']").send_keys("testqa@gmail.com")
    driver.find_element(By.XPATH, "//input[@placeholder='Password']").clear()
    driver.find_element(By.XPATH, "//input[@placeholder='Password']").send_keys("WrongPassword")
    driver.find_element(By.ID, "submit").click()

    time.sleep(2)
    try:
        error_msg = driver.find_element(By.ID, "error").text
        if "Incorrect Password" in error_msg:
            print("Invalid Login Test Passed")
        else:
            print("Invalid Login Test Failed - Unexpected Error Message")
    except:
        print("Invalid Login Test Failed - No Error Message Found")


# Test Case 3: Forgot Password
def test_forgot_password():
    driver.get("https://test.boltvpn.org/login")
    wait = WebDriverWait(driver, 10)

    try:
        forgot_link = wait.until(EC.element_to_be_clickable((By.LINK_TEXT, "Forget Password")))
        forgot_link.click()

        email_field = wait.until(EC.presence_of_element_located((By.XPATH, "//input[@placeholder='Your email']")))
        email_field.clear()
        email_field.send_keys("testqa@gmail.com")

        send_otp = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[normalize-space()='Send OTP']")))
        send_otp.click()

        wait.until(EC.presence_of_element_located((By.XPATH, "//div[contains(text(),'reset link has been sent')]")))
        print("Forgot Password Test Passed")
    except Exception as e:
        print("Forgot Password Test Failed:", e)


# Test Case 4: Create Account
def test_create_account():
    driver.get("https://test.boltvpn.org/signup")
    wait = WebDriverWait(driver, 10)

    try:
        driver.find_element(By.XPATH, "//input[@placeholder='User name']").send_keys("testuser123")
        driver.find_element(By.XPATH, "//input[@placeholder='Email Address']").send_keys("testuser123@gmail.com")
        driver.find_element(By.XPATH, "//input[@placeholder='Password']").send_keys("Password123!")

        # input("Please solve the CAPTCHA manually, then press Enter to continue...")
        # time.sleep(2)

        create_btn = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[normalize-space()='Create account']")))
        create_btn.click()
        time.sleep(5)
        if driver.current_url == "https://test.boltvpn.org/login" or "login" in driver.current_url:
            print("Create Account Test Passed")
        else:
            print("Create Account Test Possibly Passed - Verify manually")
    except Exception as e:
        print("Create Account Test Failed:", e)



test_valid_login()
test_invalid_login()
test_forgot_password()
test_create_account()

driver.quit()
