class Car():
    ''' a simple attempt to represent a car'''

    num_car = 0
    
    def __init__(self,make,model,year):
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading=0
        Car.num_car += 1

    def get_descriptive_name(self):
        long_name = str(self.year)+' '+self.make+self.model
        return long_name

    def read_odometer(self):
        print('this car had ' + str(self.odometer_reading)+ 'on it')

    def update_odometer(self,milage):
        if milage >= self.odometer_reading:
            self.odometer_reading = milage
        else:
            print('cannot rollback!')

    def fill_gas_tank(self):
        print('this car need a gas tank!!')

class ElectricCar(Car):
    '''aspects of a car ... specific to electric cars'''

    def __init__(self,make,model,year):
        super().__init__(make,model,year)
        self.battery_size = 50


    def describe_battery(self):
        print('this car has ' + str(self.battery_size)+ 'in it')

    def fill_gas_tank(self):
        print('this car doesnot need a gas tank!!')

my_tesla = ElectricCar('tesla','model X',2020)
print(my_tesla.get_descriptive_name())
my_tesla.describe_battery()
my_tesla.fill_gas_tank()

    
        
my_new_car = Car('suzuki','x series',2022)
print(my_new_car.get_descriptive_name())
my_new_car.read_odometer()
my_new_car.update_odometer(-100)
my_new_car.read_odometer()



