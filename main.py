import os
n1 = int(input("Digite um número:"))
n2 = int(input("Digite um número:"))

os.system('clear')

if (n1 == n2):
  print("Os números são iguais")
elif(n1 != n2):
  if(n1 > n2):
    print("O primeiro número é maior")
  elif(n1 < n2):
    print("O segundo número é o maior")
  