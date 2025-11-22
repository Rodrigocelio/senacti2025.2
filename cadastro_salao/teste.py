from utils.supplementation import CLIENTES_DB, PROFISIONAIS
import pandas as pd

lista = [{
        "nome": "tiago",
        "telefone": "8598659856",
        "email": "tiago@example.com",
        "tag": "cliente"
    }, {
        "nome": "maria",
        "telefone": "8598659857",
        "email": "maria@example.com",
        "tag": "cliente"
    }, {
        "nome": "joao",
        "telefone": "8598659858",
        "email": "joao@example.com",
        "tag": "cliente"
    }]

clientes = {"nome": "tiago", "telefone": "8598659856", "email": "tiago@example.com", "tag": "cliente"}

def _armazenar_clientes_DB(clientes: dict) -> bool:
    """"""
    df = pd.DataFrame([clientes])
    print(df.head())
    #if not os.path.exists(CLIENTES_DB):
        #with open(CLIENTES_DB, 'w', encoding='utf-8') as arq_clientes_DB:
            #df.to_excel(CLIENTES_DB, sheet_name="clientes", index=False)
    pass

#_armazenar_clientes_DB(clientes)



import os
import pandas as pd

def _buscar_profissionais():
    """"""
    try:
        if not os.path.exists(PROFISIONAIS):
            return []
        
        df = pd.read_excel(PROFISIONAIS, sheet_name="profissionais")
        profissionais = df.to_dict(orient="records")
        return profissionais
    except Exception as erro:
        raise Exception(f"{erro}")
    

a = {1: "abraao"}
print('1' in a)