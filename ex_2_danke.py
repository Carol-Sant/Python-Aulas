def verifica_maioridade():
    idade:int = int(input("Insira a idade: "))
    if idade < 16:
        print("MENOR")
    elif idade > 16 and idade < 18:
        print("EMANCIPADO")
    else:
        print("MAIOR")

def verifica_categoria():
    idade:int = int(input("Insira a idade: "))
    
    if(idade >= 5 and idade <= 7):
        print("Infantil A")
    elif(idade >= 8 and idade <= 10):
        print("Infantil B")
    elif(idade >= 11 and idade <= 13):
        print("Juvenil A")
    elif(idade >= 14 and idade <= 17):
        print("Juvenil B")


