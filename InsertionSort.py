import random

#Alustetaan random numerolla 1:
random.seed(1)

#Funktio randomisoidun listan luontiin:
def listanLuonti(ListanPituus):
    #i = i + 1
    RandomizedList = []
    for i in range(ListanPituus):
        n = random.randint(1, 100)
        RandomizedList.append(n)
    return RandomizedList

#Proseduuri listan lajitteluun:
def insertionSort(LajiteltavaLista):
    for i in range(1, len(LajiteltavaLista)):
        x = i
        while LajiteltavaLista[x-1] > LajiteltavaLista[x] and x > 0:
            LajiteltavaLista[x-1], LajiteltavaLista[x] = LajiteltavaLista[x], LajiteltavaLista[x-1]
            x = x - 1
  
  
#Luodaan lajiteltava lista, jonka pituus on 15 numeroa:            
LajiteltavaLista = listanLuonti(15)
#Tulostetaan lajittelematon lista:
print("Lajittelematon lista: ")
print(LajiteltavaLista)
print("")

#Lajitellaan ja tulostetaan lista:
insertionSort(LajiteltavaLista)
print("Lajiteltu lista: ")
print(LajiteltavaLista)
