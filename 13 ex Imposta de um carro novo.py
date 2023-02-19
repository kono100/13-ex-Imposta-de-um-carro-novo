

''' . O custo ao consumidor de um carro novo é a soma do custo de fábrica com a percentagem 
do distribuidor e dos impostos (aplicados ao custo de fábrica). Supondo que a percentagem 
do distribuidor seja de 28% e os impostos de 45%, faça um programa que leia o custo de 
fábrica de um carro e retorne o custo ao consumidor. '''


v_fabrica = float(input('Digite o valor base do carro: '))
impostos = v_fabrica + (v_fabrica * 0.45)
v_distribuidor = impostos + (impostos * 0.28)
print(f'O valor final do carro será de R${v_distribuidor:.2f}')
