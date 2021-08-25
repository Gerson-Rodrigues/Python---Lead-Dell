print('Vamos calcular seu IMC:')
nome = input('Qual seu nome? ')
peso = input('Qual o seu peso? ')
altura = input('Coloque sua altura: ')
idade = input('Diga sua idade: ')
peso_float = float(peso)
altura_float = float(altura)
altura_ao_quadrado = altura_float * altura_float
imc = peso_float/altura_ao_quadrado
imc_str = str(imc)
print(nome+' , com '+idade+' anos  de idade, o seu IMC foi de '+imc_str)
#print('{} com {}  anos, o seu IMC, foi de {:.2f}'.format(nome, idade, imc))

#a Ultima linha faria mais sentido, mas o exercicio proposto pede de
#forma mais iniciante, optei por seguir à risca o que pedia o enunciado
