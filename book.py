class Book(object):
    def __init__(self):
        self.vehicles = []

    def add(self, car):
        self.vehicles.append(car)

    def drucken(self):
        for car in self.vehicles:
            car.display()

    def save_txt(self):

        text_file = open("Vehicle Manager.txt", "w")
        text_file.write("LIST OF CARS\n" + "\n")

        for car in self.vehicles:
            text_file.write("%s" % car + "\n")

        text_file.close()