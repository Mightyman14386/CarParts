from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.common.exceptions import NoSuchElementException
from selenium import webdriver
from selenium_stealth import stealth
import undetected_chromedriver as uc
import time


from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


options = webdriver.ChromeOptions() 
# options.add_argument("--headless")
options.add_argument('--no-sandbox')
options.add_argument('--disable-dev-shm-usage')
#options.add_experimental_option("excludeSwitches", ["enable-automation"])
#options.add_experimental_option('useAutomationExtension', False)
service = Service()
driver = uc.Chrome(options=options, service=service)

stealth(driver,
        languages=["en-US", "en"],
        vendor="Google Inc.",
        platform="Win32",
        webgl_vendor="Intel Inc.",
        renderer="Intel Iris OpenGL Engine",
        fix_hairline=True,
)

def car(vin, zip, part):
    driver.uc_open("https://vpic.nhtsa.dot.gov/decoder/Decoder?VIN=" + vin + "&ModelYear=")
    driver.sleep(0.5)
    modelYear = driver.find_element("id","decodedModelYear").get_attribute("textContent")
    make = driver.find_element("id","decodedMake").get_attribute("textContent")
    model = driver.find_element("id","decodedModel").get_attribute("textContent")
    print(make, model, modelYear)

    # For specific make based sites
    # match make:
    #     case "FORD":
            # driver.uc_open("https://parts.ford.com")
            # driver.sleep(0.5)
            # driver.find_element(By.XPATH, "//div[@id='tabVin']/button").click()
            # driver.sleep(0.5)
            # driver.find_element("id","vinNumber_globSearch").send_keys(vin)
            # driver.find_element("id", "searchTermPartNumvin").send_keys(part)
            # catalog = driver.find_element("id","vinNumButton_globSearch")
            # driver.sleep(1)
            # try:
            #     cookies = driver.find_element(By.XPATH, "//div[@id='onetrust-close-btn-container']/button")
            #     cookies.click()
            # except:
            #     pass
            # catalog.click()
            # driver.execute_script("arguments[0].click();", catalog)

            # while True:
            #     try:
            #         driver.find_element("id","noThanksButton").click()
            #         driver.find_element("id","autocompleteAddressHomePage").send_keys(zip)
            #         break
            #     except:
            #         pass
            # driver.find_element("id","cityGoHomePage").click()
            # driver.sleep(1)
            # driver.find_element(By.CSS_SELECTOR, "td.dealerName a.ng-binding").click()
            # driver.sleep(0.5)
            # driver.find_element("id", "SimpleSearchForm_SearchTerm").send_keys(part)
            # driver.find_element("id", "searchTermButton").click()
        # case "MAZDA":
        #     pass
        # case "KIA":
        #     pass
        # case "MITSUBISHI":
        #     pass

    # Try oempartsonline
    # try:
    #     driver.uc_open("https://" + make + ".oempartsonline.com/search?search_str=" + part.replace(" ","%20") + "&make=" + make.lower() + "&model=" + model.lower() + "&year=" + modelYear + "&page_id=&page_url=")
    #     driver.sleep(0.5)
    #     driver.find_element("id","cmsgpf-close-btn").click()
    #     driver.sleep(0.5)
    #     pass
    # except Exception as e:
    #     print(e)
    
    # Try napaautoparts
    try:
        driver.uc_open("https://www.napaonline.com/en/search?text=" + part.replace(" ","%20") + "&referer=v2")
        
        # driver.uc_open("https://www.napaonline.com")
        # driver.sleep(0.5)
        # #driver.find_element("id","cmsgpf-close-btn").click()
        # driver.sleep(0.5)
        # driver.find_element("id", "geo-inputText").send_keys(part)
        # driver.find_element("id","search-icon").click()
        # while True:
        #     try:
        #         driver.find_element(By.XPATH,"//*[@id='ovEdv1']/div/label/input").submit()
        #         break
        #     except:
        #         print("click")
        driver.sleep(15)
        driver.find_element(By.CSS_SELECTOR, "#WepX1 > div > label > input[type=checkbox]").click() 
        driver.sleep(15)
        driver.find_element("id", modelYear).click()
        driver.find_element("id", make.capitalize()).click()
        driver.find_element("id", model.capitalize()).click()
        driver.find_element("id","goBtnVehicleSelector").click()

        
    except Exception as e:
        print(e)


    driver.sleep(100)

car("1FMCU0MN1RUA03532", 68521, "wiper blades")
driver.quit()