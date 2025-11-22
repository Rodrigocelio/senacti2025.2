import os
from cryptography.fernet import Fernet
import base64
from utils.supplementation import (ARQ_CHAVE, ARQ_CREDENCIAIS)


def _carregar_ou_gerar_chave(arq_chave):
    """Carrega a chave do arquivo ou gera uma nova e salva em arq_chave.
    Return -> bytes
    """
    try:
        with open(arq_chave, "rb") as arq_chave:
            return arq_chave.read()
    except FileNotFoundError:
        chave = Fernet.generate_key()
        with open(arq_chave, "wb") as arq_chave:
            arq_chave.write(chave)
            return chave        


# Implementando criptografia simétrica.
chave = _carregar_ou_gerar_chave(ARQ_CHAVE)
fernet = Fernet(chave)


def _criptografar_credenciais(usuario, senha):
    """Recebe usuario e senha e criptografa utilizando uma chave simétrica.
    Return -> bytes
    """
    try:
        usuario = fernet.encrypt(usuario.encode())
        senha = fernet.encrypt(senha.encode())
    except Exception as erro:
        raise Exception(f"Erro identificado: {erro}")
    return usuario, senha


def _descriptografar_credenciais(credenciais):
    """Recebe as credenciais em texto e descriptografa utilizando uma chave 
    simétrica.
    Return -> str
    """
    try:
        credenciais = fernet.decrypt(credenciais)
    except Exception as erro:
        raise Exception(f"Erro identificado: {erro}")
    return credenciais


def cadastrar_adm(usuario, senha):
    """Cadastra um novo administrador ao sistema."""
    if os.path.exists(ARQ_CREDENCIAIS):
        # Formata para o padrão desejado.
        usuario = f"-{usuario}\n"
        senha = f":{senha}\n\n"
        
        with open(ARQ_CREDENCIAIS, "a") as arq_credenciais:
            # Criptografando
            usuario, senha = _criptografar_credenciais(usuario, senha)

            # Convertendo texto criptografado para ASCII.
            usuario = base64.b64encode(usuario).decode()
            senha = base64.b64encode(senha).decode()

            # Grava cada token em sua própria linha (facilita a leitura)
            arq_credenciais.write(usuario + "\n")
            arq_credenciais.write(senha + "\n")


def buscar_credenciais_registradas():
    """"""
    adms = {'usuarios': [], 'senhas': []}
    try:
        if not os.path.exists(ARQ_CREDENCIAIS):
            return adms

        with open(ARQ_CREDENCIAIS, 'r') as arq_credenciais:
            for linha_pura in arq_credenciais:
                linha = linha_pura.strip()
                if not linha:
                    continue
                try:
                    # Convertendo ASCII para texto criptografado.
                    token = base64.b64decode(linha)
                    # Descriptografando para bytes
                    token = _descriptografar_credenciais(token)
                    # Convertendo bytes para str.
                    token = token.decode()
                except (ValueError, TypeError):
                    # Pula e continua.
                    continue

                # O texto pode conter múltiplas linhas; processa cada uma
                for linha in token.splitlines():
                    if linha.startswith("-"):
                        adms['usuarios'].append(linha.removeprefix("-"))
                    elif linha.startswith(":"):
                        adms['senhas'].append(linha.removeprefix(":"))
    except OSError as erro:
        print(f"Erro desconhecido: {erro}")
    return adms


def logar(usuario, senha):
    """Verifica se o usuário é um dos adminitradores do sistema. 
    Os valores de login estão em um dicionário que é consultado para validar o 
    acesso.
    """ 
    adms = buscar_credenciais_registradas()
    for par_credencial in zip(adms['usuarios'], adms['senhas']):
        if usuario == par_credencial[0] and senha == par_credencial[1]:
            return 1
    return 0
