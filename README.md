# ItDashboard

> Status: ready to homolog ⚠️

### This RPA Solution must open Itdashboard pages (Portfolio, Advanced Search), get all agencies and montantes, check downlaod then download if there's

## STEP-1 SET THE VARIABLES INPUT ON  main.py⚠️
+ ##### SET THE INPUT FILE FOR ADVANCED SEARCH
+  Agency = "National Science Foundation"
+ ##################################################
+ #BOT NAME
+ bot_name = "It_DashBoard"
+ #FOLDER OUTPUT AND FILE NAME
+ FileAgencies = fr".\Output\all_agencies_.xlsx" 
+ #FOLDER OUTPUT AND FILE NAME 
+ FileIndividual = fr".\Output\agencias_individuais.xlsx"

## STEP-2 THE MAIN.PY 
+ this is the main part of the code where all the rest of the logic are call.
+  it has all step by step from the process get all agencies and montant
+ thus get individual datas from agencies and download pdf file
+ every step is logged into .\output\loger⚠️

## STEP-3 FOLDERS STRUCTURES
+ commonfuncoes has all basic most used function to help 
+ commonselenium has all most used and necessary logic from selenium
+ commonlog has all logic used to logs step by step
+ commonitdashboard has all logic used to extract agencies and search individual ones
+ output is the folder where logs and outputs must be saves


### Technologies Used:
<table>
  <tr>
  <td>Python</td>
  <td> ChromeDriver</td>
  </tr>
  <td>3.10.0</td>
  <td>97.0.4692.71</td>
  <tr>
  </tr> 
</table>

## How to run the application:
#### Install: Python
#### Run create_env.bat (it will create the env necessary, activate it and install all necessary requeriments.txt)⚠️⚠️⚠️⚠️⚠️⚠️⚠️
