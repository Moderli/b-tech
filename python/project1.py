#first project 
#this is a comment
#this program defines the process of the calculation for finding the area of the triangle
import math
#input sides 
sa = int(input("please enter the first side : "))
sb = int(input("please enter the second side : "))
sc = int(input("please enter the first side : "))

#process the sides in to a formula

s = (sa + sb + sc)/2
m = math.sqrt(s)
area = (s*(s-sa)*(s-sb)*(s-sc)) ** 0.5

print(area , m)   #prints the area of the triangle
