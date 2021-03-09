import random

print("*****Jogo da Advinhação*****\n")

numero_secreto = random.randrange(1, 101)
print(numero_secreto)
total_de_tentativas = 3
pontos = 1000

print("Qual o nível de dificuldade?")
print("(1) Fácil (2) Médio (3) Difícil")
nivel = int(input("Defina o nível: "))

if nivel == 1:
  total_de_tentativas = 20
elif nivel == 2:
  total_de_tentativas = 10
else:
  total_de_tentativas = 5

for rodada in range(1, total_de_tentativas + 1):
  print("Tentativa {} de {}".format(rodada, total_de_tentativas))
  chute = input("Digite um número entre 1 e 100: ")
  print("Você digitou o número", chute)
  chute = int(chute)

  if (chute < 1 or chute > 100):
    print("Você deve digitar um número entre 1 e 100!")
    continue

  if (chute == numero_secreto):
    print("Você acertou e fez {} pontos!".format(pontos))
    break
  else:
    if (chute > numero_secreto):
      print("Você errou! O seu chute foi maior que o número secreto.")
    elif (chute < numero_secreto):
      print("Você errou! O seu chute foi menor que o número secreto.")
    pontos_perdidos = abs(numero_secreto - chute)
    pontos = pontos - pontos_perdidos

print("Fim do programa!")
