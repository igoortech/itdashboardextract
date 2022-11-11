from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.webdriver import WebDriver
import time

def inserir_texto_por_id(driver: WebDriver, id: str, texto: str):
    driver.find_element(By.ID, id).send_keys(texto)
    
def inserir_texto_por_xpath(driver: WebDriver, xpath: str, texto: str):
    driver.find_element(By.XPATH, xpath).send_keys(texto)
    
def inserir_texto_por_id_parcial(driver: WebDriver, id: str, texto: str):
    value = 'input[id*="%s"]' %id
    for letter in texto:
        driver.find_element_by_css_selector(value).send_keys(letter)

def inserir_texto_por_letra_xpath(driver: WebDriver, xpath: str, texto: str):
    for letter in texto:
        driver.find_element(By.XPATH, xpath).send_keys(letter)
        time.sleep(0.1)
        
def inserir_texto_por_letra(driver: WebDriver, by: By, selector: str, texto: str, delay: int = 0.1):
    for letter in texto:
        driver.find_element(by, selector).send_keys(letter)
        time.sleep(delay)

    
    
