# Digite um valor e veja quantos dolares voce poderá comprar: R$

print("conversor de real para dolar")
real = float(input("digite o valor em real a ser convertido:"))
cotacao_real_dolar = 5.0589
dolar = real / cotacao_real_dolar
print(f"dolar:{dolar}")
