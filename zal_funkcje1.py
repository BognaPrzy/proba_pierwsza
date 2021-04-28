#zadanie 5
def zamiana(lancuch):
    wynik = lancuch[-1] + lancuch[1:len(lancuch)-1] + lancuch[0]
    return wynik

slowo1 = "Kognitywistyka"
rezultat1 = zamiana(slowo1)
print(rezultat1)

slowo2 = "Samolot"
rezultat2 = zamiana(slowo2)
print(rezultat2)

slowo3 = "Radek"
rezultat3 = zamiana(slowo3)
print(rezultat3)


#zadanie 1
'''import random

def najwiekszy(lista):
    maksymalny = 0
    for i in range(len(lista)):
        for j in range(len(lista[i])):
            if lista[i][j] > maksymalny:
                maksymalny = lista[i][j]
    return maksymalny

duza_lista = []
for i in range(4):
    lista = []
    for j in range(5):
        wylosowana = random.randint(1,10000)
        lista.append(wylosowana)
    duza_lista.append(lista)

print(duza_lista)
rezultat = najwiekszy(duza_lista)
print("Największy element listy to:",rezultat)'''

#zadanie 3
'''def slownik(lista):
    print("Podaj słowo, którego chcesz uzyskać definicję:")
    haslo = input()
    if haslo in lista:
        wynik = lista[haslo]
    else:
        wynik = "   "
    return wynik

moj_slownik1 = {"jeden":"one","krzeslo":"chair","pomarancza":"orange"}
print(moj_slownik1)
rezultat = slownik(moj_slownik1)
print(rezultat)

moj_slownik2 = {"noga":"leg","ucho":"ear","wieloryb":"whale"}
print(moj_slownik2)
rezultat = slownik(moj_slownik2)
print(rezultat)

moj_slownik3 = {"siedem":"seven","samolot":"plane","szklanka":"glass"}
print(moj_slownik3)
rezultat = slownik(moj_slownik3)
print(rezultat)'''

'''import random
def tworzenie(wiersz,kolumna):
    duza_lista = []
    for i in range(kolumna):
        lista = []
        for i in range(wiersz):
            los = random.randint(1,100)
            lista.append(los)
        duza_lista.append(lista)
    return duza_lista

print("Ile wierszy ma mieć lista?")
wiersz1 = int(input())
print("Ile kolumn powinna mieć lista?")
kolumna1 = int(input())
rezultat1 = tworzenie(wiersz1,kolumna1)
print(rezultat1)

print("Ile wierszy ma mieć lista?")
wiersz2 = int(input())
print("Ile kolumn powinna mieć lista?")
kolumna2 = int(input())
rezultat2 = tworzenie(wiersz2,kolumna2)
print(rezultat2)

print("Ile wierszy ma mieć lista?")
wiersz3 = int(input())
print("Ile kolumn powinna mieć lista?")
kolumna3 = int(input())
rezultat3 = tworzenie(wiersz3,kolumna3)
print(rezultat3)'''
