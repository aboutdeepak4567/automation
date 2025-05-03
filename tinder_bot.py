# tinder_bot.py
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
import random

def start_bot(num_swipes=50):
    options = webdriver.ChromeOptions()
    options.add_argument("--start-maximized")
    driver = webdriver.Chrome(options=options)
    driver.get("https://tinder.com")

    input("Log in to Tinder manually and press Enter here...")

    try:
        body = driver.find_element(By.TAG_NAME, "body")
        for i in range(num_swipes):
            delay = random.uniform(1.2, 3.0)
            body.send_keys(Keys.ARROW_RIGHT)
            print(f"Swiped right {i + 1}/{num_swipes} | Delay: {round(delay, 3)} sec")
            time.sleep(delay)
    except Exception as e:
        print("Error:", e)

    driver.quit()