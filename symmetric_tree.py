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
wm.bgcolor("lightgreen")
wm.setup(width=window_width, height=window_height)

# setup the initial trunk
leo = turtle.Turtle()
leo.hideturtle()
leo.speed(0)
leo.penup()
leo.pensize(trunk_thickness)
leo.setpos((0, -int(window_height / 4)))
leo.setheading(90)
leo.pendown()
branch_turn = 0
leo.forward(trunk_length)
branch_ends.append((leo.pos(), leo.heading()))

total_branchs = 0

# begin making branches
while(branch_length > 0 and branch_thickness > 1):
    branch_gen += 1
    branch_thickness = int(trunk_thickness / branch_gen)
    branch_length = int(trunk_length / (branch_gen * 1.5))
    gen_branch_ends = branch_ends.copy()
    branch_ends = []
    gen_branch_turn = random.randrange(0, 91)
    for end, angle in gen_branch_ends:
        num_branches = 2
        total_branchs += num_branches
        branch_turn = gen_branch_turn
        for branch in range(num_branches):
            leo.penup()
            leo.pensize(branch_thickness)
            leo.setpos(end)
            leo.setheading(angle)
            leo.pendown()
            branch_turn = (-1 * branch_turn)
            leo.right(branch_turn)
            leo.forward(branch_length)
            branch_ends.append((leo.pos(), leo.heading()))
    localtime = time.asctime(time.localtime(time.time()))
    print("Branch Generation: " + str(branch_gen))
    print("Time: " + str(localtime))
    print("Generation Total Branches: " + str(total_branchs))
    print("Branch Thickness: " + str(branch_thickness))
    print("Branch Length: " + str(branch_length))
    print("Branch Turn: " + str(gen_branch_turn))
    print("")
    total_branchs = 0

wm.update()
wm.exitonclick()
