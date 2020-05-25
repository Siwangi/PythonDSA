# import turtle
# define a function for drawing square
# Inside circle function Run a loop in which turtle makes squares to complete a circle

import turtle

def main():
    window = turtle.getscreen()
    window.bgcolor('green')
    brad=turtle.Turtle()
    brad.shape("turtle")
    brad.color("yellow")
    brad.speed(20)
    for x in range(1, 38):
        draw_square(brad)
        brad.right(10)
        brad.speed(20)
    window.exitonclick()




def draw_square(brad):
    for movement in range(1, 5):
        brad.forward(100)
        brad.right(90)


main()