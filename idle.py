car_types=["BMW","AUDI","TOYOTA","MERC","TATA","HONDA"]
a=input("enter the name you want to find= ")

if a in car_types:
    print("yes this is present")
else:
   car_types.append(a)
   print(car_types)
