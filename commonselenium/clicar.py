from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys


def clicar_elemento_por_id(driver: WebDriver, id: str) -> None:
    driver.find_element(By.ID, id).click()

def clicar_elemento_por_class(driver: WebDriver, class_name: str) -> None:
    driver.find_element(By.CLASS_NAME, class_name).click()

def clicar_elemento_por_xpath(driver: WebDriver, xpath: str) -> None:
    driver.find_element(By.XPATH, xpath).click()

def clicar_elemento_por_classe_selector(driver: WebDriver, classe: str) -> None:
    driver.find_element(By.CSS_SELECTOR, classe).click()

def clicar_elemento_por_elemento_mouse(driver: WebDriver, elemento: WebElement):
    action = ActionChains(driver)
    action.move_to_element(elemento) 
    action.click()
    action.perform()

def clicar_elemento_botao_direito(driver: WebDriver, elemento: WebElement):
    action = ActionChains(driver)
    action.move_to_element(elemento) 
    action.context_click(elemento)
    action.perform()

def inserir_enter(driver: WebDriver, by: By, selector: str):
    driver.find_element(by, selector).send_keys(Keys.RETURN)
