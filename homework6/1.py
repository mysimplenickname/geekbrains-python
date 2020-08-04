from time import sleep


class TrafficLight:
    __color = {"red": 7, "yellow": 2, "green": 5}

    def running(self):
        print("The traffic light is working now.")
        while True:
            for key, value in self.__color.items():
                print(f"The color is {key} now.")
                sleep(value)


traffic_light = TrafficLight()
traffic_light.running()
