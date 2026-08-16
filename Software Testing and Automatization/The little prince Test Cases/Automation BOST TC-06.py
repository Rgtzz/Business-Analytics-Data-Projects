from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
import time

driver = webdriver.Chrome()

#Open the Website
driver.get("https://www.thelittleprincecinema.com")

# Configuration 
URL = "https://thelittleprincecinema.com"  # Replace with actual party page URL
TIMEOUT = 3  # seconds

# Setup WebDriver 
options = webdriver.ChromeOptions()
options.add_argument("--start-maximized")

driver = webdriver.Chrome(options=options)
wait = WebDriverWait(driver, TIMEOUT)

try:
    # 1. Open the page
    driver.get(URL)
    print("Page loaded.")

    # 2. Wait for and click the location menu item
    menu_item = wait.until(
        EC.element_to_be_clickable((By.XPATH, '//*[@id="comp-mfevgxip__8d88bd27-9b7f-41e2-86c9-a644241567fd"]'))
    )
    menu_item.click()
    time.sleep(3)
    print("Clicked location menu item (menuitem-1).")

    # scroll down to see element
    time.sleep(2)
    element = driver.find_element(By.XPATH, '//*[@id="comp-mh3p9uez1"]')
    driver.execute_script("arguments[0].scrollIntoView();", element)
    time.sleep(3)


    # 2. Wait for and click the second element: Hsot party
    party_element = wait.until(
        EC.element_to_be_clickable((By.XPATH, '//*[@id="img_comp-mh3p9uf41"]'))
    )
    party_element.click()
    print("Clicked party menu item (menuitem-2).")

    time.sleep(5)

    #2.1 Scroll Down to partys section to book now section under partys
    book_now_prtys = driver.find_element(By.XPATH, '//*[@id="comp-kuzv9m7v"]/h1/span/a/span/span/span')
    driver.execute_script("arguments[0].scrollIntoView();", book_now_prtys)
    book_now_prtys.click()
    time.sleep(3)
    print("Clicked Book Now under Parties section.")


    #3. Scroll down to see the element [This one is the Weekend party PCK(HERE IS WHERE IT CAN BE CHANGED THE XPATH TO TARGET ANOTHER ELEMENT)]
    Select_wknd_prty = driver.find_element(By.XPATH, '//*[@id="TPASection_ktwxiw7p"]/div/div/div/div[3]/div/ul/li[2]/section/div[2]/div/div[2]/div/a/span')
    driver.execute_script("arguments[0].scrollIntoView();", Select_wknd_prty)

    time.sleep(3)

    Select_wknd_prty.click()

    time.sleep(3)

    print("Clicked Weekend Party Package.")

    time.sleep(3)

    #4. Select the Availability on the Schedule
    availability_element = wait.until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, '#TPAMultiSection_l0pcbmr8 > div > div > div > div.snL_eyq > div > div > div.s__7ZA6Xm > div > div.sRwbdfA > div:nth-child(1) > div > div > div > div > div > div.sHWo534.op9uT9O---size-6-medium.s__1wD1UV.sNfG8u8 > button.sTyJWsG.s__2_MGDK.s__84R_Ct.o__7CUD01---skin-5-light.o__7CUD01---priority-7-primary.o__7CUD01---size-6-medium.sIvwCSW > span > svg'))
    )
    availability_element.click()
    print("Clicked Availability on the Schedule.")
    time.sleep(3)

    #5. Proceed to Booking
    date_button = driver.find_element(By.XPATH, '//*[@id="TPAMultiSection_l0pcbmr8"]/div/div/div/div[2]/div/div/div[1]/div/div[2]/div[1]/div/div/div/div/div/div[2]/table/tbody/tr[1]/td[6]/button')
    date_button.click()

    time.sleep(3)
    print("Selected date for booking.")

    #7. Finalize the booking
    next_button = wait.until(
        EC.element_to_be_clickable((By.XPATH, '//*[@id="TPAMultiSection_l0pcbmr8"]/div/div/div/div[2]/div/div/div[2]/button'))
    )
    next_button.click()

    time.sleep(4)
    print("Next Button pressed.")

# -------------------------------------------------------------------------------------------------------------------------------------
    def test_tax_calculation(driver):

        # Extract all price items (subtotal, tax, total)
        prices = driver.find_elements(By.CSS_SELECTOR, "[data-hook='price-item-description']")

        subtotal_text = prices[0].text
        tax_text = prices[1].text
        total_text = prices[2].text

        # Convert strings to floats
        subtotal = float(subtotal_text.replace("CA$", "").strip())
        tax = float(tax_text.replace("CA$", "").strip())
        total = float(total_text.replace("CA$", "").strip())

        print(f"Subtotal: {subtotal}, Tax: {tax}, Total: {total}")

        # Expected values
        expected_tax = round(subtotal * 0.15, 2)
        expected_total = round(subtotal + expected_tax, 2)

        print(f"Expected Tax: {expected_tax}, Expected Total: {expected_total}")

        # Assertions
        assert tax == expected_tax, f"Tax mismatch: expected {expected_tax}, got {tax}"
        assert total == expected_total, f"Total mismatch: expected {expected_total}, got {total}"

        print("TEST PASSED: Tax and total calculations are correct")
    test_tax_calculation(driver)
# -------------------------------------------------------------------------------------------------------------------------------------

    #8. Fill Booking Form (Name, Email, Phone) 

    # Enter Name
    name_field = driver.find_element(By.XPATH, '//*[@id="form-field-input-00000000-0000-0000-0000-000000000001-TPAMultiSection_l0pcbzqj-"]')
    name_field.send_keys("Felipe R")
    print("Entered name.")

    time.sleep(2)

    #E-mail field
    email_field = driver.find_element(By.XPATH, '//*[@id="form-field-input-00000000-0000-0000-0000-000000000002-TPAMultiSection_l0pcbzqj-"]')
    email_field.send_keys("c0950936@mylambton.ca")

    time.sleep(2)
    print("Entered email.")

    #Phone field
    # Select specific country (example: Canada)
    country_into_select = driver.find_element(By.XPATH, '//*[@id="form-field-input-00000000-0000-0000-0000-000000000003-TPAMultiSection_l0pcbzqj-"]')
    country_into_select.send_keys("+15676967968")

    time.sleep(4)
    print("Entered phone number.")
    
    #Number of guests.
    number_guests = driver.find_element(By.XPATH, '//*[@id="form-field-input-d68a1666-6108-4b84-a063-45d10a0c66ba-TPAMultiSection_l0pcbzqj-"]')
    number_guests.send_keys("4")

    time.sleep(2)
    print("Filled booking form.")

    #Movie selection
    movie_dropdown = driver.find_element(By.XPATH, '//*[@id="form-field-input-71e5c5cb-493d-40ad-9fed-c27fcb13a5ca-TPAMultiSection_l0pcbzqj-"]')
    movie_dropdown.send_keys("Frozen II")

    time.sleep(2)
    print("Selected movie.")

    #Subtitles selection
    subtitles_dropdown = driver.find_element(By.XPATH, '//*[@id="form-field-input-b2c9843b-74b2-44e7-b343-988cbe2f977b-TPAMultiSection_l0pcbzqj-"]')
    subtitles_dropdown.send_keys("French")

    time.sleep(2)
    print("Selected subtitles.")

    #Name and Age
    child_name_field = driver.find_element(By.XPATH, '//*[@id="form-field-input-72d6ad3c-13be-40ba-852e-87a527b4c6d8-TPAMultiSection_l0pcbzqj-"]')
    child_name_field.send_keys("Juan Gonzales - 7 years old")

    time.sleep(2)
    print("Entered child's name and age.")

    #Bringing Caake or pizza
    cake_field = driver.find_element(By.XPATH, '//*[@id="form-field-input-4723f019-1ee5-4020-bf06-badb160671ef-TPAMultiSection_l0pcbzqj-"]')
    cake_field.send_keys("Yes")

    print("Indicated bringing cake or pizza.")
    time.sleep(2)

  

# make an exception for the timeout
except TimeoutException as e:
    print("Error: One of the elements did not appear within the timeout period.")
    print("Check the XPath or page structure.")
except Exception as e:
    print(f"An unexpected error occurred: {e}")
finally:
    # Keep browser open for a few seconds to observe, then quit
    driver.implicitly_wait(20)
    driver.quit()
