# Dungeon Spiel Benedikt
dungeon1="""
################################################################
#...#........G.....€....w.....s..KK........G......w...K........#
#...#d######################################.............s.....#
#.€.#......€.#k....................w.......#...w....K........###
#...#..G.....######€...G..K....K...........G.........G..K#####.#
#.w.#....KK..G...k#.....................w..#.....K.........#€..#
#...#...s....######....K.....€..G.....K....#.K.......K.....#...#
#...#.K...G..#.........K...........w.......#K.....€....G...#...#
#.w.#.....KK.#................K............#.K....K......s.#.€.#
#.K.#######G########.....G........w...G...<#...G....w......#.€.#
#...#...........K..#d#######################...........K...#...#
#...#.w...K...G....#...w.........w........K#.G......KK.....#...#
#.G.#.......K.....s#......K.........K.......#....w...K.....#€..#
#...############G###...w.......KKK.........w.#...........#####.#
#...G....K.........#.......G....€....wK.......##################
#...#.......s....K.#.s..w......KKK.......w...€.......K...Ä.....#
#.s.#...K......€...#......K.........K...G...s...K........#..<..#
################################################################



"""
dungeon2=""" 
################################################################
#............w.....#......w......K........#..........€.........#
#.K......€.........G...€.........G........G.....K....w...K.....#
#.....G.......K....#........K........w....#........G.......K...#
####################....s.....G...K.......#.K...s...€######....#
#.......d.........k################################<##.#€#...w.#
#.......##########Ä#.......€...........K...G......###..#€#...K.#
#......##..........#..w.........K....#######...K.......#€#.G...#
#..<..##..K....K...#.......K.........#....>#.......K...#€#...€.#
#....##G......G....#..G........s...K.#.....#...........#€#..K..#
#...##.....€.....K.#......K..........#€€€€€#...K.......#€#.....#
#..##.....K........#..........G......#€€€€€#..G...K<...#€#..G..#
#.##..G.......K...##G#######################...........#€#..w..#
###.....K...€....#.....K.......K....G....s.#....K...G.#####....#
##...€..........#...€.....G...€........K..€#..€.......G......K.#
#........K......G.........K.......K......s.#....G...K.#...w.>.€#
################################################################
"""
dungeon3="""
################################################################
#......#......K...w.....K.........w.............s....w........€#
#......d....s..............K....###########..K....K......K.....#
#...K..#.K......w...K....€.....#.....s.....#........w.........K#
#..w..K#......K......K.....w..#.............#....##########G####
#......#######################...K..G..K.....#..K.#>#.#...K....#
#..K...############......K...w.............€..#...#.#.#........#
#....w.#.......w..#...K............K...w.......#s€#.#.#..s..K..#
###....#..s..K....G......G....w...........K.....#####.#........#
#k.>.K.d.....G...G....s..........K...s..........Ä..p..Ä....w...#
###....#...K....K.#......K.............K....G...#####.#........#
#..w...############..G.............G....K..w...#..#.#.#..s..K..#
#....K.#######################..w.............#...#>#.#........#
#.K....#..w...K.........w.....#.......K......#.w.##########G####
#...s..#............K.....K....#.........w..#.....K............#
#..K...d...K......w.....€.......############...s.......K....K..#
#....w.#.......s.....K.....w...K....w.......K.....K......w....€#
################################################################
"""
import random
import subprocess
princess=False 
tür="d"
hp=200
hero_hunger=0
hero="@"
hero_gold=0
food=0
herox=1
heroy=2
heroz=0
#level=list(dungeon)
level=[]
for d in (dungeon1,dungeon2,dungeon3):
    l=[]
    for line in d.splitlines():
        l.append(list(line))
    level.append(l) 
eg=("Mhmm!","Das tat gut!","Mehr davon!","Fressi Fressi!","Danke dafür!")
gg=("Money,Money,Money!","Gleich bin ich reich!","Bar auf die Kralle")
rg=("Heute ist aber ein schöner Tag!","Viel Sonne gibt es hier aber nicht")
while hero_hunger<50:
    hero_hunger+=random.choice((0,0,0,0,0,0,0,0,0,0,0
    ,1,1,1,1,1,1,2))
    #for x,c in enumerate(level):
     #   if x==herox:
      #      print(hero,end="")
       # else:
        #    print(c,end="")
    #print()
    for y, line in enumerate(level[heroz]):
        for x,c in enumerate(line):
            if x==herox and y==heroy:
                print(hero,end="")
            else:
                print(c,end="")
        print()
    command=input("gold:{} food:{} hunger:{} hp:{} Was willst du nun tun?".format(hero_gold,food,hero_hunger,hp))
    dx=0 
    dy=0
    if command=="a":
       # herox-=1
       dx=-1
    if command=="d":
        #herox+=1
        dx=1
    if command=="s":
        dy=1
    if command=="w":
        dy=-1
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
    #-------In Wand gelaufen?------
    target=level[heroz][heroy+dy][herox+dx]
    if target=="#":
        dx=0
        dy=0
        print ("Autsch, ich bin in eine Mauer gelaufen!")
    # in Monster gelaufen?
    #target=level[herox+dx]
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
            level[heroz][heroy+dy][herox+dx]="."
        else:
            print ("Du verlierst!")
            dx=0
            dy=0
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
            level[heroz][heroy+dy][herox+dx]="."
        else:
            print ("Du verlierst!")
            dx=0
            dy=0
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
            level[heroz][heroy+dy][herox+dx]="."
            print ("Du verlierst!")
            dx=0
            dy=0
    #------Gorilla-Ende------
    herox+=dx
    heroy+=dy
    # aufheben
    stuff=level[heroz][heroy][herox]
    if stuff=="€":
        hero_gold+=1
        level[heroz][heroy][herox]="."
        print(random.choice(gg))
    if stuff=="w":
        food+=2
        level[heroz][heroy][herox]="."
    if stuff=="s":
        food+=3
        level[heroz][heroy][herox]="."
        print(random.choice(rg))
    if stuff=="p":
        level[heroz][heroy][herox]="."
        subprocess.call(("espeak","Congratulation you have saved the princess!"))
        princess=True
        break
 
 
 
 #-----Spiel vorbei-----
if princess:
        subprocess.call(("espeak","You have safed the day!"))
else:
    
    print("Game Over!")
    subprocess.call(("espeak","Game Over!"))
        
        
            

