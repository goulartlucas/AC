#1
def print_padrao(n):
  for i in range(1, n + 1):
      for j in range(1, i + 1):
          print(j, end=" ")
      print()

def main():
  num = int(input("Digite um número inteiro: "))
  print_padrao(num)

if __name__ == "__main__":
  main()


#2
def count_digits(number):
  num_str = str(number)
  num_of_digits = len(num_str)
  return num_of_digits

if __name__ == "__main__":
  user_input = int(input("Digite um número: "))
  digit_count = count_digits(user_input)
  print(f"O número {user_input} tem {digit_count} dígitos.")


#3
  try:
    num1 = int(input("Digite o primeiro número inteiro: "))
    num2 = int(input("Digite o segundo número inteiro: "))

    result = num1 / num2

  except ValueError:
    print("Erro: Os valores inseridos não são números válidos.")

  except ZeroDivisionError:
    print("Erro: Divisão por zero.")

  else:
    print(f"Resultado: {result}")

  finally:
    print("Concluído.")
