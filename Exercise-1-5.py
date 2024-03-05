import turtle;

sz= float(input("What size do yu want yur square to be: "))
color= input("What color do you want your square to be: ")

wn= turtle.Screen()
wn.title("Sheldon")
shelly= turtle.Turtle()

shelly.color(color)
for i in range(4):
    shelly.forward(sz)
    shelly.right(90)

wn.mainloop()