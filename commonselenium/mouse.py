from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.chrome.webdriver import WebDriver

from commonselenium.buscar import busca_elemento_por_id, busca_elemento_por_xpath


def double_click_por_id(driver: WebDriver, id):
    elem = busca_elemento_por_id(driver, id)
    actionChains = ActionChains(driver)
    actionChains.double_click(elem).perform()

def double_click_por_xpath(driver: WebDriver, xpath):
    elem = busca_elemento_por_xpath(driver, xpath)
    actionChains = ActionChains(driver)
    actionChains.double_click(elem).perform()
    
def Move_Mouse_por_xpath(driver: WebDriver, xpath):
    elem = busca_elemento_por_xpath(driver, xpath)
    actionChains = ActionChains(driver)
    actionChains.move_to_element(elem).perform()
