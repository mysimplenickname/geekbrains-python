class Car:
    speed: int
    color: str
    name: str
    is_police: bool

    def __init__(self, user_speed: int, user_color: str, user_name: str, user_is_police: bool):
        self.speed = user_speed
        self.color = user_color
        self.name = user_name
        self.is_police = user_is_police

    def go(self):
        print(f"{self.name} drove off.")

    def stop(self):
        print(f"{self.name} stopped.")

    def turn(self, direction: str):
        if direction == "right" or direction == "left":
            print(f"{self.name} turned {direction}.")
        else:
            print(f"{self.name} did not turn because of unknown direction.")

    def show_speed(self):
        print(f"{self.name}'s speed is {self.speed}.")


class TownCar(Car):
    def show_speed(self):
        if self.speed > 60:
            print(f"{self.name}'s speed is more than allowed.")
        else:
            print(f"{self.name}'s speed is {self.speed}.")


class SportCar(Car):
    def go(self):
        print(f"You are driving the sport car. Be careful! {self.name} drove off.")


class WorkCar(Car):
    def show_speed(self):
        if self.speed > 40:
            print(f"{self.name}'s speed is more than allowed.")
        else:
            print(f"{self.name}'s speed is {self.speed}.")


class PoliceCar(Car):
    def go(self):
        print(f"Welcome officer. Have a nice day! {self.name} drove off.")


town_car = TownCar(50, "red", "Smart", False)
town_car.go()
town_car.show_speed()
town_car.turn("right")
town_car.stop()

print()

sport_car = SportCar(200, "yellow", "Lamborghini", False)
sport_car.go()
sport_car.show_speed()
sport_car.turn("")
sport_car.stop()

print()

work_car = WorkCar(60, "black", "Mercedes-Benz", False)
work_car.go()
work_car.show_speed()
work_car.turn("right")
work_car.stop()

print()

police_car = PoliceCar(80, "white", "Ford", True)
police_car.go()
police_car.show_speed()
police_car.turn("left")
police_car.stop()
