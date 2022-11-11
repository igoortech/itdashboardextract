import commonfuncoes.regex as regex

def formatar_matricula(matricula: str) -> str:
    return matricula.replace("/","").replace("-","")

def formatar_valor(valor: str) -> str:
    return valor.replace(" ","").replace("R$","").replace(".","").replace(",", ".").replace("*", "")

def formatar_valor_americano(valor: str) -> str:
    return valor.replace(",", "")

def formatar_data_completa_com_barra(data: str)-> str:
    data = data.replace("/","")
    dia = data[:2]
    mes = data[2:4]
    ano = data[4:]
    data = f"{ano}{mes}{dia}"
    return data

def formatar_data_mes_referencia_com_barra(data:str) -> str:
    data = data.replace("/","")
    mes = data[:2]
    ano = data[2:6]
    data_referecia = f"{ano}{mes}"
    return data_referecia

def formatar_data_vencimento_dois_digitos(data:str) -> str:
    data = data.replace("/","")
    dia = data[:2]
    mes = data[2:4]
    ano = data[4:]
    data = f"{ano}{mes}{dia}"
    
    if len(ano) == 2:
        data = f"20{ano}{mes}{dia}" 
        return data