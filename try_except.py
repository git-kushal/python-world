while True:
    try:    
        a=int(input("enter a number: "))
        print(1/a)
    except TypeError:
        print("your typoe is wrong")
    except ValueError:
        print("valu is wrong")
    except Exception:
        print("something is worng")
