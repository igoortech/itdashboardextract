import os 
import shutil
import time 
from urllib import request
import os.path
import time

def create_folder(folder:str, overwrite:bool = False):
    folder_exists = os.path.exists(folder)

    if( folder_exists == True and overwrite == True):
        shutil(folder)
        
    if(folder_exists== True and overwrite == False):
        return

    os.makedirs(folder)
    
def move_file(file_source: str, file_destination:str):
    if(file_exists(file_destination)):
        delete_file(file_destination)
        
    shutil.move(file_source, file_destination)
    
    delete_file(file_source)

def delete_folder_files(dir):
    files = os.listdir(dir)
    for file in files:
        for i in range(0, 10):
            print(file)
            file_path = f"{dir}\\{file}"
            try:
                os.remove(file_path)
                break
            except:
                print(f'Não foi possivel deletar o arquivo {file_path}, tentando novamente...')
                time.sleep(1)
        
def delete_file(file:str):
    if(os.path.exists(file) == True):
        os.remove(file)

def file_exists(file)-> bool:
    return os.path.exists(file)

def wait_for_file_by_extension(dir, extension, timeout) -> str:
    file_found = False
    file = ""
    
    for i in range(0, timeout):
        print('Waiting for file...')
        files = os.listdir(dir)
        for file in files:
            if extension in file.split('.')[-1]:
                file_found = True
                file = f"{dir}\\{file}"
                break

        if(file_found == True):
            break

        time.sleep(1)
        
    if(file_found == False):
            file = ""
    
    return file, file_found

def download_file_http(url:str, local_file): 
    request.urlretrieve(url, local_file)


