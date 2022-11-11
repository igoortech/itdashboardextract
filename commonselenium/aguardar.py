from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.webdriver import WebDriver

import commonselenium.buscar as buscar

def aguardar_elemento_ser_clicavel_id(driver: WebDriver, id: str, tempo: int)->bool:
    aguardar = WebDriverWait(driver, tempo)
    return aguardar.until(EC.element_to_be_clickable((By.ID, id)))
    
def aguardar_elemento_ser_clicavel_xpath(driver: WebDriver, xpath: str, tempo: int)->bool:
    aguardar = WebDriverWait(driver, tempo)
    return aguardar.until(EC.element_to_be_clickable((By.XPATH, xpath)))

def aguardar_elemento_ser_clicavel_classe(driver: WebDriver, classe: str, tempo: int)->bool:
    aguardar = WebDriverWait(driver, tempo)
    return aguardar.until(EC.element_to_be_clickable((By.CLASS_NAME, classe)))

def aguardar_elemento_ser_clicavel_classe_selector(driver: WebDriver, classe: str, tempo: int)->bool:
    aguardar = WebDriverWait(driver, tempo)
    return aguardar.until(EC.element_to_be_clickable((By.CSS_SELECTOR, classe)))

def aguardar_elemento_ser_clicavel_tag_texto(driver: WebDriver, tag: str, texto:str, tempo: int)->bool:
    aguardar = WebDriverWait(driver, tempo)
    localizou_elemento = False
    try:
        aguardar.until(EC.element_to_be_clickable((By.TAG_NAME, tag)))
        aguardar.until(EC.visibility_of_element_located((By.TAG_NAME, tag)))
        elemento_texto = buscar.busca_elemento_texto_por_tag(driver, tag)

        if texto == elemento_texto:
            localizou_elemento = True

    except Exception as e:
        print(e)
        localizou_elemento = False

    return localizou_elemento

def aguardar_alerta(driver: WebDriver, timeout = 10):
    try:
        WebDriverWait(driver, timeout).until(EC.alert_is_present())
        return True
    except:
        return False


def aguardar_xpath(driver: WebDriver,xpath:str, timeout = 10):
    try:
        WebDriverWait(driver, timeout).until(lambda x:driver.find_elements(By.XPATH, xpath))
        return True
    except:
        return False