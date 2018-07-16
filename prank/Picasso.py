import turtle

def draw_square():
    window = turtle.Screen()
    window.bgcolor("blue")
    
    brad = turtle.Turtle()
    brad.shape("turtle")
    brad.color("yellow")
    
    brad.forward(100)
    brad.right(90)
    brad.forward(100)
    brad.right(90)
    brad.forward(100)
    brad.right(90)
    brad.forward(100)
    brad.right(90)
    brad.forward(100)
    brad.right(90)

    cubzz = turtle.Turtle()
    cubzz.shape("turtle")
    cubzz.color("black")
    cubzz.circle(100)
    

    window.exitonclick()
    
draw_square()
