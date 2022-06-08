from graphics import *
wind = GraphWin()
p1 = wind.getMouse()
p2 = wind.getMouse()
p3 = wind.getMouse()

traingle = Polygon(p1, p2, p3)
traingle.setFill('red')
traingle.draw(wind)

p1 = wind.getMouse()