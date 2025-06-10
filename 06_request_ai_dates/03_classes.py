import os
os.system("cls")

class Car:
    # attributes
    description = "A four-wheeled road vehicle that is powered by an engine and is able to carry a small number of people."
    # constructor
    def __init__(self, mark, model, color) -> None:
        self.mark = mark
        self.model = model
        self.color = color
    
    def info(self):
        print("info:",self.mark, self.model, self.color)

    def start(self):
        print("Brmmm Brmmm!")

    
prado = Car(mark="Toyota",model="Prado",color="Grey")
prado.info()
prado.start()
print(prado.description)