import turtle

def draw_square(some_turtle):
    for i in range(1, 5):
        some_turtle.forward(100)
        some_turtle.right(90)
        
def draw_circle(some_turtle):
    for i in range(1, 7):
        some_turtle.forward(100)
        some_turtle.right(100)
def draw_art():
    window = turtle.Screen()
    window.bgcolor("black")
    #Brad to draw squares :)
    brad = turtle.Turtle()
    brad.shape("turtle")
    brad.color("yellow")
    for i in range(1, 37):
        draw_square(brad)
        brad.right(10)
    #Angie draws circle        
    angie = turtle.Turtle()
    angie.shape("turtle")
    angie.color("brown")
    angie.circle(100)
    for i in range(1, 37):
        draw_circle(angie)
        angie.right(10)

    window.exitonclick()

draw_art()
