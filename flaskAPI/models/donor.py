# flaskAPI/models/donor.py
class Donor:
    def __init__(self, name, blood_type):
        self.name = name
        self.blood_type = blood_type