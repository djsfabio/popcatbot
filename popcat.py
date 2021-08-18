import os
import time

import pyfiglet
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from termcolor import colored
from webdriver_manager.chrome import ChromeDriverManager


def main():
    options = Options()
    ua = 'cat'
    options.add_argument('--user-agent=%s' % ua)
    options.add_argument('--headless')
    options.add_argument("--mute-audio")
    options.add_experimental_option("excludeSwitches", ["enable-automation"])
    options.add_experimental_option('useAutomationExtension', False)
    options.add_argument("--disable-blink-features=AutomationControlled")
    driver = webdriver.Chrome(ChromeDriverManager().install(), chrome_options=options)
    os.system('cls' if os.name == 'nt' else 'clear')
    print(colored(pyfiglet.figlet_format("Popcat Clicker !", font="slant"), "cyan"))
    driver.get("https://popcat.click/")
    running = True
    incrementation = 0
    start = time.time()
    while running:
        incrementation += 1
        driver.find_element_by_tag_name("body").send_keys(Keys.SPACE)
        if incrementation % 1000 == 0:
            driver.save_screenshot("./screenshots/" + str(incrementation) + "_screenshot.png")
            os.system('cls' if os.name == 'nt' else 'clear')
            print(colored(pyfiglet.figlet_format("Popcat Clicker !", font="slant"), "cyan"))
            end = time.time()
            print("🇫🇷  Vous êtes à ", end="")
            print(driver.find_element_by_class_name("cat-img").text, end="")
            print(" points. 🇫🇷")
            sec = end - start
            ty_res = time.gmtime(sec)
            res = time.strftime("%H heure(s), %M minute(s) et %S seconde(s)", ty_res)
            print("Cela fait ", end="")
            print(res, end="")
            print(" que le programme est lancé.")


if __name__ == "__main__":
    main()
