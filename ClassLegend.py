import pygame 
class Legend:
    def __init__(self, x ,y):

            self.x = x
            self.y = y
            self.thickness = 3

    def draw_legend(self, screen, all_race_cars):
            #legend
    ##    # Display some text
    ##	font = pygame.font.Font(None, 36)
    ##	text = font.render("Hello There", 1, (10, 10, 10))
    ##	textpos = text.get_rect()
        font = pygame.font.Font(None, 36)
        
        legend_x = self.x
        legend_y = self.y
        legend_width = 350
        legend_height = 270
        legend_thickness = self.thickness
        
        pygame.draw.rect(screen, (0,0,0), (legend_x, legend_y,legend_width, legend_height), legend_thickness)

        shifter_y = 25
        shifter_x = 60

        
        for (x,car) in enumerate(all_race_cars):
            
            pygame.draw.rect(screen, (car.colour), (legend_x + legend_thickness + 2 ,legend_y + shifter_y ,20,20), 0)
            text = font.render( str(car.driver), 1, (10, 10, 10)) # (tupel ) 0 colour
            textpos = (legend_x + legend_thickness + 2 + shifter_x ,legend_y + shifter_y)
            screen.blit(text, textpos)

            shifter_y += 25

