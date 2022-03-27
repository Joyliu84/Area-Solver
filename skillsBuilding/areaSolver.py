from ast import Pass
from calendar import c
import math

triangle = []
circle = []
square = []
rectangle = []
parallelogram = []


def triangle_calculation():   
    print("Please enter all dimensions in cm \n")

    while True:
        try:
            triangleHeight = int(input("Height: "))
            triangleBase = int(input("Base: "))

            break
        except:
            print("Please only enter an wholenumber")
      
    triangle_area = (triangleHeight * triangleBase) / 2
    hypo = math.sqrt((triangleHeight * triangleHeight) + (triangleBase * triangleBase))
    triangle_perimeter = hypo + triangleBase + triangleHeight

    triangle_area = str(triangle_area)
    triangle_perimeter = str(triangle_perimeter)

    print("\nPerimeter of the triangle is " + triangle_perimeter + " cm")        
    print("Area of the triangle is " + triangle_area  + " cm" + "\n")

    input("Press Enter to continue...")

            

def circle_calculation():
    print("\nPlease enter all dimensions in cm \n")

    while True:
        try:
            radius = int(input("Radius: "))

            break
        except:
            print("Please only enter an wholenumber")

    circleArea = (radius * radius) * math.pi
    circumference = 2 * radius * math.pi

    circumference = str(circumference)
    circleArea = str(circleArea)

    print("\nThe circumference is " + circumference + " cm")
    print("Area of the circle is " + circleArea + " cm")

    input("\nPress Enter to continue...")

def square_calculation():
    print("Please enter all dimensions in cm \n")

    while True:
        try:
            squareSide = int(input("Side: "))

            break
        except:
            print("Please only enter an wholenumber")

    square_area = squareSide * squareSide
    square_perimeter = squareSide * 4

    square_area = str(square_area)
    square_perimeter = str(square_perimeter)

    print("\nPerimeter of the square is " + square_perimeter + " cm")        
    print("Area of the square is " + square_area + " cm")
    
    input("Press Enter to continue...")

def rec_calculation():
    print("\nPlease enter all dimensions in cm \n")

    while True:
        try:
            recWidth = int(input("Width: "))
            recLength = int(input("length: "))

            break
        except:
            print("Please only enter an wholenumber")

    rec_area = recWidth * recLength
    rec_perimeter = (recWidth + recLength) * 2

    rec_area = str(rec_area)
    rec_perimeter = str(rec_perimeter)

    print("\nPerimeter of the rectangle is " + rec_perimeter + " cm")        
    print("Area of the rectangle is " + rec_area + " cm")
    
    input("\nPress Enter to continue...")

def par_calculation():   
    print("\nPlease enter all dimensions in cm \n")

    while True:
        try:
            parHeight = int(input("Height: "))
            parBase = int(input("Base: "))

            break
        except:
            print("\nPlease only enter an wholenumber \n")

    par_area = parHeight * parBase
    par_perimeter = (parHeight + parBase) * 2

    par_area = str(par_area)
    par_perimeter = str(par_perimeter)

    print("\nPerimeter of the parallelogram is " + par_perimeter + " cm")        
    print("Area of the parallelogram is " + par_area + " cm")

    input("\nPress Enter to continue...")

while True:
    print("\nArea and perimeter solver \n")
    print("Please choose by entering one of the following choices \n")
    print("Triangle \nCircle \nSquare \nRectangle \nParallelogram \nFinish Calculation \n")
    
    choice = input("Please enter your choice here: ")
    choice = choice.lower()
    
    if choice == "triangle":
        print("\nYou chose triangle")
        print("Please enter the dimensions for your shape \n")

        triangle_calculation()

    elif choice == "circle":
        print("\nYou chose circle")
        print("Please enter the dimensions for your shape")

        circle_calculation()

    elif choice == "square":
        print("\nYou chose square")
        print("Please enter the dimensions for your shape")

        square_calculation()

    elif choice == "rectangle":
        print("\nYou chose rectangle")
        print("Please enter the dimensions for your shape")

        rec_calculation()

    elif choice == "parallelogram":
        print("\nYou chose parallelogram")
        print("Please enter the dimensions for your shape")

        par_calculation()

    elif choice == "finish calculation":
        break

    else:
        print("\nChoice not found, please check your spelling")

        input("\nPress Enter to continue...")