import turtle

def draw_square(someTurtle):
	for i in range (1,5):
		someTurtle.forward(100)
		someTurtle.right(90)

def draw_art():
	window = turtle.Screen()
	window.bgcolor("red")
# Create yellow square
	#brad = turtle.Turtle()
	#brad.color("yellow")
	#draw_square(brad)
	

# Create Blue circle
	angie = turtle.Turtle()
	angie.shape("turtle")
	angie.color("blue")
	angie.circle(100)
	

#Create a Triangle
	tom = turtle.Turtle()
	tom.color("green")
	draw_square(tom)
	
	window.exitonclick()
draw_art()
