nome= (input("para começar,digite seu nome:"))
print("ola, seja bem vindo", nome, ". aqui iremos calcular a sua média trimestral das avaliações")
print("digite abaixo as suas últimas notas (apenas número e ponto)")
mes_1= float(input("mes 1:"))
mes_2= float(input("mes 2:"))
mes_3= float(input("mes 3:"))


media = (mes_1 + mes_2 + mes_3) / 3
print("sua media é:", media )
