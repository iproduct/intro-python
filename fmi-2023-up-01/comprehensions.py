
if __name__ == '__main__':
    cars = [
      {'car': 'Ford', 'year': 2005},
      {'car': 'Mitsubishi', 'year': 2000},
      {'car': 'BMW', 'year': 2019},
      {'car': 'VW', 'year': 2011},
      {'car': 'VW', 'year': 2020}
    ]
    cars_dict = {item['car']: item['year'] for item in cars}
    print(cars_dict)
    cars_list = [item['car'] for item in cars]
    print(cars_list)
    cars_set = {item['car'] for item in cars}
    print(cars_set)
    cars_generator = ((item['car'], item['year']) for item in cars)
    print(cars_generator)
    for car in cars_generator:
        print(car)
