import os.path
from random import choice

from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.ui import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.core.utils import ChromeType

WHATSAPP_URL = 'https://web.whatsapp.com/'

options = Options()
options.add_argument(argument='--user-data-dir=chrome-data')


def whatsapp_bot(contact_name: str) -> None:
    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager(chrome_type=ChromeType.GOOGLE).install()))
    driver.maximize_window()
    driver.get(WHATSAPP_URL)

    wait = WebDriverWait(driver=driver, timeout=600)

    contact_name_xpath = f'//span[contains(@title, "{contact_name}")]'

    target = wait.until(ec.presence_of_element_located((By.XPATH, contact_name_xpath)))
    target.click()

    message_xpath = '//div[@class="to2l77zo gfz4du6o ag5g9lrv bze30y65 kao4egtt"][@contenteditable="true"][' \
                    '@data-tab="10"]'
    input_box = driver.find_element(by=By.XPATH, value=message_xpath)

    message = f"```message```"
    input_box.send_keys(message)
    input_box.send_keys(Keys.ENTER)

    driver.quit()


if __name__ == '__main__':
    whatsapp_bot(contact_name='')
