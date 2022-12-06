from functions import *

fajlBeolvasas()

choice=''
while choice!='0':
    choice=menu()
    if choice=='1':
        iranyitoKiir()
    if choice=='2':
        ujIranyito()
    if choice=='3':
        iranyitoTorlese()
    if choice=='4':
        ujAdat()
    if choice=='5':
        legtobbYard()
    if choice=='6':
        legkevesebbYard()