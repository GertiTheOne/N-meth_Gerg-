from data import iranyitok,yardok
from os import system

filename='Irányító.csv'

def menu():
    system('cls')
    print('----MENÜ----')
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

def iranyitoKiir():
    system('cls')
    print('----IRÁNYÍTÓK----')
    for iranyito in iranyitok:
        print(f'\t{iranyito}')
    input('Tovább...')

def ujIranyito():
    system('cls')
    print('-----ÚJ IRÁNYÍTÓ-----')
    ujIranyito=input('Név: ')
    ujYard=float(input('\tPasszolt Yardok száma: '))
    iranyitok.append(ujIranyito)
    yardok.append(ujYard)
    mentesFajlVegere(ujIranyito,ujYard)
    input('Sikeres felvétel.')

def mentesFajlVegere(iranyito,yard):
    file=open('Irányító.csv','a',encoding='utf-8')
    file.write(f'\n{iranyito};{yard}')
    file.close() 

def iranyitoTorlese():
    system('cls')
    print('----IRÁNYÍTÓ TÖRLÉSE----\n')
    
    mentesFajlba()
    input('Sikeres törlés.')

def mentesFajlba():
    file=open('Irányító','w',encoding='utf-8')
    for i in range(len(iranyitok)):
        file.write(f'{iranyitok[i]};{yardok[i]}')
        if i<len(iranyitok)-1:
            file.write('\n')
    file.close()