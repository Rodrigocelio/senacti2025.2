import os
from time import sleep
from getpass import getpass
from pyfiglet import figlet_format
from rich.console import Console
from rich.panel import Panel
from rich.text import Text


console = Console()


def limpar_tela():
    """Limpa a tela do console de forma multiplataforma.
    Essa função funciona para Linux, Mac e Windows.
    """
    if os.name == "nt":
        return os.system('cls')
    os.system('clear')


def mostrar_logo_personalizado():
    """Cria um logo renderizado pelo módulo pyfiglet e imprime centralizado 
    dentro de um painel definido pela biblioteca Rich. O logo do programa é uma
    ASCII Art.
    """
    logo = figlet_format("  BarberBack  ")
    painel = Panel(Text(logo, justify="center"))
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
        painel = Panel(Text(progresso, justify="center"), title="Carregando, aguarde!")
        console.print(painel, style="white")
        sleep(.1)
        limpar_tela()
        progresso += "//"


def solicitar_login():
    """Solicita as credenciais do usuário. A senha é solicitada de forma 
    segura. Ela não é exibida no terminal.
    """
    usuario = str(input(" Usuário: ")).strip()
    senha = getpass(" Senha: ").strip()
    return usuario, senha


def mostrar_menu():
    """Cria e imprime um menu formatado com a biblioteca Rich."""
    menu = """\n1. Cadastrar cliente\n2. Listar clientes\n3. Buscar cliente por nome\n4. Agendamento\n5. Ver agendamentos\n6. Buscar agendamento\n7. Cancelar agendamento\n8. Cadastrar Administrador\n9. Sair"""

    painel = Panel.fit(menu, title="=== Sistema de Cadastro de Clientes - Barbearia ===")
    console.print(painel, style="white", justify="left")
