import os
import pyfiglet
from rich.console import Console
from rich.panel import Panel
from rich.text import Text


def limpar_tela():
    """Limpa a tela do console de forma multiplataforma.
    Essa função funciona para Linux, Mac e Windows.
    """
    os.system('cls' if os.name == 'nt' else 'clear')


def mostrar_logo_personalizado():
    """Cria um logo renderizado pelo módulo pyfiglet 
    e imprime centralizado dentro de um painel definido 
    pela biblioteca Rich. O logo do programa é uma ASCII Art.
    """
    logo = pyfiglet.figlet_format("  BarberBack  ")
    logo_centralizado = Text(logo, justify="center")
    painel = Panel(logo_centralizado)
    console.print(painel, style="white")


def mostrar_barra_carregamento():
    """Mostra uma barra de carregamento. 
    A lógica é simples: temos um laço de um intervalo de 50, 
    a cada volta a variável progresso é incrementada com 
    dois caracteres de barra e no laço seguinte ela é impressa.
    """
    progresso = ""
    for p in range(50):
        mostrar_logo_personalizado()
        progresso_centralizado = Text(progresso, justify="center")
        painel = Panel(progresso_centralizado, title="Carregando, aguarde!")
        console.print(painel, style="white")
        sleep(.1)
        limpar_tela()
        progresso += "//"


def solicitar_login():
    """Solicita as credenciais do usuário com um diferencial. A senha é 
    solicitada de forma segura, ou seja, ela não é exibida no terminal.
    """
    usuario = input(" Usuário: ")
    senha = getpass.getpass(" Senha: ", stream=None)
    return usuario, senha
