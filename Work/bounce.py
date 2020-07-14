# bounce.py
#
# Exercise 1.5

Height=100.0 #meters
Bounce= 0

while Bounce<10:
    Bounce = Bounce +1
    Height= Height* 3/5
    print(Bounce, round(Height, 4))
    
