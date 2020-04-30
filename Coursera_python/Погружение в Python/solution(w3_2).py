import csv
import os


class CarBase:
    def __init__(self, brand, photo_file_name, carrying):
        self.brand = brand
        self.photo_file_name = photo_file_name
        self.carrying = float(carrying)
        pass

    def get_photo_file_ext(self, photo_file_name=None):
        try:
            ending = os.path.splitext(self.photo_file_name)
            if ending[1] in ['.jpg', '.jpeg', '.png', '.gif']:
                return str(ending[1])
        except:
            return None


class Car(CarBase):
    def __init__(self, brand, photo_file_name, carrying, passenger_seats_count):
        super().__init__(brand, photo_file_name, carrying)
        self.passenger_seats_count = int(passenger_seats_count)
        self.car_type = 'car'


def validate(body_whl):
    return body_whl.count('x') != 2


class Truck(CarBase):

    def __init__(self, brand, photo_file_name, carrying, body_whl):
        super().__init__(brand, photo_file_name, carrying)
        self.body_whl = body_whl
        self.car_type = 'truck'

        try:
            self.body_length = float(body_whl.split(sep='x')[0])
            self.body_width = float(body_whl.split(sep='x')[1])
            self.body_height = float(body_whl.split(sep='x')[2])
            if validate(body_whl):
                self.body_length = 0.0
                self.body_width = 0.0
                self.body_height = 0.0
        except (ValueError, IndexError, AttributeError):
            self.body_length = 0.0
            self.body_width = 0.0
            self.body_height = 0.0

    def get_body_volume(self):
        return self.body_length * self.body_width * self.body_height


class SpecMachine(CarBase):
    def __init__(self, brand, photo_file_name, carrying, extra):
        super().__init__(brand, photo_file_name, carrying)
        self.extra = str(extra)
        self.car_type = 'spec_machine'


def valid_end(ending):
    ending = os.path.splitext(ending)
    if ending[1] in ['.jpg', '.jpeg', '.png', '.gif']:
        return True
    else:
        return False


def get_car_list(csv_filename):
    car_list = []
    with open(csv_filename) as csv_fd:
        reader = csv.reader(csv_fd, delimiter=';')
        next(reader)  # пропускаем заголовок
        for row in reader:
            try:
                if row[0] and row[1] and row[3] and row[5] and valid_end(row[3]):
                    if row[0] == 'truck':
                        truck = Truck(row[1], row[3], row[5], row[4])
                        car_list.append(truck)
                    elif row[0] == 'car':
                        car = Car(row[1], row[3], row[5], row[2])
                        car_list.append(car)
                    elif row[0] == 'spec_machine' and row[6]:
                        spec_machine = SpecMachine(row[1], row[3], row[5], row[6])
                        car_list.append(spec_machine)
                else:
                    continue
            except:
                continue
    return car_list


if __name__ == '__main__':
    listcar = get_car_list("cars_week3.csv")
    # print(listcar)
    print(len(listcar))
    for car in listcar:
        # print(type(car))
        print(car.brand)
        try:
            print(car.body_whl)
            print(car.body_height, car.body_width, car.body_length, sep='\n')
        except:
            continue
