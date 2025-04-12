import speedtest
import os


def verificarSinal(destino):
    try:
        st = speedtest.Speedtest()

        print("Obtendo melhor servidor...")
        st.get_best_server()

        print("Testando velocidade de download...")
        download_speed = st.download()  # Resultado em bits por segundo
        download_mbps = download_speed / 1_000_000  # Converter para Mbps

        print("Testando velocidade de upload...")
        upload_speed = st.upload()  # Resultado em bits por segundo
        upload_mbps = upload_speed / 1_000_000  # Converter para Mbps

        ping = st.results.ping

        os.system(f"tracert {destino}")

        print("\n--- Resultados ---")
        print(f"Download: {download_mbps:.2f} Mbps")
        print(f"Upload: {upload_mbps:.2f} Mbps")
        print(f"Ping: {ping:.2f} ms")

    except speedtest.ConfigRetrievalError:
        print("Erro: Não foi possível conectar aos servidores de teste")
    except Exception as e:
        print(f"Erro inesperado: {str(e)}")


if __name__ == "__main__":
    verificarSinal("https://github.com/luizlaikovski")