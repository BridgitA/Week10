maximum_order = 150.00
minimum_order = 5.00


def cheese_program(order_amount):
    if order_amount.isdigit() == False:
        print("Enter a numeric value")
    elif float(order_amount) > maximum_order:
        print(order_amount, "is more than currently available stock") 
    elif float(order_amount) < minimum_order:
        print(order_amount, "is less than currently available stock")
    elif (float(order_amount)<= maximum_order) and (float(order_amount)>= minimum_order):  
        print(order_amount, "pounds costs", int(order_amount) * 5)
    else:
        print("Enter numeric value")             
weight = input("Enter cheese order weight (pounds numeric value): ")
function = cheese_program(weight)