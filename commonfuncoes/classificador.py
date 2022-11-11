from commonfuncoes.string import before_after, after, before
from commonfuncoes.pdf import read_pdf
import re

def get_text_before_after_by_list(pdf_text, text_list_before, text_list_after):
    
    # BUSCAR TEXTO BEFORE
    texto_localizado = False
    texto_depois = ""
    texto_antes = ""
    texto = ""

    lista_textos = text_list_before.split(',')

    for texto in lista_textos:
        if texto in pdf_text:
            texto_antes = texto 
            texto_localizado = True
            break

    if texto_localizado == False:
        return texto_antes, "", texto_localizado
    # BUSCAR TEXTO AFTER 
    lista_textos_seguintes = text_list_after.split(',')

    for texto in lista_textos_seguintes:
        if texto in pdf_text:
            texto_depois = texto 
            break
    
    texto = before_after(pdf_text, texto_antes, texto_depois)

    texto = re.sub('(Page [0-9]* of [0-9]*)', '', texto)
    return texto_antes, texto.replace('\n\n','').lstrip(), texto_localizado

def get_text_before_by_list(pdf_text, text_list_before):
    
    # BUSCAR TEXTO BEFORE
    texto_localizado = False
    texto_antes = ""
    texto = ""

    lista_textos = text_list_before.split(',')

    for texto in lista_textos:
        if texto in pdf_text:
            texto_antes = texto 
            texto_localizado = True
            break

    if texto_localizado == False:
        return texto_antes, "", texto_localizado
    
    texto = after(pdf_text, texto_antes)
    texto = re.sub('(Page [0-9]* of [0-9]*)', '', texto)
    return texto_antes, texto.replace('\n\n','').lstrip(), texto_localizado

def remove_after(): 
    file = "C:\\Users\\vinic\\Desktop\\Projetos\\Viseu\\Selenium\\Linkedin\\docs\\Bruno.pdf"
    pdf_text = read_pdf(file)

    file = open("C:\\Users\\vinic\\Desktop\\Projetos\\Viseu\\Selenium\\Linkedin\\docs\\Bruno.txt", "r", encoding="utf-8")
    pdf_text = file.read()

    person_name = "Bruno Cosmo"

    return person_name, pdf_text
    
def get_contact(pdf_text: str, person_name: str)->tuple:
    # person_name, pdf_text = remove_after()
    
    # Buscar do banco de dados
    lista_textos_antes = 'Contato,Contactar,Contact'
    lista_textos_seguintes = f'Principais competências,Principais competencias,Aptitudes principales,Top Skills,Languages,Certifications,{person_name},Resumo,Experiencia,Experience'

    return get_text_before_after_by_list(pdf_text, lista_textos_antes, lista_textos_seguintes)

    
def get_skills(pdf_text: str, person_name: str)->tuple:
    # person_name, pdf_text = remove_after()
    
    # Vir do banco de dados
    lista_textos_antes = 'Principais competências,Principais competencias,Aptitudes principales,Top Skills'
    lista_textos_seguintes = f'Languages,Certifications,{person_name},Resumo,Experiencia,Experience'

    return get_text_before_after_by_list(pdf_text, lista_textos_antes, lista_textos_seguintes)
    
def get_languages(pdf_text: str, person_name: str)->tuple:
    # person_name, pdf_text = remove_after()
    
    # Vir do banco de dados
    lista_textos_antes = 'Languages'
    lista_textos_seguintes = f'Certifications,Patents,{person_name},Resumo,Experiencia,Experience'

    return get_text_before_after_by_list(pdf_text, lista_textos_antes, lista_textos_seguintes)
    
def get_certificates(pdf_text: str, person_name: str)->tuple:
    # person_name, pdf_text = remove_after()
    
    # Vir do banco de dados
    lista_textos_antes = 'Certifications'
    lista_textos_seguintes = f'Patents,{person_name},Resumo,Experiencia,Experience'

    return get_text_before_after_by_list(pdf_text, lista_textos_antes, lista_textos_seguintes)
    
def get_patents(pdf_text: str, person_name: str)->tuple:
    # person_name, pdf_text = remove_after()
    
    # Vir do banco de dados
    lista_textos_antes = 'Patents'
    lista_textos_seguintes = f'{person_name},Resumo,Experiencia,Experience'

    return get_text_before_after_by_list(pdf_text, lista_textos_antes, lista_textos_seguintes)
    
def get_summary(pdf_text: str, person_name: str)->tuple:
    # person_name, pdf_text = remove_after()
    
    # Vir do banco de dados
    lista_textos_antes = 'Resumo,Summary,Resumen'
    lista_textos_seguintes = f'Experience\n,Experiência\n,Experiencia\n'

    return get_text_before_after_by_list(pdf_text, lista_textos_antes, lista_textos_seguintes)
    
def get_experience(pdf_text: str, person_name: str)->tuple:
    # person_name, pdf_text = remove_after()
    
    # Vir do banco de dados
    lista_textos_antes = 'Experiência,Experiencia,Experience'
    lista_textos_seguintes = f'Formação acadêmica,Academic education,Formación académica'

    texto, texto_obtido, texto_localizado = get_text_before_after_by_list(pdf_text, lista_textos_antes, lista_textos_seguintes)
    
    if(texto_localizado == True and texto_obtido.lstrip() == ''):
        texto, texto_obtido, texto_localizado = get_text_before_by_list(pdf_text, lista_textos_antes)


    return texto, texto_obtido, texto_localizado
    
def get_education(pdf_text: str, person_name: str)->tuple:
    # person_name, pdf_text = remove_after()
    
    # Vir do banco de dados
    lista_textos_antes = 'Formação acadêmica,Education,Formación académica'
    lista_textos_seguintes = f''

    return get_text_before_by_list(pdf_text, lista_textos_antes)
    
