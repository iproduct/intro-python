class Celsius:
    def __init__(self, temperature=0):
        self.temperature = temperature

    def to_fahrenheit(self):
        return (self.temperature * 1.8) + 32

    @property
    def temperature(self):
        print(f"Getting value: {self.__temperature}")
        return self.__temperature # private attribute = encapsulation

    @temperature.setter
    def temperature(self, value):
        if value < -273:  # validation
            raise ValueError("Temperature below -273 is not possible")
        print(f"Setting value: {value}")
        self.__temperature = value  # private attribute = encapsulation

    @temperature.deleter
    def temperature(self):
      del self.__temperature

if __name__ == '__main__':
    c = Celsius(300)
    # temp = c._Celsius__temperature;
    c.temperature -= 10;
    print(c.temperature)
    del c.temperature
    # print(c.temperature)
