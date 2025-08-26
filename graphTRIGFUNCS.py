import math
import turtle
import random
import array as ar

window = turtle.Screen()
window.bgcolor("black")
window.colormode()

pen = turtle.Turtle()
pen.color("white")
pen.speed(30)
pen.hideturtle()
pen.up()
pen.goto(0,-400)
pen.down()

def make_graph() :
    scaleX = int(turtle.textinput("Scale", "Scale of X Axis (1 unit is = 10x10 pixels): "))
    scaleY = int(turtle.textinput("Scale", "Scale of Y Axis (1 unit is = 10x10 pixels): "))
    scaleX*=10
    scaleY*=10
    for j in range (-400,400) :
        if j%scaleY == 0: 
            pen.goto(-5,j)
            pen.goto(0, j)
        else : 
            pen.goto(0,j)

    pen.up()
    pen.goto(-400,0)
    pen.down()
    
    for k in range (-400,400) :
        if k%scaleX == 0 : 
            pen.goto(k,-5)
            pen.goto(k,0)
        else : 
            pen.goto(k,0)
    
def buttons(x_pos,y_pos,text) : 
    pen.up()
    pen.goto (x_pos, y_pos)
    pen.down()
    for i in range (2):
        pen.left(90)
        pen.forward(30)
        pen.left(90)
        pen.forward(50)
    
    pen.up()
    pen.goto(x_pos-38,y_pos+7)
    pen.down()
    pen.write(text, font=('Arial', 8, 'normal'))

def create_lines() : 
    x1 = 1
    y1 = 0 

    m = int(turtle.textinput("Slope", "Slope of line: "))
    b = int(turtle.textinput("Y-intercept", "Y-intercept of line: "))*10
    y1 = m*-400+b

    pen.up()
    pen.goto(-400, y1)
    pen.down()

    y1 = m*400+b
    pen.goto(400, y1)

def create_circle() : 
    radius = (int(turtle.textinput("Radius", "Radius of circle: ")))*10
    x_cent = (int(turtle.textinput("X Center", "X-cord of center: ")))*10
    y_cent = (int(turtle.textinput("Radius", "Y-cord of center: ")))*10

    pen.up()
    pen.goto(x_cent, y_cent-radius)
    pen.down()
    pen.circle(radius)

def create_parabola() : 
    pen.down()
    type_polynomial = int(turtle.textinput("Polynomial","Degree of polynomial: "))
    terms_polynomial = []
    y_vals_polynomial = []

    for i in range (type_polynomial+1) : 
        i = str(i)
        print_out = "Term for x^",i
        term_vals = int(turtle.textinput("Terms", print_out))
        i = int(i)
        terms_polynomial.insert(i,term_vals)

    for j in range (-50,50) : 
        for k in range (type_polynomial+1) : 
            vals = terms_polynomial[k] * (j**k)
            y_vals_polynomial.insert(k,vals)
            
            print(j,k, terms_polynomial[k], vals)
        print(j, sum(y_vals_polynomial))
        
        if (j == -50) : 
            pen.up()
            pen.goto(j*10, sum(y_vals_polynomial)*10)
            pen.down()
        else : 
            pen.goto(j*10, sum(y_vals_polynomial)*10)

        y_vals_polynomial.clear()

def get_trig_inputs() : 
    amp = float(turtle.textinput("Amplitude", "Amplitude of function: "))*10
    mid = float(turtle.textinput("Mid-line", "Mid-line of function: "))*10
    period = float(turtle.textinput("Period", "Period of function: "))*10
    translation = float(turtle.textinput("Translation", "Translation of function: "))*10

    return amp, mid, period, translation

def create_sin() : 
    amp, mid, period, translation = get_trig_inputs()
    for i in range (-50, 50) : 
        if (i == -50) : 
            pen.up()
            y = amp * math.sin(((2*math.pi)/period)*i + translation) + mid 
            print (i,y)
            pen.goto(i*10,y)
            pen.down()
        else: 
            y = amp * math.sin(((2*math.pi)/period)*i + translation) + mid 
            print (i,y)
            pen.goto(i*10,y)

def create_cos() : 
    amp, mid, period, translation = get_trig_inputs()
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

def create_tan() : 
    amp, mid, period, translation = get_trig_inputs()
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

def sinusodial_input_type() : 
    type_func = turtle.textinput("Type", "What kind of sinusodial function is it?")
    if type_func.lower() == "sin" : 
        create_sin()
    elif type_func.lower() == "cos" : 
        create_cos()
    elif type_func.lower() == "tan" :
        create_tan()

def on_button_click(x,y) :
    if x < -250 and x > -351 and y > 300 and y < 330 : 
        print(x,",",y)
        create_lines()
    elif x < -250 and x > -351 and y > 250 and y < 280 : 
        print(x,",",y)
        create_circle()
    elif x < -250 and x > -351 and y > 200 and y < 230 : 
        print(x,",",y)
        create_parabola()
    elif x < -250 and x > -351 and y > 150 and y < 180 : 
        print(x,",",y)
        sinusodial_input_type()
    elif x < -250 and x > -351 and y > 100 and y < 130 : 
        print(x,",",y)
        window.clearscreen()
        window.bgcolor("black")
        set_up()

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

x = 0
y = 0


set_up()

window.exitonclick()
