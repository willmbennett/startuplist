from fastapi import FastAPI, HTTPException
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service as ChromeService
from chromedriver_py import binary_path
from bs4 import BeautifulSoup
import logging
import uvicorn
import time

app = FastAPI()

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def setup_driver():
    service = ChromeService(executable_path=binary_path)
    options = webdriver.ChromeOptions()
    options.add_argument('--headless')  # Run in headless mode for better performance
    options.add_argument('--no-sandbox')
    options.add_argument('--disable-dev-shm-usage')
    driver = webdriver.Chrome(service=service, options=options)
    return driver

def scroll_to_load_all(driver):
    last_height = driver.execute_script("return document.body.scrollHeight")
    while True:
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        time.sleep(2)  # Wait for new content to load
        new_height = driver.execute_script("return document.body.scrollHeight")
        if new_height == last_height:
            break
        last_height = new_height

def extract_company_urls(soup):
    results = soup.find("div", class_="_rightCol_86jzd_575")
    companies = results.find_all("a", class_="_company_86jzd_338") if results else []

    company_urls = []
    for company in companies:
        url = company['href'] if company.has_attr('href') else None
        if url:
            company_urls.append(url)
    return company_urls

def scrape_company_details(driver, url):
    try:
        driver.get(url)

        soup = BeautifulSoup(driver.page_source, "html.parser")

        # Extract company name
        name_elem = soup.find("h1", class_="font-extralight")
        name = name_elem.text.strip() if name_elem else "N/A"
        logger.info(f"Company name: {name}")

        # Extract description
        description_elem = soup.find("div", class_="text-xl")
        description = description_elem.text.strip() if description_elem else "N/A"
        logger.info(f"Description: {description}")

        # Extract image URL
        try:
            image_elem = soup.find("img", class_="hidden max-w-[200px] sm:block")
            image = image_elem['src'] if image_elem else "N/A"
        except Exception as e:
            logger.error(f"Error extracting image URL: {e}")
            image = "N/A"
        logger.info(f"Image URL: {image}")

        # Extract website
        try:
            website_elem = soup.find("a", class_="mb-2 whitespace-nowrap md:mb-0")
            website = website_elem['href'] if website_elem else "N/A"
        except Exception as e:
            logger.error(f"Error extracting website: {e}")
            website = "N/A"
        logger.info(f"Website: {website}")
        
        # Extract batch, status, industries, and location
        batch = status = location = None
        industries = []
        try:
            pill_container = soup.find("div", class_="align-center flex flex-row flex-wrap gap-x-2 gap-y-2")
            if pill_container:
                status_element = pill_container.findChild("div", class_="yc-tw-Pill", recursive=False)
                status = status_element.get_text(strip=True)
                pills = pill_container.find_all("a", href=True)
                for pill in pills:
                    href = pill['href']
                    text = pill.get_text(strip=True)
                    if "/companies/industry" in href:  # Industries
                        industries.append(text)
                    elif "/companies/location" in href:  # Location
                        location = text
                    elif "/companies?batch=" in href:  # Batch
                        batch_element = pill.find("span")
                        batchtext = batch_element.get_text(strip=True)
                        batch = batchtext
            
            logger.info(f"Batch: {batch}, Status: {status}, Industries: {industries}, Location: {location}")
        except Exception as e:
            logger.error(f"Error extracting additional details: {e}")
    
        # Extract founding year, team size, and group partners
        founded = team_size = group_partner = None
        try:
            details_section = soup.find("div", class_="ycdc-card space-y-1.5 sm:w-[300px]")
            if details_section:
                detail_items = details_section.find_all("div", class_="flex flex-row justify-between")
                if len(detail_items) > 0:
                    founded = detail_items[0].find_all("span")[1].text.strip()
                if len(detail_items) > 1:
                    team_size = detail_items[1].find_all("span")[1].text.strip()
                if len(detail_items) > 3:
                    group_partner_elem = detail_items[3].find_all("a")
                    group_partner = group_partner_elem[0].text.strip() if group_partner_elem else "N/A"
        except Exception as e:
            logger.error(f"Error extracting details: {e}")
        logger.info(f"Founded: {founded}, Team Size: {team_size}, Group Partner: {group_partner}")
        
        # Extract details about the startup
        details_element_container = soup.find("section", class_="relative isolate z-0 border-retro-sectionBorder sm:pr-[13px] ycdcPlus:pr-0 pt-1 sm:pt-2 lg:pt-3 pb-1 sm:pb-2 lg:pb-3")
        details_element = details_element_container.find("p", class_="whitespace-pre-line")
        details = details_element.text.strip() if details_element else "N/A",
        
        # Extract active founders
        founders = []
        try:
            founders_section = soup.find("h3", text="Active Founders").find_parent("section", class_="relative isolate z-0 border-retro-sectionBorder sm:pr-[13px] ycdcPlus:pr-0 pt-1 sm:pt-2 lg:pt-3 pb-1 sm:pb-2 lg:pb-3")
            if founders_section:
                founder_elements = founders_section.find_all("div", class_="flex flex-row flex-col items-start gap-3 md:flex-row")
                for founder_elem in founder_elements:
                    founder_name_elem = founder_elem.find("h3", class_="text-lg font-bold")
                    bio_elem = founder_elem.find("p", class_="prose max-w-full whitespace-pre-line")
                    img_elem = founder_elem.find("img")
                    company_elem = founder_elem.find("a", class_="block text-linkColor")
                    social_links = founder_elem.find_all("a", href=True)

                    founder_name = name_elem.text.strip() if name_elem else "N/A"
                    bio = bio_elem.text.strip() if bio_elem else "N/A"
                    img_url = img_elem['src'] if img_elem else "N/A"
                    company = company_elem.text.strip() if company_elem else "N/A"
                    company_url = company_elem['href'] if company_elem else "N/A"

                    socials = {}
                    for social_link in social_links:
                        href = social_link['href']
                        if "linkedin" in href:
                            socials['linkedin'] = href
                        elif "twitter" in href or "x.com" in href:
                            socials['x'] = href

                    founders.append({
                        "name": founder_name,
                        "bio": bio,
                        "image": img_url,
                        "company": company,
                        "company_url": company_url,
                        "socials": socials
                    })
        except Exception as e:
            logger.error(f"Error extracting founders: {e}")
        logger.info(f"Founders: {founders}")

        # Extract launch details
        launches = []
        try:
            launches_section = soup.find("h3", text="Company Launches").find_parent("section", class_="relative isolate z-0 border-retro-sectionBorder sm:pr-[13px] ycdcPlus:pr-0 pt-1 sm:pt-2 lg:pt-3 pb-1 sm:pb-2 lg:pb-3")
            if launches_section:
                launch_elements = launches_section.find_all("div", recursive=False)
                
                if launch_elements:
                    for launch_elem in launch_elements:
                        title_elem = launch_elem.find("h3")
                        link_element = launch_elem.find("a", class_="ycdc-with-link-color mb-4 mt-0 text-xl underline")
                        description_elem = launch_elem.find("div", class_="prose max-w-full")

                        title = title_elem.text.strip() if title_elem else "N/A"
                        
                        if "Company Launches" in title:
                            continue
                        link = link_element['href'] if link_element else "N/A"
                        description = description_elem.text.strip() if description_elem else "N/A"

                        launches.append({
                            "title": title,
                            "link": link,
                            "description": description
                        })
        except Exception as e:
            logger.error(f"Error extracting launches: {e}")
        logger.info(f"Launches: {launches}")


        return {
            "name": name,
            "description": description,
            "details": details,
            "image": image,
            "website": website,
            "batch": batch,
            "status": status,
            "industries": industries,
            "location": location,
            "founded": founded,
            "team_size": team_size,
            "group_partner": group_partner,
            "founders": founders,
            "launches": launches
        }

    except Exception as e:
        logger.error(f"An error occurred while scraping {url}: {e}")
        raise HTTPException(status_code=500, detail="Internal server error.")

@app.get("/api/yccompanies")
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

@app.get("/api/ycsinglecompany")
def test_scrape():
    try:
        test_url = "https://www.ycombinator.com/companies/bucket-robotics"
        driver = setup_driver()
        details = scrape_company_details(driver, test_url)
        driver.quit()  # Ensure the driver is closed
        return details

    except Exception as e:
        logger.error(f"An error occurred while scraping {test_url}: {e}")
        raise HTTPException(status_code=500, detail="Internal server error.")

# Run FastAPI in debug mode
if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000, log_level="debug")
