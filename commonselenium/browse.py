from selenium.webdriver.chrome.webdriver import WebDriver
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
import json
import os
import subprocess
import time
from base64 import b64decode
import platform

def get_driver(profile:str = "")->WebDriver:

    # enable browser logging
    d = DesiredCapabilities.CHROME
    d['goog:loggingPrefs'] = { 'performance':'ALL' }

    options = webdriver.ChromeOptions()
    USERNAME = os.environ.get('USERNAME')
    
    USER_DATA_DIR = f"/home/{USERNAME}/.config/google-chrome/Default"
    if 'windows' in platform.system().lower():
        USER_DATA_DIR = f"C:\\Users\\{USERNAME}\\AppData\\Local\\Google\\Chrome\\User Data"

    if profile != "":
        try:
            subprocess.call("TASKKILL /f  /IM  CHROME.EXE")
        except:
            pass
        time.sleep(5)
        options.add_argument(f"--user-data-dir={USER_DATA_DIR}")
        options.add_argument(fr'--profile-directory={profile}') #e.g. Profile 3

    # INICIALIZAR DRIVER
    settings = {
        "recentDestinations": [{
            "id": "Save as PDF",
            "origin": "local",
            "account": "",
        }],
        "selectedDestinationId": "Save as PDF",
        "version": 2
    }
        
    prefs = {
        #download.default_directory': "C:\\Users\\{USERNAME}\\Downloads",
        "profile.default_content_setting_values.automatic_downloads":1, 
        'printing.print_preview_sticky_settings.appState': json.dumps(settings),
        "download.default_directory": r"D:\\Prime Control Desafio\\Extract_It_Dashboard\\Output\teste.pdf", #Change default directory for downloads
        "download.prompt_for_download": True, #To auto download the file
        "download.directory_upgrade": True,
        "plugins.always_open_pdf_externally": False, #It will not show PDF directly in chrome
        "printing.default_destination_selection_rules": {
        "kind": "local",
        "namePattern": "Save as PDF",
    },
        }
    options.add_experimental_option('prefs', prefs)
    options.add_argument('--kiosk-printing')

    driver = webdriver.Chrome(ChromeDriverManager().install(), chrome_options=options, desired_capabilities=d)
    
    return driver

def openBrowser(webdriver: WebDriver, caminhoNavegador: str):
    driver = webdriver.Chrome(executable_path=caminhoNavegador)
    driver.set_page_load_timeout(120)
    return driver


def navegarSite(driver: WebDriver, url:str):
    driver.get(url)
    try:
        driver.maximize_window()
    except:
        pass

def buscar_url_request_base64(driver: WebDriver, arquivo_tipo: str = 'pdf', linha_atual: int = 1):
    # BUSCAR AS INFORMAÇÕES DE NETWORK DE REQUESTS DO CHROME. AFIM DE BUSCAR A URL SOLICITADA PARA ABERTURA AO CLICAR NO BOTAO
    browser_log = driver.get_log('performance') 
    events = [process_browser_log_entry(entry) for entry in browser_log]
    cont = 0
    for event in events:
            
        if 'Network.requestWillBeSent' in event['method']:
            try:
                url = event['params']['request']['url']
                if 'base64' in url and arquivo_tipo in url and 'chrome://' not in url:
                    cont += 1
                    if(cont == linha_atual):
                        return event['params']['request']['url']
                    
            except:
                pass
    
    return ""
def process_browser_log_entry(entry):
    response = json.loads(entry['message'])['message']
    return response



def convert_b64_to_pdf(b64:str,pathfile:str,namefile:str):
    b64 = b64.replace("data:application/pdf;base64,","")
    bytes = b64decode(b64, validate=True)
    if bytes[0:4] != b'%PDF':raise ValueError('Missing the PDF file signature')
    # Write the PDF contents to a local file
    f = open(f'{pathfile}\\{namefile}.pdf', 'wb')
    f.write(bytes)
    f.close()
