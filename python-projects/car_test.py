from car import Car

cars = []
with open("cars.txt") as file:
    for line in file:
        info = line.split()
        color = info[0]
        engine_type = info[1]
        gas_tank = int(info[2])
        odometer = int(info[3])
        car = Car(color, engine_type, gas_tank, odometer)
        cars.append(car)

car1 = cars[0]
car2 = cars[1]

print(car1)

print("Gas tank before driving:", car1.get_gas_tank())
print("Odometer before driving:", car1.get_odometer())
car1.drive()
print("Gas tank after driving:", car1.get_gas_tank())
print("Odometer after driving:", car1.get_odometer())

print(car2)

print("Gas tank before driving:", car2.get_gas_tank())
print("Odometer before driving:", car2.get_odometer())
car2.drive()
print("Gas tank after driving:", car2.get_gas_tank())
print("Odometer after driving:", car2.get_odometer())
