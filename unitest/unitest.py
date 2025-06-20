#1 - Crie uma função que calcule a área de um quadrado, de um retângulo e de um triângulo

#2 - Crie os testes de unidade para essas três funções que criou na questão 1

#3 - Altere um desses testes de unidade para que leia uma massa de teste a partir de uma lista de valores

#4 - Altere outro desses testes de unidade para que leia uma massa de teste a partir de um arquivo csv

def calcular_quadrado(lado):
    return lado ** 2

def calcular_retangulo(base, altura):
    return base * altura

def calcular_triangulo(base, altura):
    return (base * altura) / 2