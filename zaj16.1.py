#Napisz funkcję, która pobiera słowo w języku polskim
# a zwraca to samo słowo w dowolnym innym języku.
# Jeśli podane słowo nie jest znane programowi,
# funkcja powinna zwrócić pustego stringa. Program powinien wykorzystywać słowniki.
# Zaprezentuj działanie funkcji na trzech różnych stringach.

slownik1={"niebieski":"blue", "czerwony":"red"}
slownik2={"kot":"cat", "pies":"dog"}
slownik3={"jabłko":"apple", "gruszka":"pear"}
slownik4=[]

def slownik(slowo):
    definicja=slownik1[slowo]
 
    return definicja

haslo=input("Podaj hasło po polsku\n")
definicja=slownik(haslo)

if haslo in slownik1.keys():
    print("To słowo po angielsku brzmi:", definicja)
else:
    print(slownik4)

def slownik(slowo):
    definicja=slownik2[slowo]
 
    return definicja

haslo=input("Podaj hasło po polsku\n")
definicja=slownik(haslo)

if haslo in slownik2.keys():
    print("To słowo po angielsku brzmi:", definicja)
else:
    print(slownik4)

def slownik(slowo):
    definicja=slownik3[slowo]
 
    return definicja

haslo=input("Podaj hasło po polsku\n")
definicja=slownik(haslo)

if haslo in slownik3.keys():
    print("To słowo po angielsku brzmi:", definicja)
else:
    print(slownik4)
