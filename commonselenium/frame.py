
from selenium.webdriver.chrome.webdriver import WebDriver

def trocar_para_default(driver: WebDriver):
    driver.switch_to.default_content()

def trocar_default_por_frame_nome(driver: WebDriver, nome_frame: str):
    print("Trocando para o frame: " + nome_frame)
    driver.switch_to.default_content()
    driver.switch_to.frame(nome_frame)

def navegar_outro_frame_nome(driver: WebDriver, nome_frame: str):
    print('Navegando para o frame: ' + nome_frame)
    driver.switch_to.frame(nome_frame)

def navegar_outro_frame_posicao(driver: WebDriver, posicao_frame: int):
    print('Navegando para o frame: ' + str(posicao_frame))
    driver.switch_to.frame(posicao_frame)