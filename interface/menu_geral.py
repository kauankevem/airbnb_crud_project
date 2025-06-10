# Menu principal do sistema
from interface.menu_hospede import menu_hospede
from interface.menu_anfitriao import menu_anfitriao
from interface.menu_admin import menu_admin

def menu_geral():
    while True:
        print("\n=== BEM-VINDO AO AIRBNB-LÂNDIA ===")
        print("1 - Acessar como Hóspede")
        print("2 - Acessar como Anfitrião")
        print("3 - Acesso Administrativo")
        print("4 - Sair")
        opcao = input("Escolha uma opção: ")

        if opcao == '1':
            menu_hospede()
        elif opcao == '2':
            menu_anfitriao()
        elif opcao == '3':
            menu_admin()
        elif opcao == '4':
            print("Encerrando o sistema...")
            break
        else:
            print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
    menu_geral()
