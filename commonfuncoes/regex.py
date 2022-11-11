import regex


def buscar_texto_regex(texto:str, padrao: str, posicao: int) -> str:
    match = regex.findall(padrao, texto)
    return match[posicao]

def buscar_texto_regex_data_completa(texto:str, posicao:int = 0) -> str:
    
    padrao = r"([0-9]{2}\/[0-9]{2}\/[0-9]{4})"
    return buscar_texto_regex(texto, padrao, posicao)

def buscar_texto_regex_mes(texto:str, posicao:int = 0) -> str:
    
    padrao = r"([0-9]{2}\/[0-9]{4})"
    return buscar_texto_regex(texto, padrao, posicao)

def buscar_texto(texto:str, padrao: str) -> bool:
    if regex.search(padrao,texto): return True
    else: return False

def buscar_matricula(texto:str) -> str:
    return(texto)

def buscar_cod_barra(texto:str, padrao:str, posicao:int=0) -> str:
    padrao = r"([0-9]{11}-[0-9]{1} [0-9]{11}-[0-9]{1} [0-9]{11}-[0-9]{1} [0-9]{11}-[0-9]{1})"
    return buscar_texto_regex(texto, padrao, posicao)

def buscar_num_hidro(texto:str, padrao:str, posicao: str=0) -> str:
    padrao = r"[A-Z, 0-9]{10}"
    return buscar_texto_regex(texto, padrao, posicao)

