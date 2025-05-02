import os 
os.system("clear")




def cl_inss():
    







def vale_transporte(valor):
    if vale_transporte == "s":
         vte_valor = salario * 0.6
         return vte_valor
    else:
        exit

def vale_refeicao():
         vale_rfcv = salario * 0.20
         return vale_rfcv
def cl_plano(dependentes):
     return dependentes * 150

def cl_irrf(salario, dependentes):
     deducao = 189.59 * dependentes
     base_calculo = salario - deducao
     if base_calculo <= 2259.20:
        return 0.0
     elif base_calculo >= 2259.21:
          return base_calculo * 0.075 - 169.44
     elif base_calculo >=  2826.66:
          return base_calculo * 0.15 - 381.44
     elif base_calculo >=  3751.06:
          return base_calculo * 0.25 - 662.77
     elif base_calculo >= 4664.68:
          return base_calculo * 0.27 - 896.00
          

matricula = int(input("Digite sua matricula: "))
senha = int(input("Digite sua senha: "))


salario = float(input("Qual seu salário bruto? "))

dependentes = str(input("Você possui dependentes?\n Responda com 's' ou 'n': ")).lower()

if dependentes == "s":
    quantidade_dependentes = int(input("Qunatos dependentes você possui? "))
else:
    exit

valor = str(input("Você deseja o benéfico do VTE? "))
vte_final = vale_transporte(valor)

valor_ref = int(input("Qual o valor do benefício do Vale Refeição? "))


desconto_plano = cl_plano(dependentes) 
desconto_vte = vale_transporte(valor)
desconto_ref = vale_refeicao()
total_descontos = desconto_plano + desconto_vte + desconto_ref


print()
print(f"Matrícula: {matricula}")
print(f"Senha: {senha}")
print(f"Vale transporte:{vte_final}")
print(f"Vale refeição")
print(f"Desconto do vale transporte: {desconto_vte}")
print(f"Total dos descontos: ")