from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
import time
from datetime import date
import os
import json

CHROME_DRIVER_PATH = os.path.join(os.getcwd(),"chromedriver.exe")
OP = webdriver.ChromeOptions()
OP.add_argument('--headless')
DRIVER = webdriver.Chrome()

def main():
    try:
        DRIVER.get("https://trello.com")
        input("Operation Completed. Press any key...")
        DRIVER.close()
    except Exception as e:
        print(e)
        DRIVER.close()
        
    if __name__=='__main__':
        main()
