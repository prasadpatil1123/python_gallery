import math

def circle_stats(rad):
    area = math.pi * rad ** 2
    circumference = 2 * math.pi * rad 
    return area, circumference



# print(circle_stats(5))
a, c = circle_stats(5)
print("Area: {:.2f}, circumference: {:.2f}".format(a,c) ) 