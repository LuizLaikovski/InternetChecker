from speed_test import testar_velocidade
from traceroute import tracert_simples, tracert_avancado
from menu import menu

def main():
    while True:
        opcao = menu()

        if opcao == 1:
            testar_velocidade()
        elif opcao == 2:
            destino = input("Digite o endereço de destino (ex: google.com): ")
            tracert_simples(destino)
        elif opcao == 3:
            destino = input("Digite o endereço de destino (ex: google.com): ")
            tracert_avancado(destino)
        elif opcao == 4:
            host = testar_velocidade()
            if host:
                tracert_simples(host)
        elif opcao == 5:
            print("Encerrando o programa...")
            break

if __name__ == "__main__":
    main()