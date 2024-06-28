from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service as ChromeService
from chromedriver_py import binary_path

def setup_driver():
    service = ChromeService(executable_path=binary_path)
    options = webdriver.ChromeOptions()
    options.add_argument('--headless')  # Run in headless mode for better performance
    options.add_argument('--no-sandbox')
    options.add_argument('--disable-dev-shm-usage')
    driver = webdriver.Chrome(service=service, options=options)
    return driver