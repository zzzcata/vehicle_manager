from book import Book
from vehicle import Vehicle

my_vehicle_book = Book()

car1 = Vehicle(brand="VW", model="Golf", km_done=100, service_date="10.07.2016")
my_vehicle_book.add(car1)

car2 = Vehicle(brand="Audi", model="A4", km_done=70, service_date="13.06.2016")
my_vehicle_book.add(car2)

my_vehicle_book.drucken()

print "------------------"

car1.modif_km(678)
car1.display()

car2.edit_service("11.03.2015")
car2.display()

my_vehicle_book.save_txt()