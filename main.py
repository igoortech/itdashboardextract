from commonitdashboard.itdashboardgetallagenciesvalues import ItDashBoardAllAgencies
from commonitdashboard.itdashboardgetagencyvalue import ItDashBoardAgencyValue
from datetime import datetime
from commonlog.log import Logger
import os 

task_name = os.path.basename(__file__)
USERNAME = os.environ.get('USERNAME')

##### SET THE INPUT FILE FOR ADVANCED SEARCH
Agency = "National Science Foundation"
##################################################
#BOT NAME
bot_name = "It_DashBoard"
#FOLDER OUTPUT AND FILE NAME ALL AGENCIES
FileAgencies = fr".\Output\all_agencies_.xlsx"
#FOLDER OUTPUT AND FILE NAME SINGLE FILE
FileIndividual = fr".\Output\agencias_individuais.xlsx"
#PATH AND NAME FROM THE FILE DOWNLOAD

FileSource = fr'C:\Users\{USERNAME}\Downloads\Business Case _ IT Dashboard.pdf'
#####################################################
#EXTENSION PDF
extension = "pdf"
#PATH DOWNLAODS
downloads = fr'C:\Users\{USERNAME}\Downloads'

#FOLDER OUTPUT 
FileDes = fr".\Output"



#LOG INSTANCE
log_config = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'log.config')
log_file = fr'.\Output\log.config'

logger = Logger()
logger.fileConfig(log_config, project_name=bot_name, defaults={'logfilename':log_file})

try:
    logger.info("Starting the process get all agencies values")
    itdashboardAllAgencies = ItDashBoardAllAgencies()
    
    logger.info("Acesss page portfolio")
    itdashboardAllAgencies.go_to_it_portfolio()
    logger.info("Acesss page success")

    logger.info("Getting all agencies ")
    agencies = itdashboardAllAgencies.get_agencies()
    logger.info("All agencies got success")

    logger.info("Starting getting all montants from agency")
    mount = []
    for ag in agencies:
        amnt = itdashboardAllAgencies.get_amount(ag)
        mount.append({"Agency":ag.text,"Ammount":amnt})
    logger.info("Montants success")

    
    logger.info("Starting genarating excel file")
    itdashboardAllAgencies.excel(mount,FileAgencies)
    logger.info("Excel genarated sucesss")
    itdashboardAllAgencies.driver.close()
    itdashboardAllAgencies.driver.quit()

    logger.info("Process the process get all agencies values succeed completed")



    logger.info("Starting the process get indivudal values and download")
    itdashboardvalue = ItDashBoardAgencyValue()

    logger.info("Go to page adavanced search")
    itdashboardvalue.go_to_advanced_search()
    logger.info("Page accesss succeed")

      
    logger.info(f"Start searching value: {Agency}")
    itdashboardvalue.search_agency(Agency)
    logger.info(f"Finish searching value: {Agency} Succeed")
    
    
    logger.info("Selecting max view pages")
    itdashboardvalue.select_max_itens()
    logger.info("Max view page was succeed")

    logger.info("Getting investiment values and url download")
    itdashboardvalue.get_agency_investiment_values()
    logger.info("all datas was succeed ")


    result_investiments = itdashboardvalue.result

    logger.info("Starting download pdf")
    for down in result_investiments:
        hora_atual = datetime.now().strftime('%H_%M_%S')
        FileDes = fr".\Output\{down['Type of Investment']}_{hora_atual}.pdf"
        if "link" in down:
            print(down['link'])
            itdashboardvalue.download_pdf(down['link'],downloads, extension, FileDes,FileSource)
    logger.info("Download pdf was succeed")

    logger.info("Starting genarating excel file")
    itdashboardvalue.excel(result_investiments,FileIndividual)
    logger.info("Genarating excel file was succeed")

    logger.info(f'Finishing the process get indivudal values and download succeed completed')
    logger.info(f'Finishing process {bot_name} success')

except Exception as e:
    logger.info(f'Finishing process {bot_name} with error: {e}')
    print(e)





