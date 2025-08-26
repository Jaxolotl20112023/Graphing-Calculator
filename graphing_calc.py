import math
import turtle
import random
import array as ar

# setting up the screen
window = turtle.Screen()
window.bgcolor("black")
window.colormode()

# setting up the pen/turtle
pen = turtle.Turtle()
pen.color("white")
pen.speed(30)
pen.hideturtle()

# preparing the pen to draw the graph
pen.up()
pen.goto(0,-400)
pen.down()

# function that draws the graph
def make_graph() :
    # get the scale for the x and y axis
    scaleX = int(turtle.textinput("Scale", "Scale of X Axis (1 unit is = 10x10 pixels): "))
    scaleY = int(turtle.textinput("Scale", "Scale of Y Axis (1 unit is = 10x10 pixels): "))
    
    # convert the unit scale into pixels
    scaleX*=10
    scaleY*=10
    
    # create the 800 pixel long y-axis
    for j in range (-400,400) :

        # makes the tick marks for the y-axis
        if j%scaleY == 0: 
            pen.goto(-5,j)
            pen.goto(0, j)
        else : # makes the rest of the vertical line
            pen.goto(0,j)

    # moves to the left end of the screen
    pen.up()
    pen.goto(-400,0)
    pen.down()
    
    # makes the tick marks for the x-axis
    for k in range (-400,400) :
        if k%scaleX == 0 : 
            pen.goto(k,-5)
            pen.goto(k,0)
        else : # makes the rest of the horizontal line
            pen.goto(k,0)

# function that creates the buttons 
def buttons(x_pos,y_pos,text) : 

    # go to where we want to make the button
    pen.up()
    pen.goto (x_pos, y_pos)
    pen.down()

    # draw the rectangle shape
    for i in range (2):
        pen.left(90)
        pen.forward(30)
        pen.left(90)
        pen.forward(50)
    
    # go to the middle, left side of the button
    pen.up()
    pen.goto(x_pos-38,y_pos+7)
    pen.down()
    pen.write(text, font=('Arial', 8, 'normal')) # create text

# function that creates the line
def create_lines() : 
    # y-value will store the output of line equation
    y = 0 

    # get the slope and y-intercept of the line
    m = int(turtle.textinput("Slope", "Slope of line: "))
    b = int(turtle.textinput("Y-intercept", "Y-intercept of line: "))*10 # convert the y-intercept into pixels

    # find the start value of the line
    y = m*-400+b

    # go to the start value of the line
    pen.up()
    pen.goto(-400, y)
    pen.down()

    # find and go to the end value of the line
    y = m*400+b
    pen.goto(400, y)

# function that creates a circle
def create_circle() : 
    # gets the radius and center x and y values. Converting it into pixels
    radius = (int(turtle.textinput("Radius", "Radius of circle: ")))*10
    x_cent = (int(turtle.textinput("X Center", "X-cord of center: ")))*10
    y_cent = (int(turtle.textinput("Radius", "Y-cord of center: ")))*10

    # go to the center x of the circle and at the bottom of circle
    pen.up()
    pen.goto(x_cent, y_cent-radius)
    pen.down()
    pen.circle(radius) # creates the circle

# function that creates the polynomial graph
def create_polynomial() : 
    # get the degree of the polynomial
    pen.down()
    type_polynomial = int(turtle.textinput("Polynomial","Degree of polynomial: "))
    # set up the lists that will store all the erms and the outputs
    terms_polynomial = []
    y_vals_polynomial = []

    # this loop will get the values for each x
    for i in range (type_polynomial+1) : 
        i = str(i) # convert it to a string to print
        print_out = "Term for x^",i 
        term_vals = int(turtle.textinput("Terms", print_out)) # get the term val
        i = int(i) # convert it back to an integer to turn it into the index
        terms_polynomial.insert(i,term_vals) # save the term_vals into the array

    # this loop will graph the polynomil between x=-50 and x=50
    for j in range (-50,50) : 
        # calculate the value of each term
        for k in range (type_polynomial+1) : 
            vals = terms_polynomial[k] * (j**k) 
            y_vals_polynomial.insert(k,vals) # save it into the y_vals_polynomial list

        # the prints are used for testing    
            print(j,k, terms_polynomial[k], vals)
        print(j, sum(y_vals_polynomial)) 
        
        # the first point it lifts the pen up before moving to avoid drawing a line
        if (j == -50) : 
            pen.up()
            pen.goto(j*10, sum(y_vals_polynomial)*10) # convert the x and y vals to pixels and go to that pos
            pen.down()
        else : 
            pen.goto(j*10, sum(y_vals_polynomial)*10) # covner the x and y vals to pixels and go to that pos

        y_vals_polynomial.clear() # clear all the values in the list

# function that gets the inputs for the trig functiion
def get_trig_inputs() : 
    # convert the values into a float and then into pixels
    amp = float(turtle.textinput("Amplitude", "Amplitude of function: "))*10
    mid = float(turtle.textinput("Mid-line", "Mid-line of function: "))*10
    period = float(turtle.textinput("Period", "Period of function: "))*10
    translation = float(turtle.textinput("Translation", "Translation of function: "))*10

    # return the values to use in other functions
    return amp, mid, period, translation

# function that graphs the sin trig function
def create_sin() : 
    # get the inputs for the trig function
    amp, mid, period, translation = get_trig_inputs()
    # graph the trig function between x=-50 and x=50
    for i in range (-50, 50) : 
        # prevents drawing a line to the first point
        if (i == -50) : 
            pen.up()
            y = amp * math.sin(((2*math.pi)/period)*i + translation) + mid 
            print (i,y)
            pen.goto(i*10,y) # convert the x into pixels 
            pen.down()
        else:  
            # draws the rest of the function normally
            y = amp * math.sin(((2*math.pi)/period)*i + translation) + mid 
            print (i,y)
            pen.goto(i*10,y)

# function that graphs the cos trig function
def create_cos() : 
    # get the inputs for the trig func
    amp, mid, period, translation = get_trig_inputs()
    # same as sin function, but using cos instead
    for i in range (-50, 50) : 
        if (i == -50) : 
            pen.up()
            y = amp * math.cos(((2*math.pi)/period)*i + translation) + mid 
            print (i,y)
            pen.goto(i*10,y)
            pen.down()
        else: 
            y = amp * math.cos(((2*math.pi)/period)*i + translation) + mid 
            print (i,y)
            pen.goto(i*10,y)

# function that graphs the tan function
def create_tan() : 
    amp, mid, period, translation = get_trig_inputs()
    # same as all other trig functions, but instead with tan
    for i in range (-50, 50) : 
        if (i == -50) : 
            pen.up()
            y = amp * math.tan(((2*math.pi)/period)*i + translation) + mid 
            print (i,y)
            pen.goto(i*10,y)

            pen.down()
        else: 
            y = amp * math.tan(((2*math.pi)/period)*i + translation) + mid 
            print (i,y)
            pen.goto(i*10,y)

# get the input for the type of trig func
def sinusodial_input_type() : 
    # ask the kind 
    type_func = turtle.textinput("Type", "What kind of sinusodial function is it?")
    # run the corresponding function to the input
    if type_func.lower() == "sin" : 
        create_sin()
    elif type_func.lower() == "cos" : 
        create_cos()
    elif type_func.lower() == "tan" :
        create_tan()

# function that checks when each button is clicked
def on_button_click(x,y) :
    if x < -250 and x > -351 and y > 300 and y < 330 : 
        print(x,",",y)
        create_lines() # run the function that corresponds to that button
    elif x < -250 and x > -351 and y > 250 and y < 280 : 
        print(x,",",y)
        create_circle()
    elif x < -250 and x > -351 and y > 200 and y < 230 : 
        print(x,",",y)
        create_polynomial()
    elif x < -250 and x > -351 and y > 150 and y < 180 : 
        print(x,",",y)
        sinusodial_input_type()
    elif x < -250 and x > -351 and y > 100 and y < 130 : 
        print(x,",",y)
        window.clearscreen()
        window.bgcolor("black")
        set_up()

# function that sets up the graph, buttons and screen clicks
def set_up() : 
    make_graph()
    buttons(-300,300,"Lines")
    buttons(-300,250,"Circles")
    buttons(-300,200,"Parabolas")
    buttons(-300,150,"Sinusodial Function")
    buttons(-300,100,"Clear")

    turtle.listen()
    window.onscreenclick(on_button_click, 1)
    turtle.done()

set_up() # run the set_up func at the beginning 

window.exitonclick() # allows program to exit 
