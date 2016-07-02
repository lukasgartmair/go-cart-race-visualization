# -*- coding: utf-8 -*-
"""
Created on Jul  26 2015

@author: Lukas Gartmair
"""

import pygame
import math
from ClassTrack import *
from ClassRaceCar import *
from ClassLegend import *
from TXT import *
from GETCURRENTRANKING import *
import time

pygame.init()
# screen
background_colour = (225,225,225)
width = 800
height = 800
screen = pygame.display.set_mode([width, height])
pygame.display.set_caption('Race')

all_race_cars = []

# colours

colour_car_1 = (255,0,0)
colour_car_2 = (0,255,0)
colour_car_3 = (0,0,255)
colour_car_4 = (255,255,0)
colour_car_5 = (0,255,255)
colour_car_6 = (255,0,255)
colour_car_7 = (100,100,100)
colour_car_8 = (0,100,100)

# new track

mid_radius_of_track = 150
center_of_track =(width/2, height/2)
track = track(int(width/2),int(height/2),mid_radius_of_track*2,(0,0,0))
# circumference of  the circle track

circumference = 2*math.pi*mid_radius_of_track

# lap times
# get laptimesTraceback (most recent call last):

lap_times = []
lap_times = LoadRaceStats()

number_of_laps = len(lap_times[0])

lap_times_car_1 = lap_times[1]
lap_times_car_2 = lap_times[2]
lap_times_car_3 = lap_times[3]
lap_times_car_4 = lap_times[4]
lap_times_car_5 = lap_times[5]
lap_times_car_6 = lap_times[6]
lap_times_car_7 = lap_times[7]
lap_times_car_8 = lap_times[8]

# introduce cars
car_1 = race_car('Lewis Hamilton' , 150,50, 15, colour_car_1, lap_times_car_1, 1)
all_race_cars.append(car_1)

car_2 = race_car('Nico Rosberg', 150,50, 15, colour_car_2, lap_times_car_2, -1)
all_race_cars.append(car_2)

car_3 = race_car('Sebastian Vettel',150,50, 15, colour_car_3, lap_times_car_3, -1)
all_race_cars.append(car_3)

car_4 = race_car('Kimi Raikoennen', 150,50, 15, colour_car_4, lap_times_car_4, 1)
all_race_cars.append(car_4)

car_5 = race_car('Valteri Bottas', 150,50, 15, colour_car_5, lap_times_car_5, -1)
all_race_cars.append(car_5)

car_6 = race_car('Felipe Massa' , 150,50, 15, colour_car_6, lap_times_car_6, -1)
all_race_cars.append(car_6)

car_7 = race_car('Niko Huelkenberg' , 150,50, 15, colour_car_7, lap_times_car_7, 1)
all_race_cars.append(car_7)

car_8 = race_car('Sergio Perez', 150,50, 15, colour_car_8, lap_times_car_8, -1)
all_race_cars.append(car_8)


## main structure

angle = 0

race_flags_img = pygame.image.load('race_flags_small.jpg')

print('Let"s go ' + str(number_of_laps) + ' laps to go!')

### motion speed ca. 500 is ok the higher the valuE the slower
motion_speed = 35

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    screen.fill(background_colour)

    # display cars
    for (x,car) in enumerate(all_race_cars):
        omega_temp = 0
    # define circle angle area
        omega_temp = car.get_omega(car.lap_times[car.lap_counter]*motion_speed)

        car.angle = car.angle + omega_temp

        if car.angle <= 2*math.pi:
            car.move(car.angle, mid_radius_of_track, center_of_track, car.dist)
        if car.angle >= 2*math.pi:
            # add the lap time to the total time
            car.total_time += car.lap_times[car.lap_counter]
        # add 1 to the individual lap counter
            car.lap_counter += 1
##            if car == all_race_cars[0]:
##                print(car.lap_counter)
            # start from beginning after each turn
            car.angle = 0

        ### sum up the covered distance
        car.covered_distance += car.get_distance(car.angle, circumference)


        car.draw_car(screen)

        # finish
        if car.lap_counter >= len(car.lap_times):
            print('Congratulations to car ' + str(x+1) + ' ! Nice Race!') 
            running = False

    # get the current ranking from summed up laptimes

    #GetCurrentRanking(all_race_cars)
    # show the track

    track.draw_track(screen)

    # show legend
    
    legend = Legend(width/4 + 25, height/4+30)
    legend.draw_legend(screen, all_race_cars)

    # show race flags
    screen.blit(race_flags_img,(width/2-70,height/1.5))

    # show lap
    font = pygame.font.Font(None, 70)
    text = font.render(str(all_race_cars[0].lap_counter) + ' / 52', 1, (10, 10, 10)) # (tupel ) 0 colour
    textpos = (20,60)
    screen.blit(text, textpos)
    
    text_lap = font.render( 'Lap #', 1, (10, 10, 10)) # (tupel ) 0 colour
    textpos_lap = (10,10)
    screen.blit(text_lap, textpos_lap)

    pygame.display.flip()








        
