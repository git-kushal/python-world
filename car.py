class Car:

    def __init__(self,name,model,year):
        self.name=name
        self.model=model
        self.year=year

    def details(self):
        print(f"this car nameis {self.name},and it build in {self.year}year,the model is {self.model}")


