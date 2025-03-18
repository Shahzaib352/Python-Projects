# Calculator
def sum():
    num1= int(input("Enter a number: "))
    num2= int(input("Enter a number: "))
    return print(num1 + num2)

def sub():
    num1= int(input("Enter a number: "))
    num2= int(input("Enter a number: "))
    return print(num1 - num2)

def pro():
    num1= int(input("Enter a number: "))
    num2= int(input("Enter a number: "))
    return print(num1 * num2)

def div():
    num1= int(input("Enter a number: "))
    num2= int(input("Enter a number: "))
    if (num2 != 0):
        return print(num1 / num2)
    else:
        print("Infinite")
        
def sqr():
    num= int(input("Enter a number: "))
    return print(num**2)

def cube():
    num= int(input("Enter a number: "))
    return print(num**3)

def sqr_root():
    num= int(input("Enter a number: "))
    return print(num**0.5)

def to_the_power():
    num= int(input("Enter a number: "))
    power= int(input("Enter a power: "))
    return print(num ** power)

if __name__ == "__main__": # code below can not be used anywhere else
    while True:
        print("1 for Sum     2 for Subtract   3 for Divide        4 for Multiplication ")
        print("5 for Cube    6 for Square     7 for Square root   8 for number of power")
        print("9 to exit")
        operation = int(input("Chose an operation: "))
        match operation:
            case 1:
                sum()
            case 2:
                sub()
            case 3:
                div()
            case 4:
                pro()
            case 5:
                cube()
            case 6:
                sqr()
            case 7:
                sqr_root()
            case 8:
                to_the_power()
        if ( operation  == 9):
            print("Exited.")
            break 
        
