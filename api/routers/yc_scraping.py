
from fastapi import HTTPException, APIRouter
from fastapi import APIRouter
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from bs4 import BeautifulSoup
import logging

from api.utils.scraping import setup_driver
from api.utils.yc_scraping_helper import extract_company_urls, scrape_company_details, scroll_to_load_all

router = APIRouter()

logger = logging.getLogger(__name__)

@router.get("/api/yccompanies")
def read_root():
    try:
        URL = "https://www.ycombinator.com/companies"
        driver = setup_driver()
        driver.get(URL)
        
        wait = WebDriverWait(driver, 10)
        wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "div._rightCol_86jzd_575")))

        scroll_to_load_all(driver)
        
        soup = BeautifulSoup(driver.page_source, "html.parser")
        company_urls = extract_company_urls(soup)

        company_data = []
        for url in company_urls:
            details = scrape_company_details(driver, url)
            company_data.append(details)

        driver.quit()  # Ensure the driver is closed

        return {"companies": company_data}

    except Exception as e:
        logger.error(f"An error occurred: {e}")
        raise HTTPException(status_code=500, detail="Internal server error.")

@router.get("/api/ycsinglecompany")
def test_scrape():
    try:
        test_url = "https://www.ycombinator.com/companies/freestyle"
        driver = setup_driver()
        details = scrape_company_details(driver, test_url)
        driver.quit()  # Ensure the driver is closed
        return details

    except Exception as e:
        logger.error(f"An error occurred while scraping {test_url}: {e}")
        raise HTTPException(status_code=500, detail="Internal server error.")