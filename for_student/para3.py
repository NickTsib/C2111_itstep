import random

class Human:
    def __init__(self, name="Human", job=None, home=None, car=None):
        pass

    def get_home(self):
        pass

    def get_car(self):
        pass

    def get_job(self):
        pass

    def eat(self):
        pass

    def work(self):
        pass

    def shopping(self, manage):
        pass

    def chill(self):
        pass

    def clean_home(self):
        pass

    def to_repair(self):
        pass

    def day_indexes(self, day):
        day = f" Today the {day} of {self.name}'s life "
        print(f"{day:=^50}","\n")
        print(f"Money - {self.money}")
        print(f"Satiety - {self.satiety}")
        print(f"Gladness - {self.gladness}")
        home_indexes = "Home indexes"
        print(f"{home_indexes:^50}", "\n")
        print(f"Food - {self.home.food}")
        print(f"Mess - {self.home.mess}")
        car_indexes = f"{self.car.brand} car indexes"
        print(f"{car_indexes:^50}", "\n")
        print(f"Fuel - {self.car.fuel}")
        print(f"Strength - {self.car.strength}")

    def is_alive(self):
        pass

    def live(self, day):
        if self.is_alive(): # == False:
            return False
        if self.home is None:
            print("Settled in the house")
            self.get_home()
        if self.car is None:
            self.get_car()
            print(f"I bought a car {self.car.brand}")
        if self.job is None:
            self.get_job()
            print(f"I get a job {self.job.job} with salary {self.job.salary}")
        self.day_indexes(day)
        dice = random.randint(1, 4)
        if self.satiety < 20:
            print("I'll go eat")
            self.eat()
        elif self.gladness < 20:
            if self.home.mess > 15:
                print("I will clean house")
                self.clean_home()
            else:
                print("Let's chill!")
                self.chill()
        elif self.money < 0:
            print("Start working")
            self.work()
        elif self.car.strength < 15:
            print("I need repair my car")
            self.car.to_repair()
        elif dice == 1:
            print("Let's chill!")
            self.chill()
        elif dice == 2:
            print("Start working!")
            self.work()
        elif dice == 3:
            print("Cleaning time!")
            self.clean_home()
        elif dice == 4:
            print("Time to treats!")
            self.shopping(manage="delicacies")


class Auto:
    def __init__(self, brand_list):
        self.brand = random.choice(list(brand_list))
        self.fuel = brand_list[self.brand]["fuel"]
        self.strength = brand_list[self.brand]["strength"]
        self.consumption = brand_list[self.brand]["consumption"]

    def drive(self):
        if self.strength > 0 and self.fuel >= self.consumption:
            self.fuel -= self.consumption
            self.strength -= 1
            return True
        else:
            print("Car cannot move")
            return False


class House:
    def __init__(self):
        self.mess = 0
        self.food = 0


job_list = {
    "Java dev": {"salary": 50, "gladness_less": 10},
    "Python dev": {"salary": 40, "gladness_less": 3},
    "C++ dev": {"salary": 45, "gladness_less": 25},
    "Rust dev": {"salary": 70, "gladness_less": 1}
}

brands_of_car = {
    "BMW": {"fuel": 100, "strength": 50, "consumption": 12},
    "Fiat": {"fuel": 50, "strength": 40, "consumption": 10},
    "Volvo": {"fuel": 70, "strength": 150, "consumption": 8},
    "Ferrari": {"fuel": 80, "strength": 60, "consumption": 14}
}


class Job:
    def __init__(self, job_list):
        self.job = random.choice(list(job_list))
        self.salary = job_list[self.job]["salary"]
        self.gladness_less = job_list[self.job]["gladness_less"]


nick = Human(name="Vasya")

for day in range(1,8):
    if nick.live(day) == False:
        break
