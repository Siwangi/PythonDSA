import turtle

def main():
    window = turtle.getscreen()
    window.bgcolor('green')
    brad=turtle.Turtle()
    brad.shape("turtle")
    brad.color("yellow")
    brad.speed(2)
    for x in range(1, 5):
        draw_square(brad)
        brad.right(10)
    window.exitonclick()

    # draw_circle()



def draw_square(Ace):
    for movement in range(1, 5):
        Ace.forward(100)
        Ace.right(90)


"""
    brad.forward(100)
    brad.right(90)
    brad.forward(100)
    brad.right(90)
    brad.forward(100)
    brad.right(90)
    brad.forward(100)
    brad.right(90)
"""
"""

def draw_circle():
    fish = turtle.Turtle()
    fish.shape("arrow")
    fish.circle(100)
    fish.speed(10)
    fish.color("blue")

"""





main()



# Turtle --- class
# Brad and fish -- instances of the class



