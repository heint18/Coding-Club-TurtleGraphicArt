import turtle

wn = turtle.Screen()

Tracy = turtle.Turtle()

Tracy.pendown()

Tracy.fill(True)

for i in range(2):
	Tracy.color("DarkCyan")
	Tracy.right(60)
	Tracy.circle(50)
	Tracy.fill(True)
	Tracy.color("Cyan")
	Tracy.right(60)
	Tracy.circle(50)
	Tracy.fill(True)
	Tracy.color("dark orchid")
	Tracy.right(60)
	Tracy.circle(50)
	Tracy.fill(True)

Tracy.penup()

Tracy.goto(-200,200)

Tracy.pendown()

for i in range(2):
	Tracy.color("dark violet")
	Tracy.right(60)
	Tracy.circle(50)
	Tracy.fill(True)
	Tracy.color("DarkMagenta")
	Tracy.right(60)
	Tracy.circle(50)
	Tracy.fill(True)
	Tracy.color("coral")
	Tracy.right(60)
	Tracy.circle(50)
	Tracy.fill(True)
	
Tracy.penup()

Tracy.goto(200,200)

Tracy.pendown()

for i in range(2):
	Tracy.color("DarkTurquoise")
	Tracy.right(60)
	Tracy.circle(50)
	Tracy.fill(True)
	Tracy.color("Cyan")
	Tracy.right(60)
	Tracy.circle(50)
	Tracy.fill(True)
	Tracy.color("aquamarine")
	Tracy.right(60)
	Tracy.circle(50)
	Tracy.fill(True)
	
Tracy.penup()

Tracy.goto(200,-200)

Tracy.pendown()

for i in range(2):
	Tracy.color("red")
	Tracy.right(60)
	Tracy.circle(50)
	Tracy.fill(True)
	Tracy.color("coral")
	Tracy.right(60)
	Tracy.circle(50)
	Tracy.fill(True)
	Tracy.color("dark salmon")
	Tracy.right(60)
	Tracy.circle(50)
	Tracy.fill(True)
	
Tracy.penup()

Tracy.goto(-200,-200)

Tracy.pendown()

for i in range(2):
	Tracy.color("DarkCyan")
	Tracy.right(60)
	Tracy.circle(50)
	Tracy.fill(True)
	Tracy.color("cornflower blue")
	Tracy.right(60)
	Tracy.circle(50)
	Tracy.fill(True)
	Tracy.color("DarkGoldenrod")
	Tracy.right(60)
	Tracy.circle(50)
	Tracy.fill(True)
	
turtle.mainloop()