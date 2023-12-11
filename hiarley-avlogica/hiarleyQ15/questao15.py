# 15 - EXERCICIO OBRIGATORIO PARA TODOS:Imagine que você está planejando uma viagem de carro e gostaria de calcular o
# quanto de combustível você irá gastar e quanto isso vai custar. O objetivo deste
# exercício é criar um programa que peça ao usuário para inserir:
# 1. A distância total da viagem em quilômetros.
# 2. O consumo médio de combustível do carro (km por litro).
# 3. O preço do combustível por litro.
# O programa deve calcular e exibir:
# • A quantidade estimada de combustível necessária para a viagem.
# • O custo total do combustível.
# Para adicionar mais contexto e desafio ao exercício, considere as seguintes
# variações de preço para o combustível dependendo da região:
# • Região Norte: R$ 5,30 por litro
# • Região Nordeste: R$ 5,10 por litro
# • Região Centro oeste: R$ 5,20 por litro
# • Região Sudeste: R$ 5,00 por litro
# • Região Sul: R$ 5,15 por litro
# O usuário deve inserir a região para que o programa calcule o preço com base
# nos valores acima.
# Exemplo de como o programa deve funcionar:
# Digite a distância total da viagem em km: 300
# Digite o consumo médio de combustível do carro (km por litro): 10
# Digite a região para cálculo do preço do combustível (Norte, Nordeste, CentroOeste, Sudeste, Sul): Sudeste
# Você precisará de 30 litros de combustível.
# # O custo total do combustível será de R$150,00 para a região Sudeste.

n = 5.30
c = 5.10 
o = 5.20 
s = 5.00
u = 5.15

distancia= float(input("digite o total de kms da sua viangem:"))
consumo= float(input("digite o consumo do seu carro de KM por litro:"))

preco= str(input("""digite sua regiao, sendo:
                 norte = N
                 nordeste = C
                 centro oeste = O
                 sudeste = S
                 sul = u
                 :"""))

quantidadeestimada = distancia/consumo
print("a quantidade estimada de combustivel necessario e", quantidadeestimada, "L")

if preco == n:
   print("o custo total do combustivel é", (quantidadeestimada*n))
elif preco == c:
   print("o custo total do combustivel é", (quantidadeestimada*c))
elif preco == o:
   print("o custo total do combustivel é", (quantidadeestimada*o))
elif preco == s:
   print("o custo total do combustivel é", (quantidadeestimada*s))
else:
   print("o custo total do combustivel é", (quantidadeestimada*u))

   
