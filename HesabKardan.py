#Programmer : MrDaRkFoRcE
#Telegram : @ThE_DaRkFoRcE

import random
enterhesab = int(input("1.Jam\n2.Menha\n3.Zarb\n4.Taqsim\nEnter : "))

#----------------------------------------------------------------------#

def Easy():
    easy1 = random.randint(9,999)
    easy2 = random.randint(9,999)
    if enterhesab == 1:
        javab = easy1+easy2
        user = int(input("{} + {} = ".format(easy1,easy2)))
    elif enterhesab == 2:
        javab = easy1-easy2
        user = int(input("{} - {} = ".format(easy1,easy2)))
    elif enterhesab == 3:
        javab = easy1*easy2
        user = int(input("{} * {} = ".format(easy1,easy2)))
    elif enterhesab == 4:
        javab = easy1/easy2
        user = int(input("{} / {} = ".format(easy1,easy2)))
    else :
        print("Vorodi Na Motabar Ast ! ")
    if user == javab:
        print("Javab Dorost Bod ! \n")
    else :
        print("Javab Qalat Bod !\nJavab Dorost : {}\n".format(javab))

#-----------------------------------------------------------------------#

def Medium():
    medium1 = random.randint(99,9999)
    medium2 = random.randint(99,9999)
    if enterhesab == 1:
        javab = medium1+medium2
        user = int(input("{} + {} = ".format(medium1,medium2)))
    elif enterhesab == 2:
        javab = medium1-medium2
        user = int(input("{} - {} = ".format(medium1,medium2)))
    elif enterhesab == 3:
        javab = medium1*medium2
        user = int(input("{} * {} = ".format(medium1,medium2)))
    elif enterhesab == 4:
        javab = medium1/medium2
        user = int(input("{} / {} = ".format(medium1,medium2)))
    else :
        print("Vorodi Na Motabar Ast ! ")
    if user == javab:
        print("Javab Dorost Bod ! \n")
    else :
        print("Javab Qalat Bod !\nJavab Dorost : {}\n".format(javab))

#-----------------------------------------------------------------------#

def Hard():
    hard1 = random.randint(999,99999)
    hard2 = random.randint(999,99999)
    if enterhesab == 1:
        javab = hard1+hard2
        user = int(input("{} + {} = ".format(hard1,hard2)))
    elif enterhesab == 2:
        javab = hard1-hard2
        user = int(input("{} - {} = ".format(hard1,hard2)))
    elif enterhesab == 3:
        javab = hard1*hard2
        user = int(input("{} * {} = ".format(hard1,hard2)))
    elif enterhesab == 4:
        javab = hard1/hard2
        user = int(input("{} / {} = ".format(hard1,hard2)))
    else :
        print("Vorodi Na Motabar Ast ! ")
    if user == javab:
        print("Javab Dorost Bod ! \n")
    else :
        print("Javab Qalat Bod !\nJavab Dorost : {}\n".format(javab))

#-----------------------------------------------------------------------#

entergame = int(input("1.Easy\n2.Medium\n3.Hard\nEnter : "))

if (entergame == 1):
    Easy()
elif (entergame == 2):
    Medium()
elif (entergame == 3):
    Hard()
else :
    print("Vorodi Na Motabar Ast !")