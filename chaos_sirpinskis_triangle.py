from turtle import *
from random import randint
import time

#Variabeln definiren.

Geschwindigkeit = input("Auf einer Scaler von 1 bis 10. Wie schnell soll das Programm laufen?\nGeschwindigkeit:")
howoften = input("Wie oft sollen Punkte gesetzt werden? (Empfolen sind ein paar 1000)\nAnzahl: ")
n = int(input("Ein Wie vile-Eck soll es sein?\nn-Eck:"))
f = 420
Null = 0
Liste = []
Liste_x = []
Liste_y = []
minx,miny,maxx,maxy = 0, 0, 0, 0
speed(int(Geschwindigkeit))
penup()
goto(0,-200)
pensize(1)

#1. Zeichne ein Vieleck mit n-Seiten
for i in range(n):
    Liste.append(pos())
    forward((360/n)*3)
    left(360/n)

#1.1. Finde die max und min werte heraus

for i in Liste:
    print(i)
    Liste_x.append(i[0])
    print(Liste_x)
    Liste_y.append(i[1])
    print(Liste_y)


for i in Liste_x:
    if i > maxx:
        maxx = i
    elif i<minx:
        minx = i
    else:
        continue

for i in Liste_y:
    if i > maxy:
        maxy = i
    elif i < miny:
        miny = i
    else:
        continue


#2. Einen Punkt auf dem Min max fenster aussuchen.

color("yellow")
begin_fill()
goto(minx,miny)
pendown()
goto(minx,maxy)
goto(maxx,maxy)
goto(maxx,miny)
goto(minx,miny)
end_fill()

color("blue")
penup()
goto(0,-200)
pendown()
begin_fill()
for i in range(n):
    Liste.append(pos())
    forward((360/n)*3)
    left(360/n)
end_fill()




penup()
color("white")
y = randint(round(miny),round(maxy))
x = randint(round(minx),round(maxx))
goto(x,y)


#3. Putting another point midway between the previous point and a random corner
while Null < int(howoften):
    ran_ecke = randint(0,(n-1))
    if n > 3:
        while f == ran_ecke:
            ran_ecke = randint(0,(n-1))
        
    print("entfernung zur", ran_ecke,". Ecke" ,round(distance(Liste[ran_ecke])/2))
    setheading(towards(Liste[ran_ecke]))
    forward(round(distance(Liste[ran_ecke])/2))
    pendown()
    forward(1)
    penup()
    f = ran_ecke
    Null+=1
#4. Repeat a few thousend times

input("Press a Key to stopp...")
