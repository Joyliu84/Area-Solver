from calendar import c
import math

triangle = []
circle = []
square = []
rectangle = []
parallelogram = []


def area_solver():
    #loop from here?
    print("\nArea and perimeter solver \n")
    print("Please choose by entering one of the following choices \n")
    print("Triangle \nCircle \nSquare \nRectangle \nParallelogram \nFinish Calculation")
    print("Please enter all dimensions in cm \n")
    
    choice = input("Please enter your choice here: ")
    choice = choice.lower()
    
    if choice == "triangle":
        print("\nYou chose triangle")
        print("Please enter the dimensions for your shape \n")
        
        try:
            triangleHeight = int(input("Height: "))
            triangleBase = int(input("Base: "))
        except:
            print("Please only enter an integer")

        triangle_area = (triangleHeight * triangleBase) / 2
        triangle_perimeter = math.sqrt((triangleHeight * triangleHeight) + (triangleBase * triangleBase))

        triangle_area = str(triangle_area)
        triangle_perimeter = str(triangle_perimeter)

        print("\nPerimeter of the triangle is " + triangle_perimeter)        
        print("Area of the triangle is " + triangle_area + "\n")

    elif choice == "circle":
        print("You chose circle")
        print("Please enter the dimensions for your shape")

        try:
            radius = int(input("Radius: "))
        except:
            print("Please only enter an integer")

        circleArea = (radius * radius) * math.pi
        circumference = 2 * radius * math.pi

        circumference = str(circumference)
        circleArea = str(circleArea)

        print("The circumference is " + circumference)
        print("Area of the circle is " + circleArea)


    elif choice == "square":
        print("You chose square")
        print("Please enter the dimensions for your shape")

        try:
            squareSide = int(input("Side: "))
        except:
            print("Please only enter an integer")

        square_area = squareSide * squareSide
        square_perimeter = squareSide * 4

        square_area = str(square_area)
        square_perimeter = str(square_perimeter)

        print("Perimeter of the square is " + square_perimeter)        
        print("Area of the square is " + square_area)
    
    elif choice == "rectangle":
        print("You chose rectangle")
        print("Please enter the dimensions for your shape")

        try:
            recWidth = int(input("Width: "))
            recLength = int(input("length: "))
        except:
            print("Please only enter an integer")

        rec_area = recWidth * recLength
        rec_perimeter = (recWidth + recLength) * 2

        rec_area = str(rec_area)
        rec_perimeter = str(rec_perimeter)

        print("Perimeter of the rectangle is " + rec_perimeter)        
        print("Area of the rectangle is " + rec_area)
    
    
    elif choice == "parallelogram":
        print("You chose parallelogram")
        print("Please enter the dimensions for your shape")
    
        try:
            parHeight = int(input("Height: "))
            parBase = int(input("Base: "))
        except:
            print("Please only enter an integer")

        par_area = parHeight * parBase
        par_perimeter = (parHeight + parBase) * 2

        par_area = str(par_area)
        par_perimeter = str(par_perimeter)

        print("Perimeter of the parallelogram is " + par_perimeter)        
        print("Area of the parallelogram is " + par_area)

    else:
        print("Choice not found, please check your spelling")



area_solver()