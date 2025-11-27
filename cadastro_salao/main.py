from time import sleep
from rich.panel import Panel
from rich.console import Console

from utils.console_tools import (limpar_tela, mostrar_logo_personalizado,
                                 mostrar_barra_carregamento, solicitar_login, 
                                 mostrar_menu_principal, 
                                 mostrar_menu_relatorios)

from utils.security import (logar, cadastrar_adm)

from core.data_handler import (cadastrar_cliente, buscar_clientes, 
                               listar_clientes, cadastrar_profissional,
                               cadastrar_servico)

from core.data_handler import (mostrar_horario_com_maior_demada,
                               mostrar_variabilidade_dos_valores_dos_servicos,
                               mostrar_tendencia_central_dos_valores_dos_servicos, mostrar_profissionai_mais_procurado,
                               mostrar_servico_mais_procurado) 

from core.app import executar_servidor

from core.data_handler import (criar_agendamento, buscar_agendamento, 
                               listar_agendamentos, cancelar_agendamento)


console = Console()


def main():
    """Fluxo de execução de todo sistema."""    
    
    mostrar_barra_carregamento()
    
    # login
    while True:
        mostrar_logo_personalizado()
        console.print(Panel("", title="Login", style="white"))
        # verifica se as credenciais são válidas.
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
        mostrar_menu_principal()
        try:
            opt = str(input(" O que deseja fazer?  "))
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
                cadastrar_cliente()
            # Mostra um relatório com todos os clientes cadastrados.
            case "2":
                limpar_tela()
                mostrar_logo_personalizado()
                listar_clientes()
                # Congela a tela até que o usuário digite alguma coisa.
                if type(input("\n\n\n Aperte 'ENTER' para voltar: ")) == str:
                    limpar_tela()
                    continue
            # Abre a telinha para buscar um cliente especifico.
            case "3":
                limpar_tela()
                mostrar_logo_personalizado()
                buscar_clientes()
                # Congela a tela até que o usuário digite alguma coisa
                if type(input("\n\n\n Aperte 'ENTER' para voltar: ")) == str:
                    limpar_tela()
                    continue
            # Abre uma tela para criar um agendamento.
            case "4":
                limpar_tela()
                mostrar_logo_personalizado()
                criar_agendamento()
                sleep(3)
            case "5":
                limpar_tela()
                mostrar_logo_personalizado()
                listar_agendamentos()
                 # Congela a tela até que o usuário digite alguma coisa
                if type(input("\n\n\n Aperte 'ENTER' para voltar: ")) == str:
                    limpar_tela()
                    continue
            # Busca um agendamento especifico.
            case "6":
                limpar_tela()
                mostrar_logo_personalizado()
                buscar_agendamento()
                # Congela a tela até que o usuário digite alguma coisa
                if type(input("\n\n\n Aperte 'ENTER' para voltar: ")) == str:
                    limpar_tela()
                    continue
            # Cencela um agendamento.
            case "7":
                limpar_tela()
                mostrar_logo_personalizado()
                cancelar_agendamento()
                sleep(3)
            # Cadastro um adm no sistema.
            case "8":
                limpar_tela()
                mostrar_logo_personalizado()
                usuario, senha = solicitar_login()
                cadastrar_adm(usuario, senha)
            # Cadastra um novo profisional.
            case "9":
                limpar_tela()
                mostrar_logo_personalizado()
                cadastrar_profissional()
            # Cadastra um novo serviço.
            case "10":
                limpar_tela()
                mostrar_logo_personalizado()
                cadastrar_servico()
            # Mostra o menu de relatórios.
            case "11":
                limpar_tela()
                mostrar_logo_personalizado()
                mostrar_menu_relatorios()
                try:
                    opt2 = str(input(" O que deseja fazer?  "))
                    # Encerra o programa de forma elegante caso o usuário 
                    # tecle 'ctrl + c'.
                except KeyboardInterrupt:
                    print("\n Encerando o programa...")
                    sleep(1.5)
                    print("\n Programa interrupido abruptamente.")
                    print(" Por favor execute novamente.")
                    break
                match opt2:
                    case "1":
                        mostrar_horario_com_maior_demada()
                        if type(input("\n\n\n Aperte 'ENTER' para voltar: ")) == str:
                            limpar_tela()
                            continue
                    case "2":
                        mostrar_variabilidade_dos_valores_dos_servicos()
                        if type(input("\n\n\n Aperte 'ENTER' para voltar: ")) == str:
                            limpar_tela()
                            continue
                    case "3":
                        mostrar_tendencia_central_dos_valores_dos_servicos()
                        if type(input("\n\n\n Aperte 'ENTER' para voltar: ")) == str:
                            limpar_tela()
                            continue
                    case "4":
                        mostrar_profissionai_mais_procurado()
                        if type(input("\n\n\n Aperte 'ENTER' para voltar: ")) == str:
                            limpar_tela()
                            continue
                    case "5":
                        mostrar_servico_mais_procurado()
                        if type(input("\n\n\n Aperte 'ENTER' para voltar: ")) == str:
                            limpar_tela()
                            continue
                    case "6":
                        executar_servidor()
                    case "0":
                        continue
            # Encerra o programa.
            case "0":
                print("\n Encerando o programa...")
                sleep(1.5)
                break
        limpar_tela()


# Executa o sistema
if __name__ == "__main__":
    main()