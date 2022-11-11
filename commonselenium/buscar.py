from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement

def busca_elemento_por_id(driver: WebDriver, id: str) -> WebElement:
    return driver.find_element(By.ID, id)

def busca_elementos_por_id(driver: WebDriver, id: str) -> WebElement:
    return driver.find_elements(By.ID, id)


def busca_elemento_por_classe(driver: WebDriver, classe: str) -> WebElement:
    return driver.find_element(By.CLASS_NAME, classe)

def busca_elementos_por_classe(driver: WebDriver, classe: str) -> WebElement:
    return driver.find_elements(By.CLASS_NAME, classe)


def busca_elemento_por_classe_selector(driver: WebDriver, classe: str) -> WebElement:
    return driver.find_element(By.CSS_SELECTOR, classe)


def busca_elemento_por_xpath(driver: WebDriver, xpath: str) -> WebElement:
    return driver.find_element(By.XPATH, xpath)

def busca_elementos_por_xpath(driver: WebDriver, xpath: str) -> WebElement:
    return driver.find_elements(By.XPATH, xpath)

def busca_elemento_texto_por_id(driver: WebDriver, id: str) -> str:
    return driver.find_element(By.ID, id).text

def busca_elemento_texto_por_tag(driver: WebDriver, tag: str) -> str:
    return driver.find_element(By.TAG_NAME, tag).text

def busca_elemento_texto_por_xpath(driver: WebDriver, xpath: str) -> str:
    return driver.find_element(By.XPATH, xpath).text

def busca_elemento_texto_por_classe(driver: WebDriver, classe: str) -> str:
    return driver.find_element(By.CLASS_NAME, classe).text

def buscar_elemento_atributo_por_xpath(driver: WebDriver, xpath: str, attribute: str) -> str:
    elemento: WebElement = driver.find_element(By.XPATH, xpath)
    return elemento.get_attribute(attribute)

def busca_elemento_texto_por_classe_selector(driver: WebDriver, classe: str) -> str:
    return driver.find_element(By.CSS_SELECTOR, classe).text

def buscar_elemento_atributo_por_classe_selector(driver: WebDriver, classe: str, attribute: str) -> str:
    elemento: WebElement = driver.find_element(By.CSS_SELECTOR, classe)
    return elemento.get_attribute(attribute)
    


