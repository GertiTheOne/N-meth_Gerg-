from data import iranyitok,yardok
from os import system

filename='Irányító.csv'

def menu():
    system('cls')
    print('0 - Kilépés')
    print('1 - Irányítók listázása')
    print('2 - Új irányító felvétle')
    print('3 - Irányító törlése')
    print('4 - Meglévő irányító új adata')
    print('5 - Legtöbb yardot passzolt irányító')
    print('6 - Legkevesebb yardot passzolt irányító')
    return input('Kérem válasszon az alábbi menüpontok közül: ')

def fajlBeolvasas():
    file=open(filename,'r',encoding='utf-8')
    file.readline()
    for egysor in file:
        darabolt=egysor.strip().split(';')
        iranyitok.append(darabolt[0])
        yardok.append(float(darabolt[1]))
    file.close()

