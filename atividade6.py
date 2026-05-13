# Exercício 1:
n1 = int(input("digite o primeiro número: "))
n2 = int(input("Digite o segundo número :"))

if n1 > n2:
    print(n1)
else:
    print("O maior número é: ", n2)    

# Exercício 2:
n1 = int(input("Digite o primeiro valor (em números): "))
if n1 < 0:
    print("Esse valor é negativo.")
else:
    print("Esse valor é positivo.")

# Exercício 3: 
letra = input("Digite F ou M: ")

if letra == "F":
    print("Feminino")

elif letra == "M":
    print("Masculino")

else:
    print("Sexo inválido")   

# Exercício 4:
letra = input("Digite uma letra: ").lower()

if letra in "aeiou":
    print("É uma vogal")
else:
    print("É uma consoante")

# Exercício 5:
nota1 = float(input("Digite a primeira nota: "))
nota2 = float(input("Digite a segunda nota: "))

media = (nota1 + nota2) / 2

if media == 10:
    print("Aprovado com Distinção")

elif media >= 7:
    print("Aprovado")

else:
    print("Reprovado")

# Exercício 6:
num1 = float(input("Digite o primeiro número: "))
num2 = float(input("Digite o segundo número: "))
num3 = float(input("Digite o terceiro número: "))

# Maior número
if num1 > num2 and num1 > num3:
    maior = num1

elif num2 > num1 and num2 > num3:
    maior = num2

else: 
    maior = num3 

# Menor número
if num1 < num2 and num1 < num3:
    menor = num1
elif num2 < num1 and num2 < num3:
    menor = num2
else:
    menor = num3

print(f"O maior número é: {maior}")
print(f"O menor número é: {menor}")

# Exercício 7:
letra = input("Digite uma letra: ").lower()

if letra in "aeiou":
    print("É uma vogal")
else:
    print("É uma consoante")

# Exercício 8: 
produto1 = float(input("Digite o preço do primeiro produto: "))
produto2 = float(input("Digite o preço do segundo produto: "))
produto3 = float(input("Digite o preço do terceiro produto: "))

if produto1 < produto2 and produto1 < produto3:
    print("Você deve comprar o primeiro produto.")
elif produto2 < produto1 and produto2 < produto3:
    print("Você deve comprar o segundo produto.")
else:
    print("Você deve comprar o terceiro produto.")

#Exercício 9: 
num1 = int(input("Digite o primeiro número: "))
num2 = int(input("Digite o segundo número: "))
num3 = int(input("Digite o terceiro número: "))

lista = [num1, num2, num3]

lista.sort(reverse=True)

print("Números em ordem decrescente:")
print(lista)  

# Exercício 10: 
turno = input("Digite o turno que você estuda (M/V/N): ").upper()

if turno == "M":
    print("Bom Dia!")
elif turno == "V":
    print("Boa Tarde!")
elif turno == "N":
    print("Boa Noite!")
else:
    print("Valor Inválido!")

# Exercício 11:
salario = float(input("Digite o salário: R$ "))

if salario <= 280:
    percentual = 20

elif salario <= 700:
    percentual = 15

elif salario <= 1500:
    percentual = 10

else:
    percentual = 5

aumento = salario * percentual / 100

novo_salario = salario + aumento

print("Salário antes do reajuste: R$", salario)
print("Percentual aplicado:", percentual, "%")
print("Valor do aumento: R$", aumento)
print("Novo salário: R$", novo_salario)

# Atividade 12: 
valor_hora = float(input("Digite o valor da hora: "))
horas_trabalhadas = float(input("Digite as horas trabalhadas no mês: "))

salario_bruto = valor_hora * horas_trabalhadas

# Verificando o IR
if salario_bruto <= 900:
    percentual_ir = 0

elif salario_bruto <= 1500:
    percentual_ir = 5

elif salario_bruto <= 2500:
    percentual_ir = 10

else:
    percentual_ir = 20

# Cálculos
ir = salario_bruto * percentual_ir / 100

inss = salario_bruto * 10 / 100

fgts = salario_bruto * 11 / 100

total_descontos = ir + inss

salario_liquido = salario_bruto - total_descontos

# Mostrando resultados
print("Salário Bruto: (", valor_hora, "*", horas_trabalhadas, ") : R$", salario_bruto)

print("(-) IR (", percentual_ir, "%) : R$", ir)

print("(-) INSS (10%) : R$", inss)

print("FGTS (11%) : R$", fgts)

print("Total de descontos : R$", total_descontos)

print("Salário Líquido : R$", salario_liquido)

# Exercício 13:
dia = int(input("Digite um número de 1 a 7: "))

if dia == 1:
    print("Domingo")

elif dia == 2:
    print("Segunda-feira")

elif dia == 3:
    print("Terça-feira")

elif dia == 4:
    print("Quarta-feira")

elif dia == 5:
    print("Quinta-feira")

elif dia == 6:
    print("Sexta-feira")

elif dia == 7:
    print("Sábado")

else:
    print("Valor inválido")

# Exercício 14:
nota1 = float(input("Digite a primeira nota: "))
nota2 = float(input("Digite a segunda nota: "))

media = (nota1 + nota2) / 2

if media >= 9 and media <= 10:
    conceito = "A"

elif media >= 7.5 and media < 9:
    conceito = "B"

elif media >= 6 and media < 7.5:
    conceito = "C"

elif media >= 4 and media < 6:
    conceito = "D"

else:
    conceito = "E"

print("Média:", media)
print("Conceito:", conceito)
   
# Exercício 15:
nota1 = float(input("Digite a primeira nota: "))
nota2 = float(input("Digite a segunda nota: "))

media = (nota1 + nota2) / 2

if media >= 9 and media <= 10:
    conceito = "A"

elif media >= 7.5 and media < 9:
    conceito = "B"

elif media >= 6 and media < 7.5:
    conceito = "C"

elif media >= 4 and media < 6:
    conceito = "D"

else:
    conceito = "E"

print("Média:", media)
print("Conceito:", conceito)   

# Exercício 16:
lado1 = float(input("Digite o primeiro lado: "))
lado2 = float(input("Digite o segundo lado: "))
lado3 = float(input("Digite o terceiro lado: "))

# Verificando se pode formar um triângulo
if lado1 + lado2 > lado3 and lado1 + lado3 > lado2 and lado2 + lado3 > lado1:

    print("Os valores podem formar um triângulo.")

    # Verificando o tipo
    if lado1 == lado2 and lado2 == lado3:
        print("Triângulo Equilátero")

    elif lado1 == lado2 or lado1 == lado3 or lado2 == lado3:
        print("Triângulo Isósceles")

    else:
        print("Triângulo Escaleno")

else:
    print("Os valores NÃO podem formar um triângulo.")

# Exercício 17:
ano = int(input("Digite um ano: "))

if (ano % 4 == 0 and ano % 100 != 0) or (ano % 400 == 0):
    print("O ano é bissexto")
else:
    print("O ano NÃO é bissexto")

# Atividade 18:
data = input("Digite uma data (dd/mm/aaaa): ")

dia, mes, ano = data.split("/")

dia = int(dia)
mes = int(mes)
ano = int(ano)

data_valida = True

# Verificando mês
if mes < 1 or mes > 12:
    data_valida = False

# Verificando dia
elif dia < 1 or dia > 31:
    data_valida = False

# Meses com 30 dias
elif mes in [4, 6, 9, 11] and dia > 30:
    data_valida = False

# Fevereiro
elif mes == 2:

    # Ano bissexto
    if (ano % 4 == 0 and ano % 100 != 0) or (ano % 400 == 0):

        if dia > 29:
            data_valida = False

    else:
        if dia > 28:
            data_valida = False

# Resultado
if data_valida:
    print("Data válida")
else:
    print("Data inválida")

# Exercício 19:
numero = int(input("Digite um número menor que 1000: "))

centena = numero // 100

dezena = (numero % 100) // 10

unidade = numero % 10

print(numero, "=")

if centena > 0:
    print(centena, "centena(s)")

if dezena > 0:
    print(dezena, "dezena(s)")

if unidade > 0:
    print(unidade, "unidade(s)")

# Exercício 20:
nota1 = float(input("Digite a primeira nota: "))
nota2 = float(input("Digite a segunda nota: "))
nota3 = float(input("Digite a terceira nota: "))

media = (nota1 + nota2 + nota3) / 3

if media == 10:
    print("Aprovado com Distinção")
    print("Média:", media)

elif media >= 7:
    print("Aprovado")
    print("Média:", media)

else:
    print("Reprovado")
    print("Média:", media)