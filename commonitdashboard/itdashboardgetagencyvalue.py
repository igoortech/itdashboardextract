import commonselenium.aguardar as aguardar
import commonselenium.browse as browse
import commonselenium.buscar as buscar
import commonselenium.clicar as clicar
import commonselenium.inserir_texto as inserir_texto
from selenium.webdriver.support.ui import Select
import commonfuncoes.file_folder as File
from pandas import pandas as pd
import time

class ItDashBoardAgencyValue():
    URL = "https://www.itdashboard.gov/search-advanced"

    def __init__(self, remote_driver = False) -> None:
        
        if(remote_driver == False):
            self.driver = browse.get_driver()

        if(remote_driver == True):
            self.driver = browse.get_remote_driver()

        self._inputSearchButtonId  = 'edit-submit'
        self._inputSearchTextId    = "edit-keywords"
        self._inputResultId        =  "search-results"
        self._inputSelectValueId   = "show-by"
        self._inputResultItemClass = "search-result-item"
        self._inputFieldsXpath     =  "div[contains(@class,'search-result-tier') and not(contains(@class,'1')) and not(contains(@class,'2'))]/div"
        self._inputDownXpath       =  "div[contains(@class,'search-result-tier-1')]/div/span/a"
        self._inputcurrentPgeClass = "current-page"
        self._inputNexPageClass    = "next"
        self._inputPageDownloadClass    = "margin-0"




    def go_to_advanced_search(self)-> None:
        browse.navegarSite(self.driver, self.URL)
        aguardar.aguardar_elemento_ser_clicavel_id(self.driver,  self._inputSearchButtonId, 120)


    def search_agency(self, ag: str)-> None:
        #insert the value to be search
        inserir_texto.inserir_texto_por_id(self.driver, self._inputSearchTextId ,ag)
        time.sleep(1)
        #click on the button search
        clicar.clicar_elemento_por_id(self.driver,self._inputSearchButtonId )
        #wait for elements load
        aguardar.aguardar_elemento_ser_clicavel_id(self.driver,self._inputResultId, 120)
       
    def select_max_itens(self)-> None:
        #get the element dropdown
        element = buscar.busca_elemento_por_id(self.driver,self._inputSelectValueId)
        #select the element
        drop=Select(element)
        #select the max value
        drop.select_by_index(2)
        time.sleep(3)


    def get_agency_investiment_values(self)-> None:
        self.result = []
        time.sleep(2)

        try:
            #get total of pages on the screen
            current_page = buscar.busca_elementos_por_classe(self.driver,self._inputcurrentPgeClass)[0].text
            time.sleep(1)
            pages = int(current_page.split(' ')[3])
            
            for page in range(pages):
                #get all elements on the screen
                results_spending = buscar.busca_elementos_por_classe(self.driver,self._inputResultItemClass)

                #getting the result from the element on screen and generate a list 
                for res in results_spending:
                    #getting the fields
                    fields = buscar.busca_elementos_por_xpath(res,self._inputFieldsXpath)
                    #genarating a  list from the fields

                    row_result = {buscar.busca_elementos_por_xpath(x,"span")[0].text:buscar.busca_elementos_por_xpath(x,"span")[1].text for x in  fields}
           
                
                    #check if there's the option download
                    down = buscar.busca_elementos_por_xpath(res, self._inputDownXpath)
                    if down:
                        row_result["link"] = down[0].get_attribute("href")
                    self.result.append(row_result)
                
                #go to the next page
                aguardar.aguardar_elemento_ser_clicavel_classe(self.driver,"result-label high",20)
                clicar.clicar_elemento_por_class(self.driver,self._inputNexPageClass)
                time.sleep(2)
            return self.result
        except Exception as e:
            print(e)


    def download_pdf(self,url:str, down: str, extension: str, dest:str, source: str)-> None:
        browse.navegarSite(self.driver, url)
        aguardar.aguardar_elemento_ser_clicavel_classe(self.driver, self._inputPageDownloadClass, 120)
        File.delete_file(source)
        clicar.clicar_elemento_por_xpath(self.driver,'//*[@id="block-data-visualizer-content"]/div/a[1]')
        File.wait_for_file_by_extension(down,extension,20)
        File.move_file(source,dest)



    def excel(self,result:list,Dest:str)-> None:
        clientes_Resultados = [k for k in result]
        df_data=pd.DataFrame(clientes_Resultados)
        df_data = pd.DataFrame(result)
        df_data.to_excel(Dest, index=False)