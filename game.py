# Dungeon Spiel Benedikt
dungeon="..s...G.....€...G...w..€..KKK.G..s..€....w..€..G.s....w.G..€...KK...G..€..s..Ä.p"
import random
import subprocess
princess=False
ende="E" 
hp=200
hero_hunger=0
hero="@"
hero_gold=0
food=0
herox=0
level=list(dungeon)
eg=("Mhmm!","Das tat gut!","Mehr davon!","Fressi Fressi!","Danke dafür!")
gg=("Money,Money,Money!","Gleich bin ich reich!","Bar auf die Kralle")
rg=("Heute ist aber ein schöner Tag!","Viel Sonne gibt es hier aber nicht")
while hero_hunger<15:
    hero_hunger+=random.choice((0,0,0,0,0,0,0,0,0,0,0
    ,1,1,1,1,1,1,2))
    for x,c in enumerate(level):
        if x==herox:
            print(hero,end="")
        else:
            print(c,end="")
    print()
    command=input("gold:{} food:{} hunger:{} hp:{} Was willst du nun tun?".format(hero_gold,food,hero_hunger,hp))
    dx=0 
    if command=="a":
       # herox-=1
       dx=-1
    if command=="d":
        #herox+=1
        dx=1
    if command=="e":
        if food <1 :
            print ("Zu wenig Essen!")
        else:
            food -= 1
            hero_hunger -= random.randint(2,3) 
            print(random.choice(eg))
    if command=="cheat":
        hp+=100
        subprocess.call(("espeak","Cheater"))
    # in Monster gelaufen?
    target=level[herox+dx]
    #------Endboss-Anfang-------
    if target=="Ä":
        print ("Der Endboss ist erschienen!")
        print ("Er greift dich mit einem Baumstamm an!")
        schaden=random.randint(5,15)
        hp -=schaden
        print ("Du erleidest {} schaden".format(schaden))
        if hp < 1:
            print ("Du stirbst! Versager! Probier es gleich nochmal!")
            break
        sieg=0.3333
        if random.random() < sieg:
            print ("Du erledigst den Boss und darfst weiter!")
            level[herox+dx]="."
        else:
            print ("Du verlierst!")
            dx=0
    #-------Endboss-Anfang------
    #-------Kobold-Anfang------
    if target=="K":
        print ("Eine Koboldhorde blockiert deinen Weg")
        print ("Der Kobold schlägt dich mit einem Knüppel")
        schaden=random.randint(1,10)
        hp -=schaden
        print ("Du erleidest {} schaden".format(schaden))
        if hp < 1:
            print ("Du stirbst! Versager! Das war doch nur ein Kobold!")
            break
        sieg=0.6
        if random.random() < sieg:
            print ("Du erledigst den Kobold mit Gewalt")
            level[herox+dx]="."
        else:
            print ("Du verlierst!")
            dx=0
    #-------Kobold-Ende--------
    #-------Gorilla-Anfang-------
    if target=="G":
        print ("Ein Gorilla blockiert deinen Weg")
        print ("Der Gorilla schlägt dich mit einer Banane")
        schaden=random.randint(1,10)
        hp -=schaden
        print ("Du erleidest {} schaden".format(schaden))
        if hp < 1:
            print ("Du stirbst! Versager!")
            break
        sieg=0.455555
        if random.random() < sieg:
            print ("Du erledigst heldenhaft den Gorilla")
            level[herox+dx]="."
        else:
            print ("Du verlierst!")
            dx=0
    #------Gorilla-Ende------
    herox+=dx
    # aufheben
    stuff=level[herox]
    if stuff=="€":
        hero_gold+=1
        level[herox]="."
        print(random.choice(gg))
    if stuff=="w":
        food+=2
        level[herox]="."
    if stuff=="s":
        food+=3
        level[herox]="."
        print(random.choice(rg))
    if stuff=="p":
        subprocess.call(("espeak","Congratulation you have saved the princess!"))
        princess=True
        break
 
 
 
 #-----Spiel vorbei-----
if princess:
        subprocess.call(("espeak","You have safed the day!"))
else:
    
    print("Game Over!")
    subprocess.call(("espeak","Game Over!"))
        
        
            

