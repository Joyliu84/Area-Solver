from ast import Pass
from calendar import c
import math

#Lists to store answers
triangle_area_list = []
triangle_perimeter_list = []
circle_area_list = []
circumference_list = []
square_area_list = []
square_perimeter_list = []
rectangle_area_list = []
rectangle_perimeter_list = []
parallelogram_area_list = []
parallelogram_perimeter_list = []


def triangle_calculation():   #calculates triangle area and perimeter and save answers into lists for later
    print("Please enter all dimensions in cm \n")


    while True: #checks for invalid input such as negative numbers and letters

        try:
            triangle_height = float(input("Height: "))
            if triangle_height <= 0:
                print("Please enter a positive number")
                continue
            triangle_base = float(input("Base: "))
            if triangle_base <= 0:
                print("Please enter a positive number")
                continue
            triangle_side1 = float(input("Side 1:"))
            if triangle_side1 <= 0:
                print("Please enter a postitive numnber")
                continue
            triangle_side2 = float(input("Side 2:"))
            if triangle_side2 <= 0:
                print("Please enter a postitive numnber")
                continue
            triangle_side3 = float(input("Side 3:"))
            if triangle_side3 <= 0:
                print("Please enter a postitive numnber")
                continue
            break
        except:
            print("Please only enter a number")


      
    triangle_area = (triangle_height * triangle_base) / 2

    triangle_perimeter = (triangle_side1 + triangle_side2 + triangle_side3)


    triangle_area = str(triangle_area)
    triangle_perimeter = str(triangle_perimeter)

    print("\nPerimeter of the triangle is " + triangle_perimeter + " cm")        
    print("Area of the triangle is " + triangle_area  + " cm^2" + "\n")

    global triangle_area_list
    global triangle_perimeter_list

    triangle_area_list.append(triangle_area)
    triangle_perimeter_list.append(triangle_perimeter)


    input("Press Enter to continue...")

            

def circle_calculation(): #calculates circle area and circumference and save answers into lists for later
    print("\nPlease enter all dimensions in cm \n")


    while True:  #checks for invalid input such as negative numbers and letters
        try:
            radius = float(input("Radius: "))
            if radius <= 0:
                print("Please enter a positive number")
                continue
            
            break
        except:
            print("Please only enter a number")

    circle_area = (radius * radius) * math.pi
    circumference = 2 * radius * math.pi

    circumference = str(circumference)
    circle_area = str(circle_area)

    print("\nThe circumference is " + circumference + " cm")
    print("Area of the circle is " + circle_area + " cm^2")

    global circle_area_list
    global circumference_list

    circle_area_list.append(circle_area)
    circumference_list.append(circumference)

    

    input("\nPress Enter to continue...")

def square_calculation(): #calculates square area and perimeter and save answers into lists for later
    print("Please enter all dimensions in cm \n")

    while True: #checks for invalid input such as negative numbers and letters
        try:
            square_side = float(input("Side: "))
            if square_side <= 0:
                print("Please enter a positive number")
                continue
            break
        except:
            print("Please only enter a number")

    square_area = square_side * square_side
    square_perimeter = square_side * 4

    square_area = str(square_area)
    square_perimeter = str(square_perimeter)

    print("\nPerimeter of the square is " + square_perimeter + " cm")        
    print("Area of the square is " + square_area + " cm^2")

    global square_area_list
    global square_perimeter_list

    square_area_list.append(square_area_list)
    square_perimeter_list.append(square_perimeter_list)

    
    input("Press Enter to continue...")

def rec_calculation(): #calculates rectangle area and perimeter and save answers into lists for later
    print("\nPlease enter all dimensions in cm \n")

    while True: #checks for invalid input such as negative numbers and letters
        try:
            rec_width = float(input("Width: "))
            if rec_width <= 0:
                print("Please enter a positive number")
                continue            
            rec_length = float(input("length: "))
            if rec_length <= 0:
                print("Please enter a positive number")
                continue
            break
        except:
            print("Please only enter a number")

    rec_area = rec_width * rec_length
    rec_perimeter = (rec_width + rec_length) * 2

    rec_area = str(rec_area)
    rec_perimeter = str(rec_perimeter)

    print("\nPerimeter of the rectangle is " + rec_perimeter + " cm")        
    print("Area of the rectangle is " + rec_area + " cm^2")

    global rectangle_area_list
    global rectangle_perimeter_list

    rectangle_area_list.append(rec_area)
    rectangle_perimeter_list.append(rec_perimeter)
    
    input("\nPress Enter to continue...")

def par_calculation(): #calculates parallelogram area and perimeter and save answers into lists for later
    print("\nPlease enter all dimensions in cm \n")

    while True: #checks for invalid input such as negative numbers and letters
        try:
            par_height = float(input("Height: "))
            if par_height <= 0:
                print("Please enter a positive number")
                continue            
            par_base = float(input("Base: "))
            if par_base <= 0:
                print("Please enter a positive number")
                continue
            break
        except:
            print("\nPlease only enter a number \n")

    par_area = par_height * par_base
    par_perimeter = (par_height + par_base) * 2

    par_area = str(par_area)
    par_perimeter = str(par_perimeter)

    print("\nPerimeter of the parallelogram is " + par_perimeter + " cm")        
    print("Area of the parallelogram is " + par_area + " cm^2")

    global parallelogram_area_list
    global parallelogram_perimeter_list

    parallelogram_perimeter_list.append(par_perimeter)
    parallelogram_area_list.append(par_area)

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

        if triangle_area_list:
            triangle_area_list = str(triangle_area_list)
            print("Answer history for triangle area " + triangle_area_list)
        else:
            print("There are no answers history for triangle area")

        if triangle_perimeter_list:
            triangle_perimeter_list = str(triangle_perimeter_list)
            print("Answer history for triangle perimeter " + triangle_perimeter_list)
        else:
            print("There are no answers history for triangle perimeter")
            
        if circle_area_list:
            circle_area_list = str(circle_area_list)
            print("Answer history for circle area " + circle_area_list)
        else:
            print("There are no answers history for circle area")
                    

        if circumference_list:
            circumference_list = str(circumference_list)
            print("Answer history for circle perimeter " + circumference_list)
        else:
            print("There are no answers history for circumference")

        if square_area_list:
            square_area_list = str(square_area_list)            
            print("Answer history for square area " + square_area_list)
        else:
            print("There are no answers history for square area")

        if square_perimeter_list:
            square_perimeter_list = str(square_perimeter_list)
            print("Answer history for sqaure perimeter " + square_perimeter_list)
        else:
            print("There are no answers history for square perimeter")
            

        if rectangle_area_list:
            rectangle_area_list = str(rectangle_area_list)
            print("Answer history for rectangle area " + rectangle_area_list)
        else:
            print("There are no answers history for rectangle area")    
        
        if rectangle_perimeter_list:
            rectangle_perimeter_list = str(rectangle_perimeter_list)
            print("Answer history for rectangle perimeter " + rectangle_perimeter_list)
        else:
            print("There are no answers history for rectangle perimeter")

        if parallelogram_area_list:
            parallelogram_area_list = str(parallelogram_area_list)
            print("Answer history for parallelogram area " + parallelogram_area_list)
        else:
            print("There are no answers history for parallelogram area")

        if parallelogram_perimeter_list:
            parallelogram_perimeter_list = str(parallelogram_perimeter_list)
            print("Answer history for parallelogram perimeter " + parallelogram_perimeter_list)
        else:
            print("There are no answers history for parallelogram perimeter")



        break

    else:
        print("\nChoice not found, please check your spelling")

        input("\nPress Enter to continue...")



