# Ivy Tech - SDEV 140 - Introduction to Software Development
# Chapter 10 Exercise 2. Car Class
# Andrew M. Pierce  Associate of Applied Science - Software Development
# Python 3.8.6

import car


def main():
    carModel = input("Enter the make of the car: ")
    carYear = input("Enter the year the car was made: ")
    print(f'{carYear} {carModel}')
    user_car = car.Car(carYear, carModel)

    for i in range(5):
        user_car.accelerate()
        print(f'The {carModel} is going {user_car.get_speed()} mph.')

    for i in range(5):
        user_car.brake()
        print(f'The {carModel} is going {user_car.get_speed()} mph.')


if __name__ == "__main__":
    main()
