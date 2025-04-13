import platform
import subprocess
import matplotlib.pyplot as plt
from scapy.all import *
from scapy.layers.inet import ICMP

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