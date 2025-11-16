from time import sleep
from rich import print
from rich.panel import Panel

from utils.console_tools import (limpar_tela, mostrar_logo_personalizado,
                                 mostrar_barra_carregamento, solicitar_login, 
                                 mostrar_menu)

from utils.security import (logar, cadastrar_adm)

from core.data_handler import (cadastrar_cliente, buscar_clientes, 
                               listar_clientes)

from core.data_handler import (criar_agendamento, buscar_agendamento, 
                               listar_agendamentos, cancelar_agendamento)

from utils.supplementation import (PROFISIONAIS, SERVICOS)


def main():
    """Fluxo de execução de todo sistema."""    
    clientes = []
    agendamentos = []

    mostrar_barra_carregamento()
    
    # login
    while True:
        mostrar_logo_personalizado()
        print(Panel("", title="Login", style="white"))
        # verifica se login é válido.
        # TODO: veriricar se funciona sem a comparação.
        usuario, senha = solicitar_login()
        if logar(usuario, senha):
            print("\n Entrando...")
            sleep(1)
            limpar_tela()
            break
        else:
            print("""\nUsuário ou senha inválido. TENTE NOVAMENTE!""")
            limpar_tela()
        
    # loop principal
    while True:
        mostrar_logo_personalizado()
        mostrar_menu()
        try:
            opt = str(input(" >>> "))
        # Encerra o programa de forma elegante caso o usuário 
        # tecle 'ctrl + c'.
        except KeyboardInterrupt:
            print("\n Encerando o programa...")
            sleep(1.5)
            print("\n Programa interrupido abruptamente.")
            print(" Por favor execute novamente.")
            break
        
        match opt:
            # Abre a telinha para cadastrar cliente.
            case "1":
                limpar_tela()
                mostrar_logo_personalizado()
                cadastrar_cliente(clientes)
            # Mostra um relatório com todos os clientes cadastrados.
            case "2":
                limpar_tela()
                mostrar_logo_personalizado()
                listar_clientes(clientes)
                # Congela a tela até que o usuário digite alguma coisa.
                if type(input("\n\n\n Aperte 'ENTER' para voltar: ")) == str:
                    limpar_tela()
                    continue
            # Abre a telinha para buscar um cliente especifico.
            case "3":
                limpar_tela()
                mostrar_logo_personalizado()
                buscar_clientes(clientes)
                # Congela a tela até que o usuário digite alguma coisa
                if type(input("\n\n\n Aperte 'ENTER' para voltar: ")) == str:
                    limpar_tela()
                    continue
            # Abre uma tela para criar um agendamento.
            case "4":
                limpar_tela()
                mostrar_logo_personalizado()
                criar_agendamento(clientes, agendamentos, PROFISIONAIS, SERVICOS)
                sleep(3)
            case "5":
                limpar_tela()
                mostrar_logo_personalizado()
                listar_agendamentos(agendamentos)
                 # Congela a tela até que o usuário digite alguma coisa
                if type(input("\n\n\n Aperte 'ENTER' para voltar: ")) == str:
                    limpar_tela()
                    continue
            # Busca um agendamento especifico.
            case "6":
                limpar_tela()
                mostrar_logo_personalizado()
                buscar_agendamento(agendamentos)
                # Congela a tela até que o usuário digite alguma coisa
                if type(input("\n\n\n Aperte 'ENTER' para voltar: ")) == str:
                    limpar_tela()
                    continue
            # Cencela um agendamento.
            case "7":
                limpar_tela()
                mostrar_logo_personalizado()
                cancelar_agendamento(agendamentos)
                # Congela a tela até que o usuário digite alguma coisa
                if type(input("\n\n\n Aperte 'ENTER' para voltar: ")) == str:
                    limpar_tela()
                    continue
            # Cadastro um adm no sistema.
            case "8":
                limpar_tela()
                mostrar_logo_personalizado()
                usuario, senha = solicitar_login()
                cadastrar_adm(usuario, senha)
            # Encerra o programa.
            case "9":
                print("\n Encerando o programa...")
                sleep(1.5)
                break
        limpar_tela()


# Executa o sistema
if __name__ == "__main__":
    main()