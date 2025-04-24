import os
os.system ("clear")

salario_liquido = 0
salario_base = 0
trasporte = 0
total_descontos = 0
inss = 0 
irrf = 0 
desconto_vt = 0 
saude = 0 
vale_refeicao = 0
def desconto_inss(salario_base):
    if salario_base <= 1320.00:
        desconto = salario_base*0.075
        salario_base - desconto
    elif salario_base <= 2571.29:
        desconto = salario_base*0.09
        salario_base - desconto
    if salario_base <= 3856.94:
        desconto = salario_base*0.12
        salario_base - desconto
    elif salario_base <= 7507.49:
        desconto = salario_base*0.14
        salario_base - desconto
    else:
        desconto = 1051.05
    return desconto
    
def desconto_IRRF(salario_base):
        if salario_base == 2112.01 and salario_base <= 2826.65:
         desconto = salario_base*0.075
         salario_base - desconto
        elif salario_base <= 3544.00:
         desconto = salario_base*0.15
         salario_base - desconto
        if salario_base <= 4256.00:
         desconto = salario_base*0.225
         salario_base - desconto
        elif salario_base > 4256.00:
          desconto = salario_base*0.275
          salario_base - desconto
        return desconto


def desconto_saude(salario_base):
    
    if dependente == 1:
        ds_saude = salario_base - 150.00
    elif dependente == 2:
        ds_saude = salario_base - 300.00
    else:
       print ("Não solicitou dependente")    
    return 
     

if trasporte == "sim":
    desconto_vt = salario_base * 0.06
    salario_base - desconto_vt
else:
    print("Não optou por vale transporte.") 
    


print("~~~~DADOS DO FUNCIONARIO~~~~")    
matricula = input("\nDigite sua matricula: ")
senha = input("Digite sua senha: ")
salario_base = float(input("Digite o valor do seu salário: "))
refeicao = (input("Digite o valor do seu vale refeição: "))
trasporte = input("Deseja receber vale transporte? Sim | sim ou Não| não: ")
dependente = input("Solicita incluir dependente? não | Não ou sim | Sim , Quantos ? 1 ou 2 ? ")


inss = desconto_inss(salario_base)
irrf = desconto_IRRF(salario_base)
saude = desconto_saude(salario_base)
salario_liquido = (salario_base)
ds_saude = desconto_saude(salario_base)


total_descontos = inss + irrf + desconto_vt + ds_saude + vale_refeicao

salario_liquido = salario_base - total_descontos

print("\n~~~~FOLHA DE PAGAMENTO~~~~")
print(f"Desconto de INSS:{inss}")
print(f"Desconto de IRRF:{irrf}")
print(f"Desconto vale refeição: {refeicao}")
print(f"Desconto vale saúde: {ds_saude}")
print(f"Desconto vale trasnporte: {trasporte}")
print(f"Salário líquido: {salario_liquido}")







