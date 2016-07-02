# class race car
import pygame
import math

class race_car:
    
    def __init__(self, driver, x, y, size, colour, lap_times, dist):

        self.x = x

        self.y = y

        # square cars
        self.width = size
        self.height = size
        self.driver = driver
        self.colour = colour

        self.lap_times = lap_times
        self.dist = dist
        self.angle = 0
        self.lap_counter = 0
        self.total_time = 0
        self.rank = 0
        self.covered_distance = 0
         
    def draw_car(self, screen):
        # the position argument is left dist (x), top dist (y), width of rect and height of rect)
        # last digit is zero to fill it
        pygame.draw.rect(screen, self.colour , (self.x,self.y,self.width,self.height), 0)

    def get_omega(self, lap_time):

        # calculate new position out of laptime and track length
        # on the circle
        # je größer die laptime umso kleiner ist der winkel, der zurückgelegt wird.
        omega = 2*math.pi*(1/lap_time)

        return omega

        # winkelgeschwindigkeit!
##    Formel: ω = 2 · π · f
##    "ω" ist die Kreisfrequenz pro Sekunde [ 1/s ]
##    "π" ist die Kreiszahl, π=3,14159
##    "f" ist die Frequenz pro Sekunde [ 1/s ]
        # wenn ein umlauf ca. 30 sekunden dauert, dann ist die frequenz laut dreisatz ca.: 1/30s = 0,03333

    def move(self, angle,  mid_radius_of_track, center_of_track, dist):

        self.x = (center_of_track[0] + dist + math.cos(angle)*(mid_radius_of_track*2))
        self.y = (center_of_track[1] + dist + math.sin(angle)*(mid_radius_of_track*2))


    def get_distance(self, angle, circumference):

        ratio = angle/(2*math.pi)

        distance = circumference * ratio

        return distance

        

