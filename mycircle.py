from swampy.TurtleWorld import *
from math import *
world = TurtleWorld()
bob = Turtle()
print bob
bob.delay=0.02

def polygon(t,length,n):
	t=Turtle()
	#t.delay = (0.01)
	for iiiii in range(n):
		fd(t,length)
		lt(t, 360/n)
polygon(bob, 50, 8)

world.clear()
"""
#gen's solution for reference
def circle(turtle,radius):
 	circumference = 2 * pi * radius
	factor = radius/5
	sides = int(circumference/factor)
	length = circumference / sides
	polygon(turtle,length,sides)

circle(bob,20)

wait_for_user()
"""
#from math import *
bob.delay=0.01
def circle(t,r):
	#t = Turtle()
	circum = 2 * pi * r
	n = int(circum/3) +1
	length = circum / n
	polygon(t,length,n)		
circle(bob,50)

world.clear()
"""
def polyline(t, n, length, angle):
	for i in range(n):
		fd(t, length)
		lt(t, angle)
polyline(t,n,length,angle)

def polygon(t, n, length):
	angle = 360.0 / n
	polyline(t, n, length, angle)
"""
def arc(t, r, theta):
	arc_length = 2 * pi * r * theta / 360
	n = int(arc_length / 3) + 1
	step_length = arc_length / n
	step_angle = float(theta) / n
	for i in range(n):
			fd(t, step_length)
			lt(t, step_angle)
arc(bob,50,60)

#polyline(t, n, step_length, step_angle)


"""
def arc(t, r, angle):
	arc_length = 2 * pi * r * angle / 360
	n = int(arc_length / 3) + 1
	step_length = arc_length / n
	step_angle = float(angle) / n

	for i in range(n):
		fd(t, step_length)
		lt(t, step_angle)

arc(bob,20,30)
"""
wait_for_user()
	