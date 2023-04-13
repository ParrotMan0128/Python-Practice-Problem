import turtle;
import random as r;

t = turtle.Turtle();

t.speed(7);
t.width(3);

colors = ["orange","red","violet","green","blue"]

for i in range(0, 100):

    t.color(r.choice(colors));

    t.right(20+i)
    t.forward(1+(i*6))
    t.right(30+i)

turtle.mainloop();
turtle.bye();
