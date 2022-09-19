def div(a, b):
    try:
        print(a//b)
    except:
         print("Error division by zero")


x = int(input("Enter number to dividend "))
y = int(input("Enter divisor "))
div(x, y)