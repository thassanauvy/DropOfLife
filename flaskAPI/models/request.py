# flaskAPI/models/request.py
class Request:
    def __init__(self, requester, blood_type):
        self.requester = requester
        self.blood_type = blood_type