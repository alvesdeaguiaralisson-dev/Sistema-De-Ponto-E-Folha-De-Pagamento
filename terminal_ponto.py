import ponto  # Importa o módulo de ponto para registrar entrada e saída
import funcionarios  # Importa o módulo de funcionários para validar o ID

# -------------------------------------------------------
# Loop principal - fica rodando até o funcionário sair
# -------------------------------------------------------
while True:
    print("\n=== BATER PONTO ===")
    print("1. Entrada")
    print("2. Saída")
    print("3. Sair")

    opcao = input("Escolha: ")  # Lê a opção do funcionário

    if opcao == "1" or opcao == "2":  # Se escolheu entrada ou saída
        id_func = input("Digite seu ID: ")  # Pede o ID do funcionário

        func = funcionarios.buscar_funcionario(id_func)  # Verifica se o ID existe no cadastro

        if func is None:  # Se o ID não foi encontrado
            print("ID não encontrado! Procure o RH.")  # Avisa o funcionário
        else:
            print("Olá, " + func["nome"] + "!")  # Saúda o funcionário pelo nome

            if opcao == "1":  # Se escolheu entrada
                ponto.registrar_entrada(id_func)  # Registra a entrada no ponto.csv
            elif opcao == "2":  # Se escolheu saída
                ponto.registrar_saida(id_func)  # Registra a saída no ponto.csv

    elif opcao == "3":  # Se escolheu sair
        print("Até logo!")  # Mensagem de despedida
        break  # Encerra o programa

    else:
        print("Opção inválida!")  # Avisa que a opção não existe
