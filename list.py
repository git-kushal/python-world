car_types=["BMW","AUDI","TOYOTA","MERC","TATA","HONDA"]
print(car_types) #it print all the data storde in the list
print(len(car_types)) #it print the length of the data the stored
print(car_types[-4:])
print(car_types[2])
a= "AUTO"
if a in car_types:
    print("yes this is present")
else:
    car_types.append(a)
    print("-----succesfuly added-----")
    print(car_types)