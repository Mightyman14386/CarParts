from seleniumbase import SB
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time


def car(vin, zip, part):

    with SB(uc=True) as driver:
        driver.get("https://vpic.nhtsa.dot.gov/decoder/Decoder?VIN=" + vin + "&ModelYear=")
        time.sleep(0.5)
        modelYear = driver.find_element("id","decodedModelYear").get_attribute("textContent")
        make = driver.find_element("id","decodedMake").get_attribute("textContent")
        model = driver.find_element("id","decodedModel").get_attribute("textContent")
        print(make, model, modelYear)

        # For specific make based sites
        match make:
            case "FORD":
                driver.get("https://parts.ford.com")
                time.sleep(0.5)
                driver.find_element(By.XPATH, "//div[@id='tabVin']/button").click()
                time.sleep(0.5)
                driver.find_element("id","vinNumber_globSearch").send_keys(vin)
                driver.find_element("id", "searchTermPartNumvin").send_keys(part)
                catalog = driver.find_element("id","vinNumButton_globSearch")
                time.sleep(1)
                try:
                    cookies = driver.find_element(By.XPATH, "//div[@id='onetrust-close-btn-container']/button")
                    cookies.click()
                except:
                    pass
                while True:
                    try:
                        driver.find_element("id","noThanksButton").click()
                        break
                    except:
                        pass
                time.sleep(0.5)
                catalog.click()
                driver.find_element("id","autocompleteAddressHomePage").send_keys(zip)
                driver.find_element("id","cityGoHomePage").click()
                time.sleep(1)
                driver.find_element(By.CSS_SELECTOR, "td.dealerName a.ng-binding").click()
            case "MAZDA":
                pass
            case "KIA":
                pass
            case "MITSUBISHI":
                pass

        # Try oempartsonline
        try:
            driver.get("https://" + make + ".oempartsonline.com/search?search_str=" + part.replace(" ","%20") + "&make=" + make.lower() + "&model=" + model.lower() + "&year=" + modelYear + "&page_id=&page_url=")
            time.sleep(0.5)
            driver.find_element("id","cmsgpf-close-btn").click()
            time.sleep(0.5)
        except Exception as e:
            print(e)
        
        # Try napaautoparts
        try:
            driver.get("https://www.napaonline.com/en/search?text=" + part.replace(" ","%20") + "&referer=v2")
            driver.click("//*[@id='add-vehicle']/div/div[2]", by="xpath")
            driver.click("//*[@id='geo-vin-accordion']", by="xpath")
            driver.type("//*[@id='vin']/div/div[1]/input", vin + Keys.ENTER, by="xpath")
            driver.click("//*[@id='addVinAnchor']", by="xpath")
            driver.click("//*[@id='myStoreSection']", by="xpath")
            driver.click("//*[@id='change-my-store-link']", by="xpath")
            driver.type("//*[@id='store-search-input']", zip + Keys.ENTER, by="xpath")
            driver.click("//*[@id='napaStoreLocator']/div[2]/geo-tabs-horizontal/geo-tab-content[1]/div/div[2]/div[1]/ul/li[1]/div[2]/div[2]/div[2]/a", by="xpath")
        except Exception as e:
            print(e)


        time.sleep(100)

car("1FMCU0MN1RUA03532", "68521", "wiper blades")