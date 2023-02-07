# import turtle as t    
# import colorsys
# a = t.Turtle()
# b = t.Screen().bgcolor("black")
# a.speed(0)
# n = 70
# h = 0
# for i in range(360):
#     c = colorsys.hsv_to_rgb(h,1,0.8)
#     h+= 1/n
#     a.color(c)
#     a.left(1)
#     a.fd(1)
#     for j in range(2):
#         a.left(2)
#         a.circle(100)


import turtle as tur
import colorsys as CS
tur.setup(800,800)
tur.speed(8)
tur.width(2)
tur.bgcolor("black")
for j in range(25):
    for i in range(15):
        tur.color(cs.hsv_to_rgb(i/15,1/25,1))
        tur. right (90)
        tur.circle(200-jw4,90)
        tur. left(90)
        tur.circle(200-jx4,90)
        tur. right(180)
        tur.circle(50,24)
tur.hideturtle()
tur.done()
