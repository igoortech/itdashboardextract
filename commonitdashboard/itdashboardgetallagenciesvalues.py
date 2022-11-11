import commonselenium.aguardar as aguardar
import commonselenium.browse as browse
import commonselenium.buscar as buscar
from pandas import pandas as pd
import time

class ItDashBoardAllAgencies():
    URL = "https://www.itdashboard.gov/itportfoliodashboard"

    def __init__(self, remote_driver = False) -> None:
        
        if(remote_driver == False):
            self.driver = browse.get_driver()

        if(remote_driver == True):
            self.driver = browse.get_remote_driver()

        self._inputFilterAgencyId     = 'agency-select'
        self._inputAgencyXpath        = "//select[@id='agency-select']/option"
        self._inputLaodingXpth        =  "//img[@class='throbber hidden']"
        self._inputMontanteValueXpath = "//div[@class='it-spending']/p"


    def go_to_it_portfolio(self)-> None:
        browse.navegarSite(self.driver, self.URL)
        aguardar.aguardar_elemento_ser_clicavel_id(self.driver, self._inputFilterAgencyId, 120)


    def get_agencies(self)-> None:
        #Retorna cada option <Element>
        agencies = buscar.busca_elementos_por_xpath(self.driver,self._inputAgencyXpath)
        
        return agencies


    def get_amount(self,ag)-> None:
        #Clica no option <Element>
        ag.click()
        
        #Aguarda  tela carregar
        time.sleep(1)
        aguardar.aguardar_xpath(self.driver,self._inputLaodingXpth)
        return buscar.busca_elemento_por_xpath(self.driver,self._inputMontanteValueXpath).text
    

    def excel(self,result:list,Dest:str)-> None:
        clientes_Resultados = [k for k in result]
        df_data=pd.DataFrame(clientes_Resultados)
        df_data = pd.DataFrame(result)
        df_data.to_excel(Dest, index=False)
