import time
import sys
import pygame

pygame.init()

background_colour = (234, 212, 252)

active_buttons = []
SCREEN_HEIGHT = 500
SCREEN_WIDTH = 800

screen = pygame.display.set_mode((800, 500))
pygame.display.set_caption('Akinator')
screen.fill(background_colour)
pygame.display.flip()

start_img = pygame.image.load('start_btn.png').convert_alpha()
exit_img = pygame.image.load('exit_btn.png').convert_alpha()
yes_img = pygame.image.load('yes_btn.png').convert_alpha()
no_img = pygame.image.load('no_btn.png').convert_alpha()

font = pygame.font.Font('font.ttf', 12)
font1 = pygame.font.Font('font.ttf', 20)
purple = (205,96,144)

class Button():
    def __init__(self, x, y, image, scale, value):
        width = image.get_width()
        height = image.get_height()
        self.image = pygame.transform.scale(image, (int(width * scale), int(height * scale)))
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)
        self.value = value

    def draw(self):
        action = False 
        screen.blit(self.image, (self.rect.x, self.rect.y))

    def contain(self, mouse):
        return self.rect.collidepoint(mouse)

def lbl(txt, speed=0.01):
    for char in txt:
        print(char, end='')
        sys.stdout.flush()
        time.sleep(speed)
    print('')

def textt(text, x, y):
    x = x
    y = y
    mes = font.render(text,True, purple)
    textRect = mes.get_rect()
    textRect.center = (x // 2, y // 2)
    screen.blit(mes, textRect)
    pygame.display.update()

def textt1(text, x, y):
    x = x
    y = y
    mes = font1.render(text,True, purple)
    textRect = mes.get_rect()
    textRect.center = (x // 2, y // 2)
    screen.blit(mes, textRect)
    pygame.display.update()  

questions = [
    "Is this person a woman?",
    "Is this person's hair long?",
    "Is this person's hair curly/wavy?",
    "Is this person a student?",
    "Does this person watch anime?",
    "Is this person kyrgyz?",
    "Does this person wear glasses?"
]


answer = []

def get_result(answers):
    print(answers)
    result = ""
    match answers:
        case [1, 1, 1, 1, 2, 1, 2]:
            result = "Aruuke."
        case [1, 1, 2, 1, 1, 1, 1]:
            result = "Adel."
        case [1, 1, 2, 1, 1, 2, 2]:
            result = "Sae Yeon."
        case [1, 1, 2, 1, 1, 1, 2]:
            result = "Aliia."
        case [1, 1, 2, 2, 2, 1, 2]:
            result = "miss Burul."
        case [1, 2, 1, 1, 2, 1, 2]:
            result = "Roza."
        case [1, 2, 2, 1, 1, 1, 2]:
            result = "Akylai."
        case [2, 2, 1, 1, 1, 1, 2]:
            result = "Abiy."
        case [2, 2, 2, 1, 1, 1, 2]:
            result = "Alymbek."
        case [2, 2, 2, 1, 2, 2, 1]:
            result = "Dovlyat."
        case [2, 2, 2, 2, 1, 2, 2]:
            result = "Ruslan Isaev."
        case [2, 2, 2, 1, 1, 1, 1]:
            result = "Kurstan."
        case [2, 2, 2, 1, 1, 2, 1]:
            result = "Erik."
        case [2, 2, 2, 2, 2, 1, 1]:
            result = "Zhumaniiaz Mamataliev."
        case _:
            textt1("Your person is too hard to guess.", 785, 410)
            textt1("Are you sure you answered correctly?", 785, 500)
    return f"We guess this person is {result}" if len(result) else ""


def state_screen(state):
    if state is None:
        active_buttons.clear()
        active_buttons.append(Button(150, 350, start_img, 0.6, 'start'))
        active_buttons.append(Button(500, 350, exit_img, 0.6, 'exit'))
        screen.fill(background_colour)
        textt1('Welcome to Akinator!', 780, 300)
        textt('Think about someone in COM. I will try to guess who is it :>', 785, 410)
        textt('Answer the questions with click on right answer', 785, 500)
    elif state < len(questions):
        active_buttons.clear()
        active_buttons.append(Button(150, 350, yes_img, 0.6, 1))
        active_buttons.append(Button(500, 350, no_img, 0.6, 2))
        screen.fill(background_colour)
        textt1(f'Question {state+1}/{len(questions)}', 780, 300)
        textt(questions[state], 785, 410)
    else:
        active_buttons.clear()
        active_buttons.append(Button(325, 350, start_img, 0.6, 'start'))
        screen.fill(background_colour)
        textt1('End', 780, 300)
        textt(get_result(answer), 785, 410)


def click_answer(response, state):
    if response == 'start':
        state = 0
        response = 0
        answer.clear()
    if response in [0, 1, 2]:
        if response > 0:
            answer.append(button.value)
            state = state + 1
        state_screen(state)
    return state

state = None

running = True
clock = pygame.time.Clock()
state_screen(state)
while running:
    # reduce frame rate FPS
    clock.tick(10)

    # draw active buttons
    for button in active_buttons:
        button.draw()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONUP:
            mouse_position = pygame.mouse.get_pos()
            for button in active_buttons:
                if button.contain(mouse_position):
                    if button.value == 'exit':
                        running = False
                        break
                    state = click_answer(button.value, state)
                    break
    pygame.display.update()

pygame.quit()