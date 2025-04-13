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