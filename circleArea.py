import math

PI = math.pi

def area(radius,accuracy = 9):

    dR = t_dR= math.pow(10,-1*accuracy)
    initial = 1
    while t_dR != 1:
        initial *= 10
        t_dR *= 10

    area = x = 0

    #due to some errors instead of x < radius we use x < radius - dR
    while x < radius - dR: 
        for i in range(1,initial+1):
            area += 2*PI*x*dR
            x += dR
            #print(x,area,sep = "\n",end = "\n\n")
    return area
r = 1
print(area(r))
print(PI*r*r)