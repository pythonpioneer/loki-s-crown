import turtle

# changing background
window = turtle.Screen()
window.bgcolor('black')
crown = turtle.Turtle()
crown.color('gold')

# left horn of loki
hornl = turtle.Turtle()
hornl.color('gold')

# right horn of loki
hornr = turtle.Turtle()
hornr.color('gold')

# drawing left jaw
jawl = turtle.Turtle()
jawl.color('gold')

# drawing right jaw
jawr = turtle.Turtle()
jawr.color('gold')

crown.shape('turtle')
hornl.shape('turtle')
hornr.shape('turtle')
jawl.shape('turtle')
jawr.shape('turtle')

crown.speed(1)
hornl.speed(1)
hornr.speed(1)
jawl.speed(1)
jawr.speed(1)



#------------------------>
# the body
crown.up()
crown.backward(150)
crown.left(90)
crown.forward(50)
crown.down()
crown.begin_fill()
crown.fillcolor('gold')


hornl.up()
hornl.backward(150)
hornl.left(90)
hornl.forward(50)
hornl.down()
hornl.up()
hornl.setheading(315)
hornl.circle(200, 20)
hornl.down()
hornl.begin_fill()
hornl.fillcolor('gold')

hornr.up()
hornr.backward(150)
hornr.left(90)
hornr.forward(50)
hornr.setheading(315)
hornr.circle(200, 70)
hornr.down()
hornr.begin_fill()
hornr.fillcolor('gold')

jawl.up()
jawl.backward(150)
jawl.left(90)
jawl.forward(50)
jawl.down()
jawl.begin_fill()
jawl.fillcolor('gold')
jawr.up()
jawr.backward(150)
jawr.left(90)
jawr.forward(50)
jawr.setheading(315)
jawr.circle(200, 90)
jawr.down()
jawr.begin_fill()
jawr.fillcolor('gold')

crown.setheading(315)
crown.circle(200, 90)
hornl.setheading(135)
hornl.circle(-100, 100)
hornr.setheading(45)
hornr.circle(100, 100)
jawr.setheading(280)
jawr.circle(-370, 30)

crown.setheading(90)
crown.forward(30)
crown.setheading(225)
crown.circle(-200, 90)
hornr.setheading(300)
hornr.circle(-115, 70)
jawl.setheading(260)
jawl.circle(370, 30)

crown.setheading(270)
crown.forward(30)

hornl.setheading(240)
hornl.circle(115, 70)
jawl.setheading(0)
jawl.forward(30)
jawl.setheading(100)
jawl.circle(-360, 29)
jawr.setheading(180)
jawr.forward(30)
jawr.setheading(80)
jawr.circle(360, 29)


crown.end_fill()
jawl.end_fill()
jawr.end_fill()
hornl.end_fill()
hornr.end_fill()


crown.hideturtle()
hornl.hideturtle()
hornr.hideturtle()
jawl.hideturtle()
jawr.hideturtle()
turtle.done()
