from typing import List
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement

def busca_lista_elementos_por_id(driver: WebDriver, id: str) -> List[WebElement]:
    return driver.find_elements(By.ID, id)

def busca_lista_elementos_por_classe(driver: WebDriver, classe: str) -> List[WebElement] :
    return driver.find_elements(By.CLASS_NAME, classe)

def busca_lista_elementos_por_classe_selector(driver: WebDriver, classe: str) -> List[WebElement] :
    return driver.find_elements(By.CSS_SELECTOR, classe)

def busca_lista_elementos_por_xpath(driver: WebDriver, xpath: str) -> List[WebElement]:
    return driver.find_elements(By.XPATH, xpath)

def busca_lista_elementos_por_tag(driver: WebDriver, tag: str) -> List[WebElement]:
    return driver.find_elements(By.TAG_NAME, tag)

def clicar_lista_elemento_por_texto(list: list[WebElement], text) -> bool:
    elemento_localizado = False
    for item in list:
        if text in item.text:
            item.click()
            elemento_localizado = True
            break

    return elemento_localizado

def buscar_lista_texto(list: List[WebElement], texto: str) -> bool:
    localizou_texto = False
    for item in list:
        if texto.lower() in item.text.lower():
            localizou_texto = True
            break

    return localizou_texto

def buscar_lista_texto_quantidade(list: List[WebElement], texto: str) -> int:
    quantidade_texto = 0
    for item in list:
        if texto.lower() in item.text.lower():
            quantidade_texto += 1
            

    return quantidade_texto

    
