produto = float(250.50)
desconto = produto * (15 / 100)
# o codigo nao reconheceu o %, tive que fazer o
# calculo de 15/100 para conseguir a porcentagem
print(f"Valor do produto: R${produto}")
print(f"Voce esta economizando: R${desconto}")
produto = produto - desconto
print(f"Valor final do produto: R${produto}")
#aqui a sequencia de print usei a f string para puxar dados das strings acima

