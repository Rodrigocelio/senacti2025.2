import os

SERVICOS = {
        1: {"nome": "Corte de cabelo", 
            "descricao": "Corte moderno com acabamento na navalha.", 
            "valor": 30.00},
        2: {"nome": "Barba", 
            "descricao": "Barba desenhada e hidratação com toalha quente.", "valor": 25.00},
        3: {"nome": "Printura", 
            "descricao": "Printura de cabelo com tinta temporária.", 
            "valor": 15.00},
        4: {"nome": "Pacote Completo", 
            "descricao": "Cabelo + Barba + Printura com desconto especial.", "valor": 60.00}
    }

SERVICOS1 = os.path.join(os.path.dirname(__file__), "..", "data", "tabela_servicos.xlsx")

AGENDAMENTOS = os.path.join(os.path.dirname(__file__), "..", "data", "agendamentos.xlsx")

PROFISIONAIS1 = {1: "Joao", 2: "Abraao", 3: "Rodrigo"}
PROFISIONAIS = os.path.join(os.path.dirname(__file__), "..", "data", "profissionais.xlsx")

WEBHOOK_URL = "https://hook.us2.make.com/1adv2sv028glhonhwu3n1mxwzn7dgsp6"

HEADERS = {"Content-Type": "application/json",}

CLIENTES_DB = os.path.join(os.path.dirname(__file__), "..", "data", "clientes_db.xlsx")

# Persistir as credenciais.
ARQ_CREDENCIAIS = os.path.join(os.path.dirname(__file__), "..", "data", "credenciais.txt")

# # Persistir as credenciais.
ARQ_CHAVE = os.path.join(os.path.dirname(__file__), "..", "data", "chave.key")