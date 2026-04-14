peso = float(input("insira seu peso "))
altura = float(input("insira sua altura "))

IMC= peso/(altura*altura)

if IMC <= 18.5:
    print("abaixo do peso")
elif IMC >= 18.5 and IMC <= 24.9:
    print("Normal")
elif IMC >= 25 and IMC <= 29.9:
    print("Sobrepeso")
else:
    print("Obesidade")

print(f" Sua classificação - {IMC}")
print(f"Sua altura é {altura}")