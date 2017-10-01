"""
slope of line: y = mx + b
y = y
m = slope (rise over run)
x = x
b = y intercept
"""

def collect_inputs():
    #collect inputs and turn inputs into a list
    input_x1 = float(raw_input("Enter x1: "))
    input_y1 = float(raw_input("Enter y1: "))
    input_x2 = float(raw_input("Enter x2: "))
    input_y2 = float(raw_input("Enter y2: "))   
    x_and_y_input = [input_x1,input_y1,input_x2,input_y2]
    return x_and_y_input

"""
def return_coord(n):
    \"""this turns x and y from their respective
        lists into a useful format [x,y] for calculating slope and intercept
    \"""
    x_and_y = [x_list[n], y_list[n]]
    return x_and_y
"""
    
def calc_slope(x_and_y):
    #this calculates slope based on two x and y coords
    x1 = x_and_y[0]
    y1 = x_and_y[1]
    x2 = x_and_y[2]
    y2 = x_and_y[3]
    m = (y2 - y1) / (x2 - x1)
    return m

def calc_y_intercept(x_y,slope):
    b = x_y[1] - (slope * x_y[0])
    return b
        
def make_x_and_y(x_range, y, slope, y_intercept):
    #this makes x_list and y_list given an x range
    #need to adjust the y formula to accept slope or just make it return y intercept
    for item in range(x_range):
        x = float(item)
        y1 = y[1]
        m = slope
        b = y_intercept
        y1 = (m * x) + b
        x_list.append(x)
        y_list.append(y1)
    return x_list, y_list

def print_coord(n):
    #return a string of coords from a list
    return "(" + str(x_list[n]) + "," + str(y_list[n]) + ")"

def dist_btwn_pts(x_and_y):
    x1 = x_and_y[0]
    x2 = x_and_y[2]
    y1 = x_and_y[1]
    y2 = x_and_y[3]
    dx = (x2 - x1)
    dy = (y2 - y1)
    dist = ((dx ** 2) + (dy ** 2)) ** .5
    return dist

x_list = []
y_list = []

x_and_y_input = collect_inputs()

m = calc_slope(x_and_y_input)

y_intercept = calc_y_intercept(x_and_y_input, m)

dist = dist_btwn_pts(x_and_y_input)

print "inputs"
print x_and_y_input

print "Slope"
print m

print "Y intercept"
print y_intercept

print "make a list based on make_x_and_y"
print make_x_and_y(5, x_and_y_input, m, y_intercept)

print "(x,y) in string"
print print_coord(3)

print "distance between points"
print dist

"""



print "[x,y] at given number"
print return_coord(3)

"""
