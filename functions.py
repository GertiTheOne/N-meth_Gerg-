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
    for i in range(0,len(iranyitok)):
        print(f'\t{i+1}. {(iranyitok[i])}: {yardok[i]} m')
    input('Tovább...')

def ujIranyito():
    system('cls')
    print('-----ÚJ IRÁNYÍTÓ-----')
    ujIranyito=input('Név: ')
    ujYard=float(input('Passzolt Yardok száma: '))
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
    iranyitoKiir()
    sSz=int(input('Törlendő irányító sorszáma: '))
    iranyitok.pop(sSz-1)
    yardok.pop(sSz-1)
    mentesFajlba()
    input('Sikeres törlés.')

def mentesFajlba():
    file=open('Irányító','w',encoding='utf-8')
    for i in range(len(iranyitok)):
        file.write(f'{iranyitok[i]};{yardok[i]}')
        if i<len(iranyitok)-1:
            file.write('\n')
    file.close()
    
def ujAdat():
    system('cls')
    print('-----ÚJ ADAT-----')
    ujIranyito=input('Név: ')
    ujYard=float(input('Új Adat: '))
    if ujIranyito in iranyitok:
        i = 0
        while ujIranyito != iranyitok[i]:
            i+=1
        yardok[i]+=ujYard
    else:
        iranyitok.append(ujIranyito)
        yardok.append(ujYard)
    
    f = open("Irányító.csv","w",encoding="utf-8")
    f.write(f"Irányító;passzolt yardok\n")
    for i in range(len(iranyitok)):
        f.write(f"\n{iranyitok[i]};{yardok[i]}")
        
    f.close()
    input('Sikeres felvétel.')

def legtobbYard():
    print('----LEGTÖBB YARD----')
    max=0
    maxindex=0
    for i in range(len(yardok)):
        if yardok[i]>max:
            max=yardok[i]
            maxindex=i
    print(f'A legtöbb passzolt yard {max} {iranyitok[maxindex]} által')
    input('Tovább...')

def legkevesebbYard():
    print('----LEGKEVESEBB YARD----')
    min=99999
    minindex=0
    for i in range(len(yardok)):
        if yardok[i]<min:
            min=yardok[i]
            minindex=i
    print(f'A legkevesebb passzolt yard {min} {iranyitok[minindex]} által')
    input('Tovább...')