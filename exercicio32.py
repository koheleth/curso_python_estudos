# -*- coding: utf-8 -*-

def numero_inteiro():
    try:
        numero = input("Digite um número inteiro: ")
        numero_int = int(numero)
        if numero_int % 2 == 0:
            print("O número é par")
        else:
            print("O número é ímpar")
    except ValueError:
    	print('Não foi digitado um número inteiro') 


def hora():
    try:
        pass
        hora = input("Digite a hora: ")
        hora_int = int(hora)
        minuto = input("Digite o minuto: ")
        if 0 <= hora_int <= 11:
            print("Bom dia")
        elif 12 <= hora_int <= 17:
            print("Boa tarde")
        elif 18 <= hora_int <= 23:
            print("Boa noite")
        else:
            print("Hora inválida")      
    except ValueError:
        print('Não foi digitado um número inteiro')
    

def tamanho_nome():
    nome = input("Digite seu nome: ")
    if len(nome) <= 4:
        print("Seu nome é curto")
    elif len(nome) in [5-6]:
        print("Seu nome é normal")
    else:
        print("Seu nome é muito grande")


def main():
    numero_inteiro()
    hora()
    tamanho_nome()


if __name__ == "__main__":
    main()
    