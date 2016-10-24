class Vehicle(object):
    def __init__(self, brand, model, km_done, service_date):
        self.brand = brand
        self.model = model
        self.km_done = km_done
        self.service_date = service_date

    def display(self):
        item = "Brand: %s; Model: %s; Km_done: %s; Service_date: %s " % (self.brand, self.model, self.km_done, self.service_date)
        print item

    def modif_km(self, new_km):
        self.km_done = new_km

    def edit_service(self, new_service):
        self.service_date = new_service

