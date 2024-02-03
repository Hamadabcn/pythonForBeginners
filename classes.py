class Vehicle:
    def __init__(self, make, model):
        self.make = make
        self.model = model
        
    def moves(self):
        print("Moves Along. . .")
        
    def get_make_model(self):
        print(f"I'm a {self.make} {self.model}.")
        
my_car = Vehicle('Mercedes', 'G Class')

#print(my_car.make)
#print(my_car.model)
my_car.get_make_model()
my_car.moves()

your_car = Vehicle('BMW', 'M-4')
your_car.get_make_model()
your_car.moves()

his_car = Vehicle('SEAT', 'IBIZA')
his_car.get_make_model()
his_car.moves()

yassin_car = Vehicle('FERRARI', '488 Pista')
yassin_car.get_make_model()
yassin_car.moves()


class Airplane(Vehicle):
    def __init__(self, make, model, faa_id):
        super().__init__(make, model)
        self.faa_id = faa_id
        
    def moves(self):
        print("Flies Along. . .")
        
class Truck(Vehicle):
    def moves(self):
        print("Rumbles Along. . .")
        
class GolfCart(Vehicle):
        pass
    
airbus = Airplane('Airbus', 'A 380', 'N-123456789')
man = Truck('MAN', 'TGX')
golfwagon = GolfCart('Yamaha', 'GC-100')

airbus.get_make_model()
airbus.moves()

man.get_make_model()
man.moves()

golfwagon.get_make_model()
golfwagon.moves()

print("\n\n")

for v in (my_car, your_car, his_car, yassin_car, airbus, man, golfwagon):
    v.get_make_model()
    v.moves()
    