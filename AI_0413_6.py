import turtle;
import random as r;

Colors = ["orange","red","violet","green","blue"]

t = turtle.Turtle();
t.shape("turtle");

for i in range (0, 9):

    t.penup();

    radius = r.randint(1, 101);
    centerX = r.randint(-200, 201);
    centerY = r.randint(-200, 201);

    t.color(r.choice(Colors));

    t.goto(centerX, centerY);  

    t.pendown();

    t.circle(radius);

turtle.mainloop();
turtle.bye();



    