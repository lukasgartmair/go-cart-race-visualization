import pygame

# class track
class track:
    
    def __init__(self, x ,y, mid_radius, colour):

            self.x = x
            self.y = y
            self.mid_radius = mid_radius
            self.colour = colour
            self.thickness = 5
            self.width = 30

    
    def draw_track(self, screen):
        # inner and outer radius

        pygame.draw.circle(screen, self.colour, (self.x, self.y),self.mid_radius+self.width,self.thickness)
        pygame.draw.circle(screen, self.colour, (self.x, self.y),self.mid_radius-self.width,self.thickness)
        # line
        #line(Surface, color, start_pos, end_pos, width=1) -> Rect
        # start finish line hor
        start =(self.x + self.mid_radius - self.width)
        end = (self.x + self.mid_radius + self.width)

        # horizontal

        for i in range(-9,9,3):
            pygame.draw.line(screen,(0,0,0),(start, self.y+i), (end, self.y+i),2)

        # start finish line ver
        start =(self.x + self.mid_radius - self.width)
        end = (self.x + self.mid_radius + self.width)
        # vertical
        for i in range(0,60,5):
            pygame.draw.line(screen,(0,0,0),(start+i, self.y+6), (start+i, self.y-9),2)

        
