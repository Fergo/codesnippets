from fractions import *
import math
import random

def maximoDivisorComum(maior : int, menor: int):
    while (menor != 0):
        temp = menor
        menor = maior % menor
        maior = temp

    return maior

def geraPrimos(de : int, ate: int):
    lista = []
    for num in range(de, ate + 1):
        if num > 1:
            for i in range(2, num):
                if (num % i) == 0:
                    break
            else:
                lista.append(num)

    return lista

def geraCoprimos(valor: int):
    lista = []
    for i in range(2,101):
        if maximoDivisorComum(valor, i) == 1:
            lista.append(i)

    return lista

def criptografa(msg : str, E : int, N : int):
    msgBytes = bytearray(msg.encode())
    cripto = []

    for char in msgBytes:
        cripto.append((char ^ E) % N)
    
    return cripto

def descriptografa(msgCripto : list, D : int, N : int):
    decripto = []

    for char in msgCripto:
        decripto.append((char ^ D) % N)
    
    return decripto.decode("ascii")

# Escolhe dois numeros primos quaisquer
P = random.choice(geraPrimos(2, 50))
Q = random.choice(geraPrimos(2, 50))

# Calcula os parametros
N = P * Q
Z = (P - 1) * (Q - 1)

# Escolhe um coprimo aleatorio de Z
D = geraCoprimos(Z)[0]

# Encontra (E * D) mod Z = 1
valorInicial = 0
E = 1
while (E * D) % Z != 1:
    E = E + 1
    
public_key = (E, N)
private_key = (D, N)

msg = "Meu nome é Teste"

cript = criptografa(msg, E, N)
decript = descriptografa(cript, D, N)


print(P)
print(Q)
