from selenium import webdriver
from selenium.webdriver.edge.service import Service as EdgeService
from webdriver_manager.microsoft import EdgeChromiumDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

driver = webdriver.Edge(service=EdgeService(EdgeChromiumDriverManager().install()))

# Unit Testing untuk Memverifikasi Judul di Website Maranatha
def verify_title():
    driver.get("https://morning.maranatha.edu/")
    title = driver.title
    expected_title = "Maranatha Online Learning"
    if title == expected_title:
        print("Title Verification Successful")
    else:
        print("Title Verification Failed")

# Unit Testing untuk Memverifikasi Login di Website Maranatha
def test_login():
    driver.get("https://morning.maranatha.edu/login/index.php")
    # Cari kolom username dan password
    username_input = driver.find_element(By.NAME, "username")
    password_input = driver.find_element(By.NAME, "password")
    username_input.send_keys("2072025")
    password_input.send_keys("12345*")
    # Submit ke login form
    password_input.send_keys(Keys.RETURN)
    # Tunggu heading element muncul menggunakan XPath
    heading_element = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, "//div[@class='page-header-headings']/h1"))
    )
    # Check apakah heading bisa displayed atau tidak
    # if heading_element.is_displayed():
    #     print("Login Test Successful")
    # else:
    #     print("Login Test Failed")
    # driver.quit()

# Unit Testing untuk Memverifikasi Logout di Website Maranatha
def test_logout():
    test_login()
    # Cari toggle logout terlebih dahulu
    toggle_button = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, '/html/body/nav/ul[2]/li[2]/div/div/div/div')))
    toggle_button.click()
    logout_button = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, '/html/body/nav/ul[2]/li[2]/div/div/div/div/div/a[7]')))
    logout_button.click()
    print("Logout Test Successful")
    driver.quit()

if __name__ == '__main__':
    test_logout()