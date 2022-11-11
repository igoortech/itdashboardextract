import autoit as at
import commonfuncoes.file_folder as ff

from commonimagerecognition.ImageRecognition import ImageRecognition
import commonselenium.window_handles as window_handles 
import time

def clicar_imprimir_script(driver, handles):
        handles = window_handles.adicionar_nova_janela(driver, handles)
        driver.switch_to.window(handles[-1])

        lista = driver.execute_script(
        "return document.querySelector('print-preview-app').shadowRoot.querySelector('#sidebar').shadowRoot.querySelector('#destinationSettings').shadowRoot.querySelector('#destinationSelect').shadowRoot.querySelector('print-preview-settings-section').querySelector('.md-select').querySelectorAll('option')"
        )

        print(lista)
        for item in lista:
                if 'Salvar como PDF' in item.text:
                        item.click()
                        time.sleep(1)
                        break
        
        botao_salvar = driver.execute_script(
        "return document.querySelector('print-preview-app').shadowRoot.querySelector('#sidebar').shadowRoot.querySelector('print-preview-button-strip').shadowRoot.querySelector('.action-button')"
        )
        botao_salvar.click()
        handles = window_handles.remover_ultima_janela(driver, handles)
        driver.switch_to.window(handles[-1])



def clicar_imprimir_imagem(driver):
        path_img = "src/img/imprimir"

        shape_confidence = 0.9
        histogram_confidence = 0.4
        image_find = f'{path_img}/btn_salvar.png'
        recognition = ImageRecognition(image_find)
        retry_times = 3
        image_found = recognition.click_image(driver, shape_confidence, histogram_confidence, retry_times)

        if(image_found == False):
                image_find = f'{path_img}/imprimir_print_pdf.png'
                recognition = ImageRecognition(image_find)
                image_found = recognition.click_image(driver, shape_confidence, histogram_confidence, retry_times)

                image_find = f'{path_img}/imprimir_select_salvar_como_pdf.png'
                recognition = ImageRecognition(image_find)
                image_found = recognition.click_image(driver, shape_confidence, histogram_confidence, retry_times)

                image_find = f'{path_img}/btn_salvar.png'
                recognition = ImageRecognition(image_find)
                image_found = recognition.click_image(driver, shape_confidence, histogram_confidence, retry_times)

def salvar_como(file, janela_nome = "Save Print Output As"):
        ff.delete_file(file)
        window_title = janela_nome
        timeout = 10
        at.win_wait(window_title, timeout)
        control = "Edit1"
        at.control_set_text(window_title, control, file)
        control = "Button2"
        at.control_click(window_title, control)
        

    
