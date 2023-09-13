#Quetão 1:
def e_primo(num):
  for div in range(2, num):
    if num % div == 0:
      print(f"{num} não é primo, é divisível por {div}")
      
  
  else:
    print("O numero e primo")

e_primo(16)


#Questão 2:
def calcular_juros(valor_divida, parcelas):
    if parcelas == 1:
        return 0.0
    if parcelas == 3:
        return valor_divida * 0.10
    if parcelas == 6:
        return valor_divida * 0.15
    if parcelas == 9:
        return valor_divida * 0.20
    if parcelas == 12:
        return valor_divida * 0.25
    else:
        return None


def calcular_valor_total(valor_divida, juros):
    return valor_divida + juros

def mostrar_opcoes_parcelamento(valor_divida):
    print("Opções de Parcelamento:")

    print(f"Parcelas: 1 | Juros: R$ 0 | Total: R${valor_divida:} | Valor da Parcela: R${valor_divida}")
    
    for parcela in range(3,13,3):
      juros = calcular_juros(valor_divida, parcela)
      valor_total = calcular_valor_total(valor_divida, juros)
      valor_parcela = valor_total / parcela
      print(f"Parcelas: {parcela} | Juros: R${juros:} | Total: R${valor_total:} | Valor da Parcela: R${valor_parcela:}")
    
    
    

valor_divida = float(input("Digite o valor da dívida: "))


mostrar_opcoes_parcelamento(valor_divida)


#Questão 3:
intervalo_0_25 = 0 
intervalo_26_50 = 0 
intervalo_51_75 = 0 
intervalo_76_100 = 0 

while True:
  num = int(input("digite seu numero:"))

  if num < 0:
   break

  if 0 <= num < 25:
    intervalo_0_25 += 1
  elif 26 <= num < 50:
    intervalo_26_50 += 1
  elif 51 <= num < 75:
    intervalo_51_75 += 1
  elif 76 <= num < 100:
    intervalo_76_100 += 1

print("[0-25]", intervalo_0_25)
print("[26-50]", intervalo_26_50)
print("[51-75]", intervalo_51_75)
print("[76-100]", intervalo_76_100)


