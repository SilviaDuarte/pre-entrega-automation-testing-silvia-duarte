import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from utilities import login

@pytest.fixture
def driver():
    # Configura opciones de Chrome
    chrome_options = Options()
    chrome_options.add_argument("--incognito")  # Activa modo incógnito

    # Crea el navegador con las opciones configuradas
    driver = webdriver.Chrome(options=chrome_options)
    yield driver
    driver.quit()

@pytest.fixture
def login_in_driver(driver):
    login(driver)
    return driver