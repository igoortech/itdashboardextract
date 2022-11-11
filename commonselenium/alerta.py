
from selenium.webdriver.common.alert import Alert 
from selenium.webdriver.chrome.webdriver import WebDriver

import commonselenium.aguardar as aguardar

def _buscar_alerta(driver: WebDriver, timeout_aguardar_alerta = 10):
    aguardar.aguardar_alerta(driver, timeout_aguardar_alerta)
    return Alert(driver) 

def buscar_texto(driver: WebDriver, timeout_aguardar_alerta = 10):
    alert = _buscar_alerta(driver, timeout_aguardar_alerta)
    return alert.text

def aceitar(driver: WebDriver, timeout_aguardar_alerta = 10):
    alert = _buscar_alerta(driver, timeout_aguardar_alerta)
    return alert.accept()

def recusar(driver: WebDriver, timeout_aguardar_alerta = 10):
    alert = _buscar_alerta(driver, timeout_aguardar_alerta)
    return alert.dismiss()

def enviar_texto(driver: WebDriver, texto: str, timeout_aguardar_alerta = 10):
    alert = _buscar_alerta(driver, timeout_aguardar_alerta)
    return alert.send_keys(texto)
