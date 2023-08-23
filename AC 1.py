#Questão 1:

a = float(input("digite seu número"))
b = float(input("digite seu número"))
c = float(input("digite seu número"))

d = (b**2 - 4*a*c)
x1 = (-b + d**(1/2)) / (2*a)
x2 = (-b - d**(1/2)) / (2*a)

print("x1", x1,)
print("x2", x2,)


#Questão 2:

ano = int(input("digite seu ano escolhido:"))
bissexto = (ano % 4 == 0 and ano % 100 != 0) or (ano % 400 == 0)
print(bissexto and f"{ano} é um ano bissexto" or f"{ano} não é um ano bissexto")


