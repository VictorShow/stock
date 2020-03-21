from crime_map.service import Service
from crime_map.entity import Entity

class Controller:
    def __init__(self):
        self.s = Service()

    def pilice_pos(self):
        self.s.save_police_pos()

    def cctv_pop(self):
        self.s.save_cctv_pop()

    def police_norm(self):
        self.s.save_police_norm()

    def crime_map(self):
        self.s.draw_crime_map()
