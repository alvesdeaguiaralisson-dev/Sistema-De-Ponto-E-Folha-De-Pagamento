

import csv  # Importa a biblioteca nativa do Python para trabalhar com arquivos CSV

ARQUIVO_FUNCIONARIOS = "funcionarios.csv"  # Nome do arquivo CSV que serve como banco de dados

# -------------------------------------------------------
# Cria o arquivo CSV de funcionários se ele não existir
# -------------------------------------------------------
def criar_arquivo():
    try:
        with open(ARQUIVO_FUNCIONARIOS, "r"):  # Tenta abrir o arquivo para leitura
            pass  # Se conseguiu abrir, não faz nada
    except FileNotFoundError:  # Se o arquivo não existe, cai aqui
        with open(ARQUIVO_FUNCIONARIOS, "w", newline="") as arquivo:  # Cria o arquivo
            writer = csv.writer(arquivo)  # Prepara para escrever no CSV
            writer.writerow(["ID", "NOME", "SALARIO", "DEPENDENTES"])  # Escreve o cabeçalho


# -------------------------------------------------------
# Cadastra um novo funcionário no CSV (somente adiciona,
# nunca edita registros anteriores - norma IEEE)
# -------------------------------------------------------
def cadastrar_funcionario(id_func, nome, salario, dependentes):
    criar_arquivo()  # Garante que o arquivo existe antes de escrever

    # Verifica se o ID já está cadastrado para evitar duplicatas
    funcionarios = carregar_funcionarios()  # Carrega todos os funcionários do CSV
    if id_func in funcionarios:  # Se o ID já existe no dicionário
        print("Funcionário já cadastrado!")  # Avisa o usuário
        return  # Encerra a função sem cadastrar

    with open(ARQUIVO_FUNCIONARIOS, "a", newline="") as arquivo:  # Abre em modo append (só adiciona)
        writer = csv.writer(arquivo)  # Prepara para escrever
        writer.writerow([id_func, nome, salario, dependentes])  # Adiciona linha com os dados

    print("Funcionário cadastrado com sucesso!")  # Confirma o cadastro


# -------------------------------------------------------
# Carrega todos os funcionários do CSV e retorna
# um dicionário com ID como chave
# -------------------------------------------------------
def carregar_funcionarios():
    funcionarios = {}  # Cria um dicionário vazio para guardar os funcionários

    try:
        with open(ARQUIVO_FUNCIONARIOS, "r") as arquivo:  # Abre o CSV para leitura
            leitor = csv.reader(arquivo)  # Prepara para ler linha por linha
            next(leitor)  # Pula o cabeçalho (primeira linha)

            for linha in leitor:  # Percorre cada linha do arquivo
                id_func, nome, salario, dependentes = linha  # Separa os dados da linha
                funcionarios[id_func] = {  # Adiciona ao dicionário usando o ID como chave
                    "nome": nome,  # Nome do funcionário
                    "salario": float(salario),  # Salário convertido para número decimal
                    "dependentes": int(dependentes)  # Dependentes convertido para número inteiro
                }

    except FileNotFoundError:  # Se o arquivo não existir ainda
        pass  # Retorna o dicionário vazio sem erro

    return funcionarios  # Retorna o dicionário com todos os funcionários


# -------------------------------------------------------
# Busca um funcionário específico pelo ID
# -------------------------------------------------------
def buscar_funcionario(id_func):
    funcionarios = carregar_funcionarios()  # Carrega todos os funcionários do CSV

    if id_func in funcionarios:  # Verifica se o ID existe no dicionário
        return funcionarios[id_func]  # Retorna os dados do funcionário encontrado
    else:
        return None  # Retorna None se não encontrou o funcionário


# -------------------------------------------------------
# Lista todos os funcionários cadastrados na tela
# -------------------------------------------------------
def listar_funcionarios():
    funcionarios = carregar_funcionarios()  # Carrega todos os funcionários do CSV

    if len(funcionarios) == 0:  # Verifica se o dicionário está vazio
        print("Nenhum funcionário cadastrado.")  # Avisa que não há ninguém
        return  # Encerra a função

    print("\n--- FUNCIONÁRIOS CADASTRADOS ---")  # Título da listagem
    for id_func in funcionarios:  # Percorre cada ID no dicionário
        func = funcionarios[id_func]  # Pega os dados do funcionário atual
        # Exibe os dados formatados na tela
        print("ID:", id_func, "| Nome:", func["nome"], "| Salário: R$", func["salario"], "| Dependentes:", func["dependentes"])
