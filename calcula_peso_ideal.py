# Sua solução aqui
altura = float(input("Digite a altura em metros: "))
sexo = input("Digite o sexo (M ou F): ")

# para homens: (72.7*altura)-58
# para mulheres: (62.1*altura)-44.7

if sexo == "M":
    peso_ideal = (72.7 * altura) - 58

else :
    peso_ideal = (62.1 * altura) - 44.7

print(f"{peso_ideal:.2f}")

