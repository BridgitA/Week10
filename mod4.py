def str_analysis(string):
    while string.lower() == "":
        string = input("Enter a word or interger: ")
    else: 
        if string.lower().isdigit(): 
            if int(string) > 100:
                print("This is a big number")
            elif int(string) < 100:
                print("This is a smaller number than expected")
        elif string.lower().isalpha():
            print("This string is all alphabetic")
        else:
            print("This string contains multiple character types")
str_analysis(input("Enter a word or interger: "))                        

