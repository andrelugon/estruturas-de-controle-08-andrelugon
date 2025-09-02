# Programa que lê a altura (em metros) e o sexo ("M" ou "F") e calcula o peso ideal.

# Dados de entrada: o usuário informa altura e sexo:
altura = float(input("Digite a altura em metros: "))
sexo = input("Digite o sexo (M ou F): ")

# para homens: (72.7*altura)-58
# para mulheres: (62.1*altura)-44.7

# Estrutura condicional: se o sexo for exatamente "M", aplica a fórmula masculina; caso contrário, feminina.
if sexo == "M":
    peso_ideal = (72.7 * altura) - 58
else :
    peso_ideal = (62.1 * altura) - 44.7

# Saída de dados: peso ideal com duas casas decimais  
print(f"{peso_ideal:.2f}")

