
def formatar_dois_digitos(numero:str):
    if(int(numero) < 10 and len(numero) < 2):
        return f"0{numero}"
    return numero

def buscar_mes_numero(mes_nome:str) -> str:

    if "jan" in mes_nome.lower():
        return "01"

    if "fev" in mes_nome.lower():
        return "02"

    if "mar" in mes_nome.lower():
        return "03"

    if "abr" in mes_nome.lower():
        return "04"

    if "mai" in mes_nome.lower():
        return "05"

    if "jun" in mes_nome.lower():
        return "06"

    if "jul" in mes_nome.lower():
        return "07"

    if "ago" in mes_nome.lower():
        return "08"

    if "set" in mes_nome.lower():
        return "09"

    if "out" in mes_nome.lower():
        return "10"

    if "nov" in mes_nome.lower():
        return "11"

    if "dez" in mes_nome.lower():
        return "12"


def buscar_mes_nome(nome_mes:str) -> str:
    if "01" in nome_mes:
        return "Janeiro"
    
    if "02" in nome_mes:
        return "Fevereiro"
    
    if "03" in nome_mes:
        return "Março"
    
    if "04" in nome_mes:
        return "Abril"
    
    if "05" in nome_mes:
        return "Maio"
    
    if "06" in nome_mes:
        return "Junho"
    
    if "07" in nome_mes:
        return "Julho"
    
    if "08" in nome_mes:
        return "Agosto"
    
    if "09" in nome_mes:
        return "Setembro"
    
    if "10" in nome_mes:
        return "Outubro"
    
    if "11" in nome_mes:
        return "Novembro"
    
    if "12" in nome_mes:
        return "Dezembro"