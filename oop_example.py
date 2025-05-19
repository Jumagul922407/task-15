class Car:
    """
    Машина классы.
    Атрибуттар:
    - brand: Машинанын бренди
    - color: Машинанын түсү
    """

    def _init_(self, brand, color):
        self.brand = brand
        self.color = color

    def drive(self):
        """Машина айдап жатат деген билдирүү чыгарат."""
        print(f"{self.color} {self.brand} машина айдап жатат.")

    def stop(self):
        """Машина токтоду деген билдирүү чыгарат."""
        print(f"{self.color} {self.brand} машина токтоду.")

    def accelerate(self):
        """Машина ылдамдап жатат деген билдирүү чыгарат."""
        print(f"{self.color} {self.brand} машина ылдамдап жатат.")


Объект түзүү жана методдорду чакыруу
car1 = Car("Toyota", "Кызыл")
car2 = Car("BMW", "Кара")
car1.drive()
car1.accelerate()
car1.stop()

print()  # бош катар

car2.drive()
car2.accelerate()
car2.stop()


---

Эми бул файлды сактап, иштетсең төмөнкүдөй натыйжа чыгат:


Кызыл Toyota машина айдап жатат.
Кызыл Toyota машина ылдамдап жатат.
Кызыл Toyota машина токтоду.

Кара BMW машина айдап жатат.
Кара BMW машина ылдамдап жатат.
Кара BMW машина токтоду.
