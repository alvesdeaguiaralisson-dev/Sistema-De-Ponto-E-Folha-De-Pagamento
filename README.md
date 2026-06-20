# Sistema de Ponto e Folha de Pagamento

Sistema de controle de jornada e cálculo de folha de pagamento desenvolvido em Python, implementando as principais regras da legislação trabalhista brasileira (CLT).

Projeto acadêmico desenvolvido como mini-TCC do curso de Análise e Desenvolvimento de Sistemas (ADS) — UNIP.

## O que o sistema faz

- Cadastro de funcionários (ID, nome, salário base, dependentes)
- Registro de ponto (entrada/saída) com timestamp automático
- Cálculo de horas trabalhadas por emparelhamento de registros
- Cálculo de folha de pagamento com os seguintes descontos:
  - **INSS** — tabela progressiva 2024
  - **IRRF** — com base de cálculo ajustada por número de dependentes
  - **Vale-Transporte** — desconto de 6% sobre o salário bruto
  - **Faltas e DSR** — desconto proporcional de Descanso Semanal Remunerado
- Dois pontos de acesso separados: terminal do RH (autenticado) e terminal do funcionário (autoatendimento)

## Por que os registros de ponto nunca são editados

O arquivo `ponto.csv` funciona em modo **append-only**: cada registro recebe um Número Sequencial de Registro (NSR) e nunca é alterado ou removido depois de criado. Essa é a mesma lógica usada por sistemas de ponto eletrônico homologados — qualquer correção exige um novo registro, nunca a edição do histórico, preservando a auditabilidade dos dados.

## Estrutura do projeto

```
sistema-ponto/
├── main.py              # Terminal do RH — cadastro, listagem e cálculo de folha
├── terminal_ponto.py    # Terminal do funcionário — bater ponto (entrada/saída)
├── funcionarios.py       # Cadastro e consulta de funcionários (CSV)
├── ponto.py              # Registro de ponto e cálculo de horas trabalhadas
├── Def_Salarios.py       # Regras de cálculo: INSS, IRRF, VT, DSR
├── exemplos/              # Dados de demonstração (5 funcionários, 1 mês de ponto)
├── .env.example           # Modelo de variáveis de ambiente
└── .gitignore
```

## Como rodar

Requer apenas Python 3 — sem dependências externas.

```bash
git clone https://github.com/alvesdeaguiaralisson-dev/sistema-ponto.git
cd sistema-ponto
```

Defina a senha de acesso do RH copiando o arquivo de exemplo:

```bash
cp .env.example .env
# edite o .env e defina sua própria senha em SENHA_RH
```

No Linux/Mac, exporte a variável antes de rodar (ou use um pacote como `python-dotenv` se preferir carregamento automático):

```bash
export SENHA_RH=sua_senha
python3 main.py
```

No Windows (PowerShell):

```powershell
$env:SENHA_RH="sua_senha"
python main.py
```

Para o terminal de autoatendimento do funcionário (sem senha):

```bash
python3 terminal_ponto.py
```

## Dados de exemplo

A pasta `exemplos/` contém `funcionarios_exemplo.csv` e `ponto_exemplo.csv` com 5 funcionários fictícios e um mês de registros de ponto, para quem quiser ver o sistema processando dados sem precisar cadastrar do zero. Para testar com eles, copie os arquivos para a raiz do projeto renomeando para `funcionarios.csv` e `ponto.csv`.

## Possíveis evoluções

- Migração de CSV para banco de dados relacional (SQLite/PostgreSQL)
- Interface web (Flask/Django) no lugar do terminal
- Testes automatizados para as regras de cálculo (INSS, IRRF, DSR)

## Autor

**Alisson Alves**
[github.com/alvesdeaguiaralisson-dev](https://github.com/alvesdeaguiaralisson-dev) · alvesdeaguiaralisson@gmail.com
