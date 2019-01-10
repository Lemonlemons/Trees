import turtle
import random
import time

# let's make some basic variables:
window_width = 600
window_height = int(window_width * 1.5)
trunk_thickness = 25
trunk_length = int(window_width * 0.5)
total_branch_width = 0
branch_ends = []
branch_gen = 1
branch_thickness = trunk_thickness
branch_length = trunk_length

# Setup the screen
wm = turtle.Screen()
wm.delay(0)
# wm.tracer(0, 0)
wm.bgcolor("lightblue")
wm.setup(width=window_width, height=window_height)

# setup the initial trunk
leo = turtle.Turtle()
leo.hideturtle()
leo.speed(0)
leo.penup()
random_color = "#000"
leo.pencolor(random_color)
leo.pensize(trunk_thickness)
leo.setpos((0, -int(window_height / 4)))
leo.setheading(90)
leo.pendown()
branch_turn = 0
leo.forward(trunk_length)
branch_ends.append((leo.pos(), leo.heading()))

total_branchs = 0

# begin making branches
while(branch_length > 0 and branch_thickness > 2):
    branch_gen += 1
    branch_thickness = int(trunk_thickness / branch_gen)
    branch_length = int(trunk_length / (branch_gen * 1.5))
    gen_branch_ends = branch_ends.copy()
    branch_ends = []
    for end, angle in gen_branch_ends:
        num_branches = random.randint(3, 5)
        total_branchs += num_branches
        for branch in range(num_branches):
            leo.penup()
            random_color = "#" + ("%06x" % random.randint(0, 0xFFFFFF))
            leo.pencolor(random_color)
            leo.pensize(branch_thickness)
            leo.setpos(end)
            leo.setheading(angle)
            leo.pendown()
            branch_turn = random.randrange(-90, 91)
            leo.right(branch_turn)
            leo.forward(branch_length)
            branch_ends.append((leo.pos(), leo.heading()))
    # wm.update()
    localtime = time.asctime(time.localtime(time.time()))
    print(localtime)
    print(total_branchs)
    print(branch_thickness)
    total_branchs = 0

wm.update()
wm.exitonclick()
