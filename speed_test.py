import speedtest

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