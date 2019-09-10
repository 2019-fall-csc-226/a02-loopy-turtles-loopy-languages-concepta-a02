######################################################################
# Author: Concepta Njolima
# Username: njolimac
#
# Assignment: A02: Loopy Turtles
# Purpose: To demonstrate the turtle library and loops
###############################################

import turtle


def draw_design(turtle, text_turtle):
    """
    This function draws the background design

    :param turtle: turtle draws the design
                    text_turtle writes the text
    :return: none
    """
    for i in range(5):

        for i in ("red", "blue", "yellow", "green", "purple"):
            turtle.speed(0)
            turtle.pendown()
            turtle.color(i)
            turtle.pendown()
            turtle.begin_fill()
            turtle.circle(150)
            turtle.end_fill()
            turtle.penup()
            turtle.forward(5)
            turtle.left(15)
    write_text(text_turtle)

def write_text(turtle):
    """
    This function writes text
    :param turtle: The tutle writing the text
    :return: none
    """
    turtle.write("I AM HAPPY", move=False, align='center', font=("Arial", 30, ("bold", "normal")))


def main():

    """
    This is the main function
    :return:
    """
    wn = turtle.Screen()
    wn.bgcolor("sky blue")

    concepta = turtle.Turtle()
    text_draw = turtle.Turtle()
    concepta.penup()
    # concepta.setpos(-250,-250)
    draw_design(concepta, text_draw)

    wn.exitonclick()
main()