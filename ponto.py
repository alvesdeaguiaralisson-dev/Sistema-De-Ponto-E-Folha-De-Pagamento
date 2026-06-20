import csv  # Importa a biblioteca nativa do Python para trabalhar com arquivos CSV
from datetime import datetime  # Importa datetime para pegar data e hora atual

ARQUIVO_PONTO = "ponto.csv"  # Nome do arquivo CSV que guarda os registros de ponto


# -------------------------------------------------------
# Cria o arquivo de ponto se ele não existir ainda
# -------------------------------------------------------
def criar_arquivo():
    try:
        with open(ARQUIVO_PONTO, "r"):  # Tenta abrir o arquivo para leitura
            pass  # Se conseguiu abrir, não faz nada
    except FileNotFoundError:  # Se o arquivo não existe, cai aqui
        with open(ARQUIVO_PONTO, "w", newline="") as arquivo:  # Cria o arquivo
            writer = csv.writer(arquivo)  # Prepara para escrever no CSV
            writer.writerow(["NSR", "ID", "DATA", "HORA", "TIPO"])  # Escreve o cabeçalho


# -------------------------------------------------------
# Conta quantas linhas de registro existem no arquivo
# para gerar o número sequencial (NSR) corretamente
# -------------------------------------------------------
def contar_linhas():
    try:
        with open(ARQUIVO_PONTO, "r") as arquivo:  # Abre o arquivo para leitura
            return sum(1 for _ in arquivo) - 1  # Conta linhas e desconta o cabeçalho
    except FileNotFoundError:  # Se o arquivo não existe ainda
        return 0  # Retorna 0 pois não há registros


# -------------------------------------------------------
# Registra um evento de ponto (ENTRADA ou SAIDA)
# Seguindo a norma IEEE: somente adiciona, nunca edita
# -------------------------------------------------------
def registrar_ponto(id_func, tipo):
    criar_arquivo()  # Garante que o arquivo existe antes de escrever

    agora = datetime.now()  # Pega o momento atual (data e hora)
    data = agora.strftime("%d/%m/%Y")  # Formata a data como DD/MM/AAAA
    hora = agora.strftime("%H:%M")  # Formata a hora como HH:MM

    nsr = contar_linhas() + 1  # Gera o próximo número sequencial de registro

    with open(ARQUIVO_PONTO, "a", newline="") as arquivo:  # Abre em modo append (só adiciona)
        writer = csv.writer(arquivo)  # Prepara para escrever
        writer.writerow([nsr, id_func, data, hora, tipo])  # Adiciona a nova linha

    print(tipo + " registrada com sucesso!")  # Confirma o registro para o usuário


# -------------------------------------------------------
# Registra entrada do funcionário
# -------------------------------------------------------
def registrar_entrada(id_func):
    registrar_ponto(id_func, "ENTRADA")  # Chama a função geral passando o tipo ENTRADA


# -------------------------------------------------------
# Registra saída do funcionário
# Verifica se existe uma entrada sem saída correspondente
# -------------------------------------------------------
def registrar_saida(id_func):
    entradas = 0  # Contador de entradas do funcionário
    saidas = 0    # Contador de saídas do funcionário

    try:
        with open(ARQUIVO_PONTO, "r") as arquivo:  # Abre o arquivo para leitura
            leitor = csv.reader(arquivo)  # Prepara para ler linha por linha
            next(leitor)  # Pula o cabeçalho

            for linha in leitor:  # Percorre cada linha do arquivo
                _, id_reg, data, hora, tipo = linha  # Separa os dados da linha

                if id_reg == id_func:  # Filtra apenas os registros do funcionário
                    if tipo == "ENTRADA":  # Se for uma entrada
                        entradas += 1  # Incrementa o contador de entradas
                    elif tipo == "SAIDA":  # Se for uma saída
                        saidas += 1  # Incrementa o contador de saídas

    except FileNotFoundError:  # Se o arquivo não existir
        print("Nenhum registro encontrado.")  # Avisa o usuário
        return  # Encerra a função

    if entradas > saidas:  # Se há mais entradas do que saídas, existe uma entrada pendente
        registrar_ponto(id_func, "SAIDA")  # Registra a saída
    else:
        print("Nenhuma entrada pendente encontrada.")  # Avisa que não há entrada aberta


# -------------------------------------------------------
# Calcula o total de horas trabalhadas pelo funcionário
# Emparelha cada ENTRADA com a próxima SAIDA correspondente
# -------------------------------------------------------
def calcular_horas(id_func):
    total_horas = 0  # Acumulador do total de horas trabalhadas
    entradas = []    # Lista temporária para guardar os horários de entrada

    try:
        with open(ARQUIVO_PONTO, "r") as arquivo:  # Abre o arquivo para leitura
            leitor = csv.reader(arquivo)  # Prepara para ler linha por linha
            next(leitor)  # Pula o cabeçalho

            for linha in leitor:  # Percorre cada linha do arquivo
                _, id_reg, data, hora, tipo = linha  # Separa os dados da linha

                if id_reg != id_func:  # Se não for o funcionário buscado
                    continue  # Pula para a próxima linha

                if tipo == "ENTRADA":  # Se for uma entrada
                    entradas.append(hora)  # Guarda o horário de entrada na lista

                elif tipo == "SAIDA" and len(entradas) > 0:  # Se for saída e há entrada pendente
                    hora_entrada = entradas.pop(0)  # Pega a entrada mais antiga da lista
                    h1 = datetime.strptime(hora_entrada, "%H:%M")  # Converte entrada para datetime
                    h2 = datetime.strptime(hora, "%H:%M")  # Converte saída para datetime
                    horas = (h2 - h1).seconds / 3600  # Calcula a diferença em horas
                    total_horas += horas  # Soma ao total

    except FileNotFoundError:  # Se o arquivo não existir
        return 0  # Retorna 0 horas

    return total_horas  # Retorna o total de horas trabalhadas
