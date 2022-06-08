from graphics import *

def main():
    wind = GraphWin("Polygon")
    wind.setCoords(0.0, 0.0, 10.0, 10.0)
    message = Text(Point(5, 0.5), "Click on three points")
    
    p1 = wind.getMouse()
    p1.draw(wind)
    
    p2 = wind.getMouse()
    p2.draw(wind)
    
    p3 = wind.getMouse()
    p3.draw(wind)
    
    traingle = Polygon(p1, p2, p3)
    traingle.setFill('red')
    traingle.setOutline('blue')
    traingle.draw(wind)
    
    message = Text(Point(5, 0.5), "Click on three points")
    message.draw(wind)
    p1 = wind.getMouse()
main()