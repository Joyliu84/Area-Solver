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
    print("Triangle \nCircle \nSquare \nRectangle \nParallelogram \n")
    print("Please enter all dimensions in cm")
    
    choice = input("Please enter your choice here: ")
    choice = choice.lower()
    
    if choice == "triangle":
        print("You chose triangle")
        print("Please enter the dimensions for your shape")
        
        try:
            triangleHeight = int(input("Height: "))
            triangleBase = int(input("Base: "))
        except:
            print("Please only enter an integer")

        triangle_area = (triangleHeight * triangleBase) / 2
        triangle_perimeter = math.sqrt((triangleHeight * triangleHeight) + (triangleBase * triangleBase))

        triangle_area = str(triangle_area)
        triangle_perimeter = str(triangle_perimeter)

        print("Perimeter of the triangle is " + triangle_perimeter)        
        print("Area of the triangle is " + triangle_area)

    elif choice == "circle":
        print("You chose circle")
        print("Please enter the dimensions for your shape")
    
    elif choice == "square":
        print("You chose square")
        print("Please enter the dimensions for your shape")
    
    elif choice == "rectangle":
        print("You chose rectangle")
        print("Please enter the dimensions for your shape")
    
    elif choice == "parallelogram":
        print("You chose parallelogram")
        print("Please enter the dimensions for your shape")
    
    else:
        print("Choice not found, please check your spelling")



area_solver()