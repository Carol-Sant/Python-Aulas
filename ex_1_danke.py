import math


def calcula_area_retangulo():
    largura = int(input("Qual a largura do retangulo? "))
    altura = int(input("Qual a altura do retangulo? "))
    print("A area do retangulo eh igual a", largura * altura)


def calcula_area_quadrado():
    lado = int(input("Qual a medida do lado do quadrado? "))
    print("A area do quadrado eh igual a", lado**2)


def calcula_valor_desconto():
    valor_reais = int(input("Insira o valor do produto em reais "))
    desconto = int(input("Insira a porcentagem do desconto a ser aplicado "))
    print("O valor do produto com desconto eh", valor_reais - (valor_reais * (desconto / 100)))


def calcula_area_circulo():
    raio = float(input("Qual o raio do circulo? "))
    area = math.pi * (raio ** 2)
    print("A area do circulo eh", area)


def calcula_cotacao_BRL_to_USD():
    reais = float(input("Qual a quantia a ser convertida? "))
    cotacao_dolar = float(input("Qual a cotacao atual do dolar? "))
    valor_dolar = reais / cotacao_dolar

    print(f"{reais} com a cotacao de {cotacao_dolar} eh: {valor_dolar}")

