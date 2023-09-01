#Questao 1:
def calcular_salario(salario_por_hora, horas_trabalhadas_no_mes):
    return salario_por_hora * horas_trabalhadas_no_mes

salario_por_hora = float(input("Digite o salário por hora: "))
horas_trabalhadas_no_mes = float(input("Digite o número de horas trabalhadas no mês: "))

salario_total = calcular_salario(salario_por_hora, horas_trabalhadas_no_mes)
print(f"O salário a ser recebido é: R$ {salario_total:.2f}")

#Questao 2:
def calcular_e_exibir_resultados(num1, num2, num3):
    resultado1 = (2 * num1) * (num2 / 2)
    resultado2 = (3 * num1) + num3
    resultado3 = num3 ** 3

    print(f"Resultado 1: O produto do dobro do primeiro com metade do segundo é {resultado1}")
    print(f"Resultado 2: A soma do triplo do primeiro com o terceiro é {resultado2}")
    print(f"Resultado 3: O terceiro elevado ao cubo é {resultado3}")

num1 = float(input("Digite o primeiro número: "))
num2 = float(input("Digite o segundo número: "))
num3 = float(input("Digite o terceiro número: "))

calcular_e_exibir_resultados(num1, num2, num3)

#Questao 3:
def calcular_resultados(num1, num2, num3):
    resultado1 = (2 * num1) * (num2 / 2)
    resultado2 = (3 * num1) + num3
    resultado3 = num3 ** 3

    return resultado1, resultado2, resultado3

num1 = float(input("Digite o primeiro número: "))
num2 = float(input("Digite o segundo número: "))
num3 = float(input("Digite o terceiro número: "))

resultado1, resultado2, resultado3 = calcular_resultados(num1, num2, num3)

print(f"Resultado 1: O produto do dobro do primeiro com metade do segundo é {resultado1}")
print(f"Resultado 2: A soma do triplo do primeiro com o terceiro é {resultado2}")
print(f"Resultado 3: O terceiro elevado ao cubo é {resultado3}")

#Questao 4:
def eh_bissexto(ano):
    return (ano % 4 == 0 and ano % 100 != 0) or (ano % 400 == 0)

# Exemplo de uso da função
ano = int(input("Digite um ano: "))

resultado = eh_bissexto(ano)

print(f"{ano} é um ano bissexto: {resultado}")








