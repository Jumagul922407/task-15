# oop_example.py

class Car:
    def __init__(self, brand, color):
        self.brand = brand
        self.color = color

    def drive(self):
        print(f"{self.color} {self.brand} машина айдап жатат.")

# Объект түзөбүз
car1 = Car("Toyota", "кызыл")
car2 = Car("BMW", "кара")

car1.drive()
car2.drive()
