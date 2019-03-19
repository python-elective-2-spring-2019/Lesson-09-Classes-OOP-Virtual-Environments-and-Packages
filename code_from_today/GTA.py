from car import Car
from attributes import Engine
from attributes import Pedal
from attributes import A
import attributes

def main():

    try:
        bmw = Car(Engine())
        bmw.run()

        triumph = Car(A())
        triumph.run()
    except AttributeError:
        print('This car will never run!!')

        #print(sorted(attributes.__dict__))


if __name__ == "__main__":
    main()