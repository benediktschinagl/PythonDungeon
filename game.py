# Dungeon Spiel Benedikt
dungeon="..s..€..w.....€...B...w..€..w....w..B..s..€.....w....w..€...s.....w..€..w...Ä..€..s..E"
import random
ende="E" 
hero_hunger=0
hero="@"
hero_gold=0
food=0
herox=0
level=list(dungeon)
eg=("Mhmm!","Das tat gut!","Mehr davon!","Fressi Fressi!","Danke dafür!")
gg=("Money,Money,Money!","Gleich bin ich reich!","Bar auf die Kralle")
rg=("Heute ist aber ein schöner Tag!","Viel Sonne gibt es hier aber nicht")
while hero_hunger<10:
    hero_hunger+=random.choice((0,0,0,0,0,0,0,0,0,0,0,0,1,1,1,1,1,1,2))
    for x,c in enumerate(level):
        if x==herox:
            print(hero,end="")
        else:
            print(c,end="")
    print()
    command=input("gold:{} food:{} hunger:{} Was willst du nun tun?".format(hero_gold,food,hero_hunger))
    
    if command=="a":
        herox-=1
    if command=="d":
        herox+=1
    if command=="e":
        if food <1 :
            print ("zu wenig")
        else:
            food -= 1
            hero_hunger -= random.randint(2,3) 
            print(random.choice(eg))
    # aufheben
    stuff=level[herox]
    if stuff=="€":
        hero_gold+=1
        level[herox]="."
        print(random.choice(gg))
    if stuff=="w":
        food+=1
        level[herox]="."
    if stuff=="s":
        food+=5
        level[herox]="."
        print(random.choice(rg))
    if stuff=="E":
       break

print("Game Over!")
        
        
        
            

