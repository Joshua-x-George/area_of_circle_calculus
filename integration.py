import math

PI = math.pi

def area(function: str, startX, stopX, accuracy = 6):

    dX = t_dX= math.pow(10,-1*accuracy)
    initial = 1
    while t_dX != 1:
        initial *= 10
        t_dX *= 10
    x = startX
    sum = 0
    #due to some errors instead of x < stopX-dR we use x < stopX - dR
    while x < stopX - dX: 
        for i in range(1,initial+1):
            sum += eval(function)*dX
            x += dX
            print(x,sum,i)
    return sum
if __name__ == '__main__':
    #returns and prints the area of a circle of radius 2 (using the y as 2PIr)
    print(area('2*PI*x',0,2))