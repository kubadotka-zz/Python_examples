import turtle

def draw_square(some_turtle):
    for i in range(1,5):
        some_turtle.forward(100)
        some_turtle.right(90)

def draw_art():
    window = turtle.Screen()
    window.bgcolor("red")
    kuba = turtle.Turtle()
    kuba.shape("turtle")
    kuba.color("blue")
    kuba.speed(8)
    for i in range(1,36):
        draw_square(kuba)
        kuba.right(10)
    for i in range(1,200):
        kuba.right(20)
        

    
    window.exitonclick()
draw_art()
