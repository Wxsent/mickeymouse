from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import time

options = Options()
options.add_argument("--headless=new")
options.add_argument("--no-sandbox")
options.add_argument("--disable-dev-shm-usage")

driver = webdriver.Chrome(options=options)

driver.get("https://bloxflip.com")

print("Login manually first if needed")

while True:
    try:
        buttons = driver.find_elements(By.XPATH, "//*[contains(text(),'Join')]")

        for btn in buttons:
            try:
                btn.click()
                print("Joined rain!")
            except:
                pass

    except Exception as e:
        print(e)

    time.sleep(2)