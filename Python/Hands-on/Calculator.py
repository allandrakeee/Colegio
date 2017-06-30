first_number = input("Enter first number: ")
operation = input("Type operation (+,-,/,*) ")
second_number = input("Enter second number: ")

if operation == "+" :
    total = int(first_number) + int(second_number)
    print("Total is {}".format(total))
elif operation == "-" :
    total = int(first_number) - int(second_number)
    print("Total is {}".format(total))    
elif operation == "/" :
    total = int(first_number) / int(second_number)
    print("Total is {}".format(total))    
elif operation == "*" :
    total = int(first_number) * int(second_number)
    print("Total is {}".format(total))    
