car_types=["BMW","AUDI","TOYOTA","MERC","TATA","HONDA"]
print(car_types) #it print all the data storde in the list
print(len(car_types)) #it print the length of the data the stored
print(car_types[-4:])
print(car_types[2])

while True:
    a = input("Enter a car name (or 'quit' to exit): ")
    
    if a == "QUIT":
        print("Goodbye!")
        break
    elif a in car_types:
        print("Yes, this is already present!")
    else:
        car_types.append(a)
        print("----- Successfully Added -----")
        print(car_types)