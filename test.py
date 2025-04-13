import speedtest
import os
import platform
import subprocess
import matplotlib.pyplot as plt
from scapy.all import *  # Para a versão avançada (opcional)
from scapy.layers.inet import ICMP


def testar_velocidade():
    try:
        st = speedtest.Speedtest()

        print("\nObtendo melhor servidor...")
        server = st.get_best_server()
        print(f"Servidor selecionado: {server['host']} ({server['country']})")

        print("\nTestando velocidade de download...")
        download = st.download() / 1_000_000  # Converter para Mbps
        print("Testando velocidade de upload...")
        upload = st.upload() / 1_000_000  # Converter para Mbps

        print("\n--- Resultados de Velocidade ---")
        print(f"Download: {download:.2f} Mbps")
        print(f"Upload: {upload:.2f} Mbps")
        print(f"Ping: {st.results.ping:.2f} ms")

        return server['host']  # Retorna o host para usar no traceroute

    except speedtest.ConfigRetrievalError:
        print("Erro: Não foi possível conectar aos servidores Speedtest")
        return None
    except Exception as e:
        print(f"Erro inesperado: {type(e).__name__} - {str(e)}")
        return None


def tracert_simples(destino):
    """Versão simples usando o comando do sistema"""
    print(f"\nIniciando traceroute para {destino}...")

    if platform.system().lower() == "windows":
        comando = ["tracert", "-d", destino]
    else:  # Linux/Mac
        comando = ["traceroute", "-n", destino]

    try:
        subprocess.run(comando, check=True)
    except subprocess.CalledProcessError as e:
        print(f"Erro ao executar traceroute: {e}")


def tracert_avancado(destino, max_hops=30):
    """Versão avançada com gráfico (requer privilégios de admin)"""
    print(f"\nTraceroute avançado para {destino}...")

    try:
        times = []
        ips = []

        for ttl in range(1, max_hops + 1):
            pkt = IP(dst=destino, ttl=ttl) / ICMP()
            reply = sr1(pkt, verbose=0, timeout=2)

            if reply is None:
                print(f"{ttl}: *")
                times.append(None)
                ips.append("*")
            else:
                rtt = (reply.time - pkt.sent_time) * 1000  # ms
                print(f"{ttl}: {reply.src}  {rtt:.2f}ms")
                times.append(rtt)
                ips.append(reply.src)

                if reply.src == destino:
                    break

        # Plotar gráfico
        hops = range(1, len(times) + 1)
        plt.figure(figsize=(10, 5))
        plt.plot(hops, times, 'b-o')
        plt.xlabel('Número do Hop')
        plt.ylabel('Tempo (ms)')
        plt.title(f'Traceroute para {destino}')
        plt.grid(True)
        plt.show()

    except Exception as e:
        print(f"Erro no traceroute avançado: {e}")


def menu():
    print("\n" + "=" * 50)
    print("DIAGNÓSTICO DE REDE COMPLETO".center(50))
    print("=" * 50)
    print("1. Testar velocidade da internet")
    print("2. Executar traceroute simples")
    print("3. Executar traceroute avançado (com gráfico)")
    print("4. Testar velocidade E traceroute")
    print("5. Sair")

    while True:
        try:
            opcao = int(input("\nEscolha uma opção (1-5): "))
            if 1 <= opcao <= 5:
                return opcao
            print("Por favor, digite um número entre 1 e 5.")
        except ValueError:
            print("Entrada inválida. Digite um número.")


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