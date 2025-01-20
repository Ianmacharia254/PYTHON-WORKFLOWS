try:
    file = open("myData.txt", "r")
    print(file.read())
except FileNotFoundError:  
    print("This file is not found") 
finally:
    print("Any statement")     