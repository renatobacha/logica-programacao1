# logica-programacao
Curso de Lógica em Programação em Pyton EBAC

Olá, esse arquivo é relacionado a uma tarefa do curso de Analista de Dados da EBAC, referente à linguagem Python.

Segue o passo a passo para que você possa utiliza-lo da melhor maneira. 

Precisamos apenas dos dados num1 (50), num2(25), e a operação que desejamos fazer, que no caso, seria de multiplicação, com resultado de 1250.

Primeiro, é digitado o num1(50). Posteriormente, o num2(25), e é escolhida a operação que deseja realizar 3(multiplicação).

O robô vai analisar a escolha e vai mostrar em tela o valor final de 1250.

Segue abaixo o código completo.

CALCULADORA DO RENATINHO

print("Bem-vindo à Calculadora do Renatinho!")
     
Bem-vindo à Calculadora do Renatinho!

num1 = float(input("Digite o num1:"))
num2 = float(input("Digite o num2:"))
print("Escolha a operação que gostaria de fazer")
print("1 - Soma")
print("2 - Subtração")
print("3 - Multiplicação")
print("4 - Divisão")
escolha = input("Digite a operação:")
if escolha == "1":
  resultado = num1 + num2
  print(f"Resultado: {num1} + {num2} = {resultado}")
if escolha == "2":
  resultado = num1 - num2
  print(f"Resultado: {num1} - {num2} = {resultado}")
if escolha == "3":
  resultado = num1 * num2
  print(f"Resultado: {num1} * {num2} = {resultado}")
if escolha == "4":
  if num2 !=0:
    resultado = num1 / num2
    print(f"Resultado: {num1} * {num2} = {resultado}")
     
Digite o num1:50
Digite o num2:25
Escolha a operação que gostaria de fazer
1 - Soma
2 - Subtração
3 - Multiplicação
4 - Divisão
Digite a operação:3
Resultado: 50.0 * 25.0 = 1250.0
