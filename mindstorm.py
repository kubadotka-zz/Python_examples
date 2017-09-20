import turtle

def draw_square():

    window = turtle.Screen()
    window.bgcolor("blue")
    
    kuba = turtle.Turtle()
    kuba.shape("turtle")
    kuba.color("green", "black")
    kuba.speed(speed = 8)
    kuba.right(30)
    kuba.circle(50, extent = 250, steps = 100)
    kuba.setheading(90)
    kuba.forward(100)
    kuba.circle(35, extent = 180, steps = 100)
    kuba.forward(100)
    kuba.setheading(145)
    kuba.circle(50, extent = 250, steps = 100)

    
    window.exitonclick()
draw_square()
