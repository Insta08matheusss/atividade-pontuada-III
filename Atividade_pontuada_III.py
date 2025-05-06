import os
os.system("clear")

def calcular_inss(salario):
    if salario <= 1518.00:
        return salario * 0.075
    elif salario <= 2793.88:
        return salario * 0.09 - 113.85
    elif salario <= 4190.83:
        return salario * 0.12 - 189.54
    elif salario <= 8157.41:
        return salario * 0.14 - 318.38
    else:
        return 1142.04

def calcular_irrf(salario, dependentes):
    deducao = 189.59 * dependentes
    base_calculo = salario - deducao

    if base_calculo <= 2259.20:
        return 0.0
    elif base_calculo <= 2826.65:
        return base_calculo * 0.075 - 169.44
    elif base_calculo <= 3751.05:
        return base_calculo * 0.15 - 381.44
    elif base_calculo <= 4664.68:
        return base_calculo * 0.225 - 662.77
    else:
        return base_calculo * 0.275 - 896.00

def calcular_vale_transporte(salario):
       
    if vale_transporte == 's':
        return salario * 0.06 
    else:
        0.0
    

def calcular_vale_refeicao(valor_beneficio):
    return valor_beneficio * 0.20

def calcular_plano_saude(dependentes):
    return dependentes * 150.00


matricula = input("Digite sua matrícula: ")
senha = input("Digite sua senha: ")

salario = float(input("Qual seu salário base?: "))
dependentes = int(input("Quantos dependentes você possui?: "))
vale_transporte = input("Deseja receber vale transporte?\n Responda com 's' ou 'n': ").lower()
valor_vale_refeicao = float(input("Qual valor do vale refeição?: "))


dsc_inss = calcular_inss(salario)
dsc_irf = calcular_irrf(salario, dependentes)
dsc_vte = calcular_vale_transporte(salario, vale_transporte)
dsc_vr = calcular_vale_refeicao(valor_vale_refeicao)
dsc_saude = calcular_plano_saude(dependentes)

total_descontos = dsc_inss + dsc_irf + dsc_vte + dsc_vr + dsc_saude
salario_liquido = salario - total_descontos


print(f"Matrícula: {matricula}")
print(f"Salário Base: {salario:.2f}")
print(f"Desconto Iss: {dsc_inss:.2f}")
print(f"Desconto Irff: {dsc_irf:.2f}")
print(f"Desconto Vale Transporte: {dsc_vte:.2f}")
print(f"Desconto Vale Refeição: {dsc_vr:.2f}")
print(f"Desconto Plano de Saúde: {dsc_saude:.2f}")
print(f"Total de Descontos: {total_descontos:.2f}")
print(f"Salário Líquido: {salario_liquido:.2f}")