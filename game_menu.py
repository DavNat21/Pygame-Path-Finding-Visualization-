import string
from xmlrpc.client import Boolean
import pygame as pg
pg.init()

YELLOW = (204,204,0)
BLACK = (0,0,0)
WHITE = (255,255,255)
text_1 = 'Game Menu'
text_2 = 'Movement Type'
text_3 = 'Heuristics'
screen = pg.display.set_mode((640,640))
screen.fill(BLACK)

def set_mainmenu():
    font = pg.font.Font(None, 50)
    size = font.size(text_1)
    color = WHITE

    menu_render = font.render(text_1,1,color,BLACK)
    menu_rect = screen.blit(menu_render,(50,50))

    Move_render = font.render(text_2,1,color,BLACK)
    Move_rect = screen.blit(Move_render, (50, 2*50 + size[1]))

    heur_render = font.render(text_3,1,color,BLACK)
    heur_rect = screen.blit(heur_render, (50, 3*50+2*size[1]))

    return menu_rect, Move_rect, heur_rect, size

def set_heurmenu():
    text_1 = 'Heuristics Options'
    text_2 = 'Manhattan distance'
    text_3 = 'Diagonal distance'
    font = pg.font.Font(None, 50)
    
    size = font.size(text_1)
    color = WHITE

    menu_render = font.render(text_1,1,color,BLACK)
    menu_rect = screen.blit(menu_render,(50,50))

    Move_render = font.render(text_2,1,color,BLACK)
    Move_rect = screen.blit(Move_render, (50, 2*50 + size[1]))

    heur_render = font.render(text_3,1,color,BLACK)
    heur_rect = screen.blit(heur_render, (50, 3*50+2*size[1]))





def update_collision(rect:pg.Rect, text:string):
    font = pg.font.Font(None,50)
    size = font.size(text)
    x,y = rect[0], rect[1]
    color = YELLOW
    
    render = font.render(text,1, YELLOW,BLACK)
    screen.blit(render, (x,y))


    

menu_rect, move_rect, heur_rect, size = set_mainmenu()


pg.display.flip()
while True:
    # use event.wait to keep from polling 100% cpu
    mouse_pos = pg.mouse.get_pos()

    if move_rect.collidepoint(mouse_pos[0],mouse_pos[1]):

        update_collision(move_rect, text_2)
    elif heur_rect.collidepoint(mouse_pos[0], mouse_pos[1]):
        update_collision(heur_rect, text_3)
    else:
        set_mainmenu()
    
    if move_rect.collidepoint(mouse_pos[0],mouse_pos[1]) and pg.mouse.get_pressed()[0]:
        
        set_heurmenu()
        


    if pg.event.wait().type == pg.QUIT:
        break
    pg.display.update()
pg.quit()
