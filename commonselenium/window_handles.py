from selenium.webdriver.chrome.webdriver import WebDriver

def adicionar_nova_janela(driver: WebDriver, handles: list):
    if(len(driver.window_handles) > len(handles)):
        for handle in driver.window_handles:
            if(handle not in handles):
                handles.append(handle)
    return handles
                
def remover_ultima_janela(driver: WebDriver, handles: list):
    del handles[-1]
    return handles