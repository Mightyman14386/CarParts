from seleniumbase import SB
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


def car(vin, zip, part, exclude=None):
    List = []

    with SB(uc=True, incognito=True, headless=False) as driver:
        driver.uc_open("https://vpic.nhtsa.dot.gov/decoder/Decoder?VIN=" + vin + "&ModelYear=")
        modelYear = driver.find_element("id","decodedModelYear").text
        make = driver.find_element("id","decodedMake").text
        model = driver.find_element("id","decodedModel").text
        print(make, model, modelYear)

        # For specific make based sites
        # match make:
        #     case "CHRYSLER" | "JEEP" | "DODGE" | "RAM" | "FIAT":
        #         driver.uc_open("https://store.mopar.com")
        #         driver.type("//*[@id='main_search_5']", vin + Keys.ENTER, by="xpath")
        #         driver.type("//*[@id='main_search_5']", part + Keys.ENTER, by="xpath")
        #     case "FORD":
        #         # Process to get to list
        #         print("Finding list")
        #         driver.uc_open("https://parts.ford.com")
        #         driver.find_element(By.XPATH, "//div[@id='tabVin']/button").click()
        #         driver.find_element("id","vinNumber_globSearch").send_keys(vin)
        #         driver.find_element("id", "searchTermPartNumvin").send_keys(part)
        #         catalog = driver.find_element("id","vinNumButton_globSearch")
        #         try:
        #             cookies = driver.find_element(By.XPATH, "//div[@id='onetrust-close-btn-container']/button")
        #             cookies.click()
        #         except:
        #             pass
        #         while True:
        #             try:
        #                 driver.find_element("id","noThanksButton").click()
        #                 break
        #             except:
        #                 pass
        #         driver.sleep(0.5)
        #         catalog.click()
        #         driver.find_element("id","autocompleteAddressHomePage").send_keys(zip)
        #         driver.find_element("id","cityGoHomePage").click()
        #         driver.find_element(By.CSS_SELECTOR, "td.dealerName a.ng-binding").click()

        #         # Save List
        #         print("Saving list")
        #         fordList = []
        #         all_divs = driver.find_element(By.XPATH, '//*[@id="partForm"]').find_elements(By.XPATH, "//*[contains(@class, 'partTile')]")
        #         for div in all_divs:
        #             save = []
        #             hrefs = div.find_elements(By.TAG_NAME, "a")
        #             if len(hrefs) == 1:
        #                 continue
        #             image = hrefs[0].find_element(By.TAG_NAME, "img").get_attribute("src")
        #             p = hrefs[1].find_elements(By.TAG_NAME, "p")
        #             name = p[0].text
        #             if part.casefold() not in name.casefold() or (exclude != None and exclude.casefold() in name.casefold()):
        #                 continue
        #             partn = p[1].text
        #             link = hrefs[0].get_attribute("href")
        #             price = float(div.find_element(By.CLASS_NAME, "msrp").text.replace("MSRP:  $", ""))
        #             save = [name, price, partn, link, image, "Pickup", 0]
        #             fordList.append(save)
        #         for idx in range(0, len(fordList)):
        #             save = fordList[idx]

        #             # reference values
        #             ground = {0: 7.95, 40: 15.95, 80: 29.95, 120: 39.95}
        #             overnight = {0: 9.95, 10: 19.95, 20: 29.95, 30: 39.95, 40: 49.95, 50: 59.95, 70: 79.95, 90: 99.95, 110: 119.95, 130: 139.95}

        #             driver.uc_open(save[3])
        #             driver.click('//*[@id="menuList"]/li[2]/a', by='xpath')
        #             weight = driver.get_element('//*[@id="specification"]/div[1]/div', by="xpath").text
        #             weight = float(weight[weight.index("Weight: ") : weight.index("  lbs")].replace("Weight:  ", ""))
                    
        #             # Get delivery prices
        #             if weight <= 10:
        #                 gnd = save.copy()
        #                 ovn = save.copy()
        #                 gnd[5] = "FedEx Ground"
        #                 gnd[6] = 3
        #                 gnd[1] += 7.95
        #                 ovn[5] = "FedEx Overnight"
        #                 ovn[6] = 1
        #                 ovn[1] += 9.95
        #                 fordList.extend([gnd, ovn])
        #             elif weight <= 20:
        #                 gnd = save.copy()
        #                 ovn = save.copy()
        #                 gnd[5] = "FedEx Ground"
        #                 gnd[6] = 3
        #                 gnd[1] += 7.95
        #                 ovn[5] = "FedEx Overnight"
        #                 ovn[6] = 1
        #                 ovn[1] += 19.95
        #                 fordList.extend([gnd, ovn])
        #             elif weight <= 30:
        #                 gnd = save.copy()
        #                 ovn = save.copy()
        #                 gnd[5] = "FedEx Ground"
        #                 gnd[6] = 3
        #                 gnd[1] += 7.95
        #                 ovn[5] = "FedEx Overnight"
        #                 ovn[6] = 1
        #                 ovn[1] += 29.95
        #                 fordList.extend([gnd, ovn])
        #             elif weight <= 40:
        #                 gnd = save.copy()
        #                 ovn = save.copy()
        #                 gnd[5] = "FedEx Ground"
        #                 gnd[6] = 3
        #                 gnd[1] += 7.95
        #                 ovn[5] = "FedEx Overnight"
        #                 ovn[6] = 1
        #                 ovn[1] += 39.95
        #                 fordList.extend([gnd, ovn])
        #             elif weight <= 50:
        #                 gnd = save.copy()
        #                 ovn = save.copy()
        #                 gnd[5] = "FedEx Ground"
        #                 gnd[6] = 3
        #                 gnd[1] += 15.95
        #                 ovn[5] = "FedEx Overnight"
        #                 ovn[6] = 1
        #                 ovn[1] += 49.95
        #                 fordList.extend([gnd, ovn])
        #             elif weight <= 70:
        #                 gnd = save.copy()
        #                 ovn = save.copy()
        #                 gnd[5] = "FedEx Ground"
        #                 gnd[6] = 3
        #                 gnd[1] += 15.95
        #                 ovn[5] = "FedEx Overnight"
        #                 ovn[6] = 1
        #                 ovn[1] += 59.95
        #                 fordList.extend([gnd, ovn])
        #             elif weight <= 80:
        #                 gnd = save.copy()
        #                 ovn = save.copy()
        #                 gnd[5] = "FedEx Ground"
        #                 gnd[6] = 3
        #                 gnd[1] += 15.95
        #                 ovn[5] = "FedEx Overnight"
        #                 ovn[6] = 1
        #                 ovn[1] += 79.95
        #                 fordList.extend([gnd, ovn])
        #             elif weight <= 90:
        #                 gnd = save.copy()
        #                 ovn = save.copy()
        #                 gnd[5] = "FedEx Ground"
        #                 gnd[6] = 3
        #                 gnd[1] += 29.95
        #                 ovn[5] = "FedEx Overnight"
        #                 ovn[6] = 1
        #                 ovn[1] += 79.95
        #                 fordList.extend([gnd, ovn])
        #             elif weight <= 110:
        #                 gnd = save.copy()
        #                 ovn = save.copy()
        #                 gnd[5] = "FedEx Ground"
        #                 gnd[6] = 3
        #                 gnd[1] += 29.95
        #                 ovn[5] = "FedEx Overnight"
        #                 ovn[6] = 1
        #                 ovn[1] += 99.95
        #                 fordList.extend([gnd, ovn])
        #             elif weight <= 120:
        #                 gnd = save.copy()
        #                 ovn = save.copy()
        #                 gnd[5] = "FedEx Ground"
        #                 gnd[6] = 3
        #                 gnd[1] += 29.95
        #                 ovn[5] = "FedEx Overnight"
        #                 ovn[6] = 1
        #                 ovn[1] += 119.95
        #                 fordList.extend([gnd, ovn])
        #             elif weight <= 130:
        #                 gnd = save.copy()
        #                 ovn = save.copy()
        #                 gnd[5] = "FedEx Ground"
        #                 gnd[6] = 3
        #                 gnd[1] += 39.95
        #                 ovn[5] = "FedEx Overnight"
        #                 ovn[6] = 1
        #                 ovn[1] += 119.95
        #                 fordList.extend([gnd, ovn])
        #             else:
        #                 gnd = save.copy()
        #                 ovn = save.copy()
        #                 gnd[5] = "FedEx Ground"
        #                 gnd[6] = 3
        #                 gnd[1] += 39.95
        #                 ovn[5] = "FedEx Overnight"
        #                 ovn[6] = 1
        #                 ovn[1] += 139.95
        #                 fordList.extend([gnd, ovn])

        #         List.extend(fordList)
        #         print(fordList, "Length", len(fordList))

        #     case "MAZDA":
        #         driver.uc_open("https://parts.mazdausa.com")
        #         driver.sleep(0.5)
        #         driver.uc_gui_click_captcha()
        #         driver.sleep(0.5)
        #         driver.find_element(By.XPATH, "//*[@id='SearchInput']").send_keys(vin + Keys.ENTER)
        #         driver.find_element(By.XPATH, "//*[@id='ctl00_Content_PageBody_RefineSearchTermInput']").send_keys(part + Keys.ENTER)
        #         driver.find_element(By.XPATH, "//*[@id='ctl00_Content_PageBody_RefineSearchTermButton']").click()
                
        #     case "KIA":
        #         driver.uc_open("https://parts.kia.com")
        #         driver.sleep(0.5)
        #         driver.type("//*[@id='vinInput']", vin + Keys.ENTER, by="xpath")
        #         driver.click("//*[@id='vin-input-button-submit']", by="xpath")
                
        #     case "MITSUBISHI":
        #         driver.uc_open("https://parts.mitsubishicars.com")
        #         driver.uc_gui_click_captcha()
        #         driver.find_element(By.XPATH, "//*[@id='layout_homepage']/div/div/div[3]/div/div/div/div/div[2]/div/form/input[1]").send_keys(vin + Keys.ENTER)
        #         driver.find_element(By.XPATH, "//*[@id='main_search_1']").send_keys(part + Keys.ENTER)
                

        # Try oempartsonline
        try:
            # Finding List
            driver.uc_open_with_tab("https://" + make + ".oempartsonline.com/search?search_str=" + vin)
            driver.get_element("id","cmsgpf-close-btn", timeout=5).click()
            driver.find_element(By.XPATH, "//*[@id='main_search_8']").send_keys(part + Keys.ENTER)
            driver.click('//*[@id="layout_search"]/div/div/div/div/div[2]/div[2]/div/div/div/div[1]/div[1]/div[2]/div[2]/a/span', by='xpath')
            driver.type('//*[@id="zipInput"]', zip + Keys.ENTER, by='xpath')
            driver.click('//*[@id="dealersList"]/li[1]/button', by='xpath')

            # Saving List
            oemList = []
            div_list = driver.find_elements(By.CLASS_NAME, "catalog-product row")
            for div in div_list:
                a = div.find_element(By.TAG_NAME, "a")
                image = div.find_elements(By.TAG_NAME, "img").get_attribute("src")
                link = div.find_element(By.TAG_NAME, "img").get_attribute("href")
                name = div.find_element(By.CLASS_NAME, "title-link").text
                price = float(div.find_element(By.CLASS_NAME, "sale-price").text.replace("$", ""))
                partn = div.find_element(By.CLASS_NAME, "catalog-product-id").find_element(By.TAG_NAME, "a").text
                [name, price, partn, link, image, "Delivery", 0]
        except Exception as e:
            print(e)
        
        # # Try napaautoparts
        # try:
        #     driver.uc_open("https://www.napaonline.com/en/search?text=" + part.replace(" ","%20") + "&referer=v2")
        #     driver.uc_gui_click_captcha()
        #     driver.click("//*[@id='add-vehicle']/div/div[2]", by="xpath")
        #     driver.click("//*[@id='geo-vin-accordion']", by="xpath")
        #     driver.type("//*[@id='vin']/div/div[1]/input", vin + Keys.ENTER, by="xpath")
        #     driver.click("//*[@id='addVinAnchor']", by="xpath")
        #     driver.click("//*[@id='myStoreSection']", by="xpath")
        #     driver.click("//*[@id='change-my-store-link']", by="xpath")
        #     driver.type("//*[@id='store-search-input']", zip + Keys.ENTER, by="xpath")
        #     driver.sleep(0.5)
        #     driver.click("//*[@id='napaStoreLocator']/div[2]/geo-tabs-horizontal/geo-tab-content[1]/div/div[2]/div[1]/ul/li[1]/div[2]/div[2]/div[2]/a", by="xpath")
            
        #     ##driver.click("/html/body/div[12]/div/div[2]/div/div/div/div/div/button", by="xpath")
        # except Exception as e:
        #     print(e)

        # # Try Autozone
        # try:
        #     driver.uc_open("https://www.autozone.com/searchresult?searchText=" + part.replace(" ","%20"))
        #     driver.click("//*[@id='nav_wrapper']/div[2]/div/button", by="xpath")
        #     driver.click("//*[@id='headlessui-tabs-tab-:r2:']", by="xpath")
        #     driver.type("//*[@id='__starc-7']", vin + Keys.ENTER, by="xpath")
        #     driver.click('//*[@id="nav_wrapper"]/div[4]/div[2]/div/div', by='xpath')
        #     driver.click('//*[@id="changeStoreBtn"]', by='xpath')
        #     driver.type('//*[@id="SearchInput"]', zip + Keys.ENTER, by='xpath')
        #     driver.click('//*[@id="setStore"]', by='xpath')
        # except Exception as e:
        #     print(e)

        # Sort both lists
        pList = sorted(List, key=lambda x: x[1]) # Sorted by cheapest price
        dList = sorted(List, key=lambda x: x[1]) # Sorted by delivery time

        driver.sleep(100)

car("1FMCU0MN1RUA03532", "68521", "wiper blade")
#1FMCU0MN1RUA03532 ford
#JM1GL1VM4M1605064 mazda
#5XYKT3A64CG304354 kia
#4A3AE75H53E075200 mitsubishi
#3C3CFFHH1FT667930 fiat