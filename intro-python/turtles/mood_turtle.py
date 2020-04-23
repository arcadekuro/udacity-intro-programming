mood = "happy"

import turtle
riley = turtle.Turtle()
riley.width(5)


for side in range(5):
    if mood == "happy":
        riley.color("yellow")
    if mood == "sad":
        riley.color("blue")
    if mood == "angry":
        riley.color("red")
    if False:
        riley.color("gray")
    riley.forward(100)
    riley.right(144)