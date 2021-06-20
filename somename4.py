class Car(object):
    def __init__(self,model,color):
        self.model = model
        self.color = color
    def start(self):
        print("START")
    def stop(self,time):
        print("STOP", time)
car = Car("circle","blue")
print(car.model)
print(car.color)
car.start()
car.stop(20)