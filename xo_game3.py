import pygame
import random
import sys
from typing import Any, List
import copy

TIP = 0
BREAKER = 0
ROZOVI = (189, 30, 128)
FIOLETOVI = (125, 81, 196)
NASROZOVI = (255, 20, 147)
ORHID = (138, 43, 226)
BLACK = (0, 0, 0)
WHITE = (200, 200, 200)
margine = 5
WINDOW_HEIGHT = 500 + margine * 11
WINDOW_WIDTH = 500 + margine * 11
mas: List[Any] = [[0] * 10 for i in range(10)]
query = 0
sys.setrecursionlimit(100000)
RES = WINDOW_WIDTH, WINDOW_HEIGHT
sc = pygame.display.set_mode(RES)
screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption("Crazy XO game! 5 = LOSE")
clock = pygame.time.Clock()


def main():
    """Запускает игру"""
    global screen, clock
    pygame.init()
    screen.fill(BLACK)

    while True:
        draw_grid()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        pygame.display.update()


def restart():
    """Перезапуск игры"""
    global mas, TIP, query
    query = 0
    TIP = 0
    mas = [[0] * 10 for _ in range(10)]
    main()


def break_lose():
    """Завершает рекурсию"""
    win_gratz('o')


def win_gratz(sign):
    """Отрисовка победного экрана"""
    while True:
        sc.fill(BLACK)
        font = pygame.font.SysFont('Calibri', 45)
        if sign == 'xo':
            text1 = font.render(f'Wow! Draw! [Press Q to Exit]', True, WHITE, 5)
        else:
            text1 = font.render(f'{sign.upper()} Lose [Press Q to Exit]', True, WHITE, 5)
        text2 = font.render(f'[R to Restart]', True, WHITE, 5)
        text_rect = text1.get_rect()
        text_x = sc.get_width() / 2 - text_rect.width / 2
        text_y = sc.get_height() / 2 - text_rect.height / 2
        sc.blit(text1, [text_x, text_y - 30])
        sc.blit(text2, [text_x + 75, text_y + 150])
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_q:
                    sys.exit()
                if event.key == pygame.K_r:
                    restart()
        pygame.display.update()


def check_draw():
    """Проверка ничьи"""
    global mas
    x, o = 0, 0
    for i in mas:
        for j in i:
            if j == 0:
                break
            elif j == 'x':
                x += 1
            elif j == 'o':
                o += 1
    if x == 50 and o == 50:
        win_gratz('xo')


def check_win(col, row, sign):
    """Проверка победы по горизонтали"""
    schet = 0
    n = col
    j = 0
    while j < 4:
        i = -4 + j
        while i < 5:
            if i + j + n < 0:
                i += 1
                continue
            try:
                if mas[n + i + j][row] == sign:
                    schet += 1
                if schet > 4:
                    win_gratz(sign)
                elif mas[n + i][row] != sign:
                    schet = 0
                i += 1
            except IndexError:
                i += 1
                continue
        schet = 0
        j += 1


def check_win2(col, row, sign):
    """Проверка победы по вертикали"""
    schet = 0
    n = row
    j = 0
    while j < 4:
        i = -4 + j
        while i < 4:
            if i + j + n < 0:
                i += 1
                continue
            try:
                if mas[col][n + i + j] == sign:
                    schet += 1
                if schet > 4:
                    win_gratz(sign)
                elif mas[col][n + i + j] != sign:
                    schet = 0
                i += 1
            except IndexError:
                i += 1
                continue
        schet = 0
        j += 1


def check_win3(col, row, sign):
    """Проверка победы по диагонали(from Left to Right)"""
    schet = 0
    n = col
    k = row
    j = 0
    while j < 4:
        i = -4 + j
        while i < 4:
            if i + j + n < 0:
                i += 1
                continue
            try:
                if mas[n + i + j][k + i + j] == sign:
                    schet += 1
                if schet > 4:
                    win_gratz(sign)
                elif mas[n + i + j][k + i + j] != sign:
                    schet = 0
                i += 1
            except IndexError:
                i += 1
                continue
        schet = 0
        j += 1


def check_win4(col, row, sign):
    """Проверка победы по диагонали(from Right to Left)"""
    schet = 0
    n = col
    k = row
    p = -1
    j = 0
    while j < 4:
        i = -4 + j
        while i < 4:
            if i * p + j * p + n < 0:
                i += 1
                continue
            try:
                if mas[n + i * p + j * p][k + i + j] == sign:
                    schet += 1
                if schet > 4:
                    win_gratz(sign)
                elif mas[n + i * p + j * p][k + i + j] != sign:
                    schet = 0
                i += 1
            except IndexError:
                i += 1
                continue
        schet = 0
        j += 1


def check_lose(col, row, sign, copy_mas):
    """Проверка хода PC по горизонтали"""
    global TIP
    schet = 0
    n = col
    j = 0
    while j < 4:
        i = -4 + j
        while i < 5:
            if i + j + n < 0:
                i += 1
                continue
            try:
                if copy_mas[n + i + j][row] == sign:
                    schet += 1
                if schet > 4:
                    TIP += 1
                    random_pos()
                    break
                elif copy_mas[n + i][row] != sign:
                    schet = 0
                i += 1
            except IndexError:
                i += 1
                continue
        if schet > 4:
            break
        schet = 0
        j += 1


def check_lose2(col, row, sign, copy_mas):
    """Проверка хода PC по вертикали"""
    global TIP
    schet = 0
    n = row
    j = 0
    while j < 4:
        i = -4 + j
        while i < 4:
            if i + j + n < 0:
                i += 1
                continue
            try:
                if copy_mas[col][n + i + j] == sign:
                    schet += 1
                if schet > 4:
                    TIP += 1
                    random_pos()
                    break
                elif copy_mas[col][n + i + j] != sign:
                    schet = 0
                i += 1
            except IndexError:
                i += 1
                continue
        if schet > 4:
            break
        schet = 0
        j += 1


def check_lose3(col, row, sign, copy_mas):
    """Проверка хода PC по диагонали(from Left to Right)"""
    global TIP
    schet = 0
    n = col
    k = row
    j = 0
    while j < 4:
        i = -4 + j
        while i < 4:
            if i + j + n < 0:
                i += 1
                continue
            try:
                if copy_mas[n + i + j][k + i + j] == sign:
                    schet += 1
                if schet > 4:
                    TIP += 1
                    random_pos()
                    break
                elif copy_mas[n + i + j][k + i + j] != sign:
                    schet = 0
                i += 1
            except IndexError:
                i += 1
                continue
        if schet > 4:
            break
        schet = 0
        j += 1


def check_lose4(col, row, sign, copy_mas):
    """Проверка хода PC по диагонали(from Right to Left)"""
    global TIP
    schet = 0
    n = col
    k = row
    p = -1
    j = 0
    while j < 4:
        i = -4 + j
        while i < 4:
            if i * p + j * p + n < 0:
                i += 1
                continue
            try:
                if copy_mas[n + i * p + j * p][k + i + j] == sign:
                    schet += 1
                if schet > 4:
                    TIP += 1
                    random_pos()
                    break
                elif copy_mas[n + i * p + j * p][k + i + j] != sign:
                    schet = 0
                i += 1
            except IndexError:
                i += 1
                continue
        if schet > 4:
            break
        schet = 0
        j += 1


def random_pos():
    """Поиск и выбор хода компьютера"""
    global query, BREAKER
    BREAKER += 1
    if BREAKER < 2000:
        blocksize = 50
        comp_x = random.randint(0, 510)
        comp_y = random.randint(0, 510)
        col = comp_x // (blocksize + margine)
        row = comp_y // (blocksize + margine)
        copy_mas = copy.deepcopy(mas)
        if copy_mas[col][row] == 0:
            if TIP < 200 and query % 2 != 0:
                copy_mas[col][row] = 'o'
                check_lose(col, row, 'o', copy_mas)
                if query % 2 != 0:
                    check_lose2(col, row, 'o', copy_mas)
                if query % 2 != 0:
                    check_lose3(col, row, 'o', copy_mas)
                if query % 2 != 0:
                    check_lose4(col, row, 'o', copy_mas)
                if mas[col][row] == 0 and query % 2 != 0:
                    mas[col][row] = 'o'
                    check_win(col, row, 'o')
                    check_win2(col, row, 'o')
                    check_win3(col, row, 'o')
                    check_win4(col, row, 'o')
                    check_draw()
                    query += 1
        else:
            random_pos()
    else:
        break_lose()


def computer_turn():
    """Ход компьютера"""
    random_pos()


def draw_grid():
    """Отрисовка сетки и X O"""
    global query
    blocksize = 50
    for x in range(0, WINDOW_WIDTH, blocksize):
        for y in range(0, WINDOW_HEIGHT, blocksize):
            rect = pygame.Rect(x, y, blocksize, blocksize)
            pygame.draw.rect(screen, WHITE, rect, 1)
    for event in pygame.event.get():
        if event.type == pygame.MOUSEBUTTONDOWN and query % 2 == 0:
            x_mouse, y_mouse = pygame.mouse.get_pos()
            col = x_mouse // (blocksize + margine)
            row = y_mouse // (blocksize + margine)
            if mas[col][row] == 0:
                if query % 2 == 0:
                    mas[col][row] = 'x'
                    check_win(col, row, 'x')
                    check_win2(col, row, 'x')
                    check_win3(col, row, 'x')
                    check_win4(col, row, 'x')
                    check_draw()
                query += 1
        elif query % 2 != 0:
            computer_turn()

    for row in range(10):
        for col in range(10):
            if mas[col][row] == 'x':
                color = FIOLETOVI
            elif mas[col][row] == 'o':
                color = ROZOVI
            else:
                color = WHITE
            x = col * blocksize + (col + 1) * margine
            y = row * blocksize + (row + 1) * margine
            pygame.draw.rect(sc, color, (x, y, blocksize, blocksize))
            if color == FIOLETOVI:
                pygame.draw.line(sc, NASROZOVI, (x + 10, y + 10), (x + blocksize - 10, y + blocksize - 10), 5)
                pygame.draw.line(sc, NASROZOVI, (x + blocksize - 10, y + 10), (x + 10, y + blocksize - 10), 5)
            elif color == ROZOVI:
                pygame.draw.circle(sc, ORHID, (x + blocksize // 2, y + blocksize // 2), blocksize // 2 - 5, 5)


if __name__ == '__main__':
    main()
