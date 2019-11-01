import turtle as t
import time

guess = input("guess my favourite shape! : ")
if guess =="square":

    t.color("green")
    t.begin_fill()

    counter = 0

    while counter < 4:
        t.forward(100)
        t.left(90)
        counter = counter + 1

    t.end_fill()
    time.sleep(3)
    print('You win')
else:
    print('You lose')


t.color("red")
t.begin_fill()

counter = 0

while counter < 360:
    t.forward(3)
    t.left(1)
    counter = counter +1

t.end_fill()
time.sleep(5)

# turtle.begin_fill()
# turtle.forward(100)
# turtle.left(90)
# turtle.forward(100)
# turtle.left(90)
# turtle.forward(100)
# turtle.left(90)
# turtle.forward(100)
# turtle.end_fill()
