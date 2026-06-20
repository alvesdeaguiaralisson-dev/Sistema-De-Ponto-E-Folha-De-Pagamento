# -------------------------------------------------------
# Vale Transporte
# Desconto de 6% sobre o salário bruto
# -------------------------------------------------------
def vale_transporte(salario):
    return salario * 0.06  # Retorna 6% do salário como desconto de VT


# -------------------------------------------------------
# INSS - Instituto Nacional do Seguro Social
# Tabela progressiva 2024
# -------------------------------------------------------
def INSS(salario):
    if salario <= 1621.00:  # Faixa 1: até R$ 1.621,00
        return salario * 0.075  # Alíquota de 7,5%
    elif salario <= 2902.84:  # Faixa 2: até R$ 2.902,84
        return (salario * 0.09) - 24.32  # Alíquota de 9% com dedução
    elif salario <= 4354.27:  # Faixa 3: até R$ 4.354,27
        return (salario * 0.12) - 111.4  # Alíquota de 12% com dedução
    elif salario <= 8475.55:  # Faixa 4: até R$ 8.475,55
        return (salario * 0.14) - 198.49  # Alíquota de 14% com dedução
    else:  # Acima do teto: valor fixo no teto máximo
        return (8475.55 * 0.14) - 198.49  # Desconto máximo do INSS


# -------------------------------------------------------
# IRRF - Imposto de Renda Retido na Fonte
# Calcula com base no salário, dependentes e INSS já descontado
# -------------------------------------------------------
def IRRF(salario, dependentes, inss):
    base = salario - inss - (189.59 * dependentes)  # Base de cálculo: salário menos INSS e dedução por dependente

    if base <= 2428.80:  # Faixa isenta: até R$ 2.428,80
        print("Isento de IRRF")  # Informa que está isento
        return 0  # Sem desconto de IR
    elif base <= 2826.65:  # Faixa 1: até R$ 2.826,65
        return (base * 0.075) - 182.16  # Alíquota de 7,5% com dedução
    elif base <= 3751.05:  # Faixa 2: até R$ 3.751,05
        return (base * 0.15) - 394.16  # Alíquota de 15% com dedução
    elif base <= 4664.68:  # Faixa 3: até R$ 4.664,68
        return (base * 0.225) - 675.49  # Alíquota de 22,5% com dedução
    else:  # Faixa 4: acima de R$ 4.664,68
        return (base * 0.275) - 908.75  # Alíquota de 27,5% com dedução


# -------------------------------------------------------
# Faltas e DSR - Descanso Semanal Remunerado
# Calcula o desconto por faltas e o reflexo no DSR
# -------------------------------------------------------
def faltas_DSR(salario, dias_trabalhados, dias_uteis=22):
    valor_dia = salario / 30  # Calcula o valor de um dia de trabalho (salário dividido por 30)
    faltas = dias_uteis - dias_trabalhados  # Calcula quantos dias o funcionário faltou

    if faltas <= 4:  # Se faltou até 4 dias
        dsr = faltas  # O reflexo no DSR é igual ao número de faltas
    else:  # Se faltou mais de 4 dias
        dsr = 4  # O DSR é limitado a 4 dias de desconto

    desconto_faltas = valor_dia * faltas  # Calcula o desconto total pelas faltas
    desconto_dsr = valor_dia * dsr  # Calcula o desconto do DSR

    total = desconto_faltas + desconto_dsr  # Soma os dois descontos

    return total  # Retorna o total de desconto por faltas + DSR


# -------------------------------------------------------
# Salário Final
# Subtrai todos os descontos do salário bruto
# -------------------------------------------------------
def calculo_salario(salario, vt, inss, irrf, faltas):
    return salario - vt - inss - irrf - faltas  # Salário bruto menos todos os descontos


# -------------------------------------------------------
# Salário por Horas Trabalhadas
# Calcula o salário proporcional às horas trabalhadas no mês
# -------------------------------------------------------
def calcular_salario_por_hora(salario, horas_trabalhadas):
    valor_hora = salario / 220  # Divide o salário por 220 (horas mensais padrão CLT)
    return valor_hora * horas_trabalhadas  # Multiplica pelo total de horas trabalhadas
