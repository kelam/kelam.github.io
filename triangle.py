import turtle
w = turtle.Turtle()
w.speed(1)
turtle.delay(0)
def tri(s):
    for i in range (3):
        w.forward(s)
        w.left(120)
x = 10
for i in range (3):
    for i in range (3):
        for i in range (3):
            for i in range (3):
                for i in range (3):
                    for i in range (3):
                        tri(x)
                        w.forward(2*x)
                        w.left(120)
                    w.forward(4*x)
                    w.left(120)
                w.forward(8*x)
                w.left(120)
            w.forward(16*x)
            w.left(120)
        w.forward(32*x)
        w.left(120)
    w.forward(64*x)
    w.left(120)
    
