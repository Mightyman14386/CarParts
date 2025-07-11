from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.common.exceptions import NoSuchElementException
from selenium import webdriver

# from IPython.display import display, Image

import time
# import pandas as pd

# from collections import deque
# from graphviz import Digraph

options = webdriver.ChromeOptions() 
options.add_argument('--no-sandbox')
options.add_argument('--disable-dev-shm-usage')
options.headless = True # don't use a GUI (necessary on a VM)
service = Service()
driver = webdriver.Chrome(options=options, service=service)

def car(vin, zip, part):
    driver.get("https://vpic.nhtsa.dot.gov/decoder/Decoder?VIN=" + vin + "&ModelYear=")
    time.sleep(0.5)
    modelYear = driver.find_element("id","decodedModelYear").get_attribute("textContent")
    make = driver.find_element("id","decodedMake").get_attribute("textContent")
    model = driver.find_element("id","decodedModel").get_attribute("textContent")
    print(make, model, modelYear)

    # For specific make based sites
    # match make:
    #     case "FORD":
    #         driver.get("https://parts.ford.com")
    #         time.sleep(0.5)

    #         driver.find_element(By.XPATH, "//div[@id='tabVin']/button").click()
    #         time.sleep(0.5)

    #         driver.find_element("id","vinNumber_globSearch").send_keys(vin)
    #         catalog = driver.find_element("id","vinNumButton_globSearch")
    #         try:
    #             cookies = driver.find_element(By.XPATH, "//div[@id='onetrust-close-btn-container']/button")
    #             cookies.click()
    #         except:
    #             pass
    #         catalog.click()
    #         while True:
    #             try:
    #                 driver.find_element("id","noThanksButton").click()
    #                 driver.find_element("id","autocompleteAddressHomePage").send_keys(zip)
    #                 break
    #             except:
    #                 pass
    #         driver.find_element("id","cityGoHomePage").click()
    #         time.sleep(1)
    #         driver.find_element(By.CSS_SELECTOR, "td.dealerName a.ng-binding").click()
    #         time.sleep(0.5)
    #         driver.find_element("id", "SimpleSearchForm_SearchTerm").send_keys(part)
    #         driver.find_element("id", "searchTermButton").click()
    #     case "MAZDA":
    #         pass
    #     case "KIA":
    #         pass
    #     case "MITSUBISHI":
    #         pass

    # Try oempartsonline
    try:
        # driver.get("https://" + make + ".oempartsonline.com")
        # time.sleep(0.5)
        # driver.find_element("id","cmsgpf-close-btn").click()
        # time.sleep(0.5)
        # driver.find_element(By.CLASS_NAME,"vin_search_str").send_keys(vin)
        # driver.find_element("id","button-submit").click()
        # while True:
        #     try:
        #         driver.find_element(By.CSS_SELECTOR, "input[type='checkbox']").click()
        #         break
        #     except:
        #         pass

        # driver.get("https://" + make + ".oempartsonline.com/search?search_str=" + vin)
        # time.sleep(0.5)
        # driver.find_element("id","cmsgpf-close-btn").click()
        # time.sleep(0.5)
        # driver.find_element("id","main_search_8").send_keys(part)
        # print(driver.get_cookies())
        #driver.find_element(By.XPATH, "//*[@id='inner-page-search']/div/div/div[2]/div/div/form/fieldset/button").click()
        
        # driver.get("https://" + make + ".oempartsonline.com/search?search_str=" + part.replace(" ","+"))
        # time.sleep(0.5)
        # driver.find_element("id","cmsgpf-close-btn").click()
        # time.sleep(0.5)
        # Select(driver.find_element(By.XPATH,"//*[@id='layout_search']/div/div/div/div/div[2]/div[1]/div/div[2]/div[2]/div[1]/div/div/div[2]/select")).select_by_visible_text(model)
        # Select(driver.find_element(By.XPATH,"//*[@id='layout_search']/div/div/div/div/div[2]/div[1]/div/div[2]/div[2]/div[1]/div/div/div[3]/select")).select_by_visible_text(modelYear)
        # driver.get("https://ford.oempartsonline.com/search?search_str=" + part.replace(" ","%20") + "&make=" + make.lower + "&model=" + model.lower + "&year=" + modelYear.lower + "&page_id=&page_url=")
        
        driver.get("https://" + make + ".oempartsonline.com/search?search_str=" + part.replace(" ","%20") + "&make=" + make.lower() + "&model=" + model.lower() + "&year=" + modelYear + "&page_id=&page_url=")
        time.sleep(0.5)
        driver.find_element("id","cmsgpf-close-btn").click()
        time.sleep(0.5)
        pass

    except Exception as e:
        print(e)
    
    try:
        #driver.get("https://www.napaonline.com/en/search?text=" + part.replace(" ","%20") + "&referer=v2")
        driver.get("https://www.napaonline.com/?srsltid=AfmBOoroip19a6j-FHooIO3pKYXnPXT0Rpi7pAupCEQy_FsdkCiv52Vh")
        time.sleep(0.5)
        driver.find_element("id","cmsgpf-close-btn").click()
        time.sleep(0.5)
    except Exception as e:
        print(e)


    time.sleep(100)

car("5ux43eu00t9016682", 68521, "wiper blades")
#1FMCU0MN1RUA03532
driver.quit()