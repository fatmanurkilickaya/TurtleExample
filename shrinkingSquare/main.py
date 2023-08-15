import turtle


turtle_screen = turtle.Screen()
turtle_screen.bgcolor("light blue")
turtle_screen.title("Turtle Python")

turtle_instance = turtle.Turtle()
turtle_instance.color("green")

def shrinkingSqaure(size):
    for i in range(4):
        turtle_instance.forward(size)
        turtle_instance.left(90)
        size = size - 5


shrinkingSqaure(150)
shrinkingSqaure(130)
shrinkingSqaure(100)
shrinkingSqaure(80)
shrinkingSqaure(50)
shrinkingSqaure(30)


turtle.done()