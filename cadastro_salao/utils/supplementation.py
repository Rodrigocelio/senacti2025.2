from os.path import join, dirname

# Link do webhook e cabeçalhos
WEBHOOK_URL = "https://hook.us2.make.com/1adv2sv028glhonhwu3n1mxwzn7dgsp6"
HEADERS = {"Content-Type": "application/json",}

# Caminho para os arquivos que alimentam a aplicação.
CLIENTES_DB = join(dirname(__file__), "..", "data", "clientes_db.xlsx")
ARQ_CREDENCIAIS = join(dirname(__file__), "..", "data", "credenciais.txt")
ARQ_CHAVE = join(dirname(__file__), "..", "data", "chave.key")
PROFISIONAIS = join(dirname(__file__), "..", "data", "profissionais.xlsx")
AGENDAMENTOS = join(dirname(__file__), "..", "data", "agendamentos.xlsx")
SERVICOS = join(dirname(__file__), "..", "data", "servicos.xlsx")
