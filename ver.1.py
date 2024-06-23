import pygame  # Импорт библиотеки Pygame для создания игр
from random import randrange  # Импорт функции randrange из модуля random для генерации случайных чисел


RES = 800  # Размер игрового поля (800 пикселей)
SIZE = 40  # Размер ячейки (квадрата), из которого состоит змейка и яблоко

x, y = randrange(SIZE, RES - SIZE, SIZE), randrange(SIZE, RES - SIZE, SIZE)  # Начальные координаты головы змейки
apple = randrange(SIZE, RES - SIZE, SIZE), randrange(SIZE, RES - SIZE, SIZE)  # Начальные координаты яблока
length = 1  # Длина змейки (начальное значение)
snake = [(x, y)]  # Список координат сегментов змейки
dx, dy = 0, 0  # Направление движения змейки по осям x и y (начальное значение)
fps = 60  # Количество кадров в секунду
dirs = {'W': True, 'S': True, 'A': True, 'D': True, }  # Словарь для отслеживания разрешенных направлений движения
score = 0  # Счет игрока
speed_count, snake_speed = 0, 10  # Переменные для отслеживания скорости змейки

pygame.init()  # Инициализация Pygame
surface = pygame.display.set_mode([RES, RES])  # Создание игровой поверхности
clock = pygame.time.Clock()  # Создание объекта Clock для управления временем
font_score = pygame.font.SysFont('Arial', 26, bold=True)  # Задание параметров шрифта для отображения счета
font_end = pygame.font.SysFont('Arial', 78, bold=True)  # Задание параметров шрифта для отображения конечного экрана
img = pygame.image.load('m_m_1644009690_59-phonoteka-org-p-fon-dlya-prezentatsii-televizor-60 (1).png').convert()  # Загрузка изображения заднего фона

def close_game():  # Функция для закрытия игры при нажатии на крестик
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()

while True:  # Бесконечный игровой цикл
    surface.blit(img, (0, 0))  # Отображение заднего фона

    # Отрисовка сегментов змейки и яблока
    [pygame.draw.rect(surface, pygame.Color('green'), (i, j, SIZE - 1, SIZE - 1)) for i, j in snake]
    pygame.draw.rect(surface, pygame.Color('red'), (*apple, SIZE, SIZE))

    render_score = font_score.render(f'SCORE: {score}', 1, pygame.Color('orange'))  # Создание объекта для отображения счета
    surface.blit(render_score, (5, 5))  # Отображение счета на экране

    # Движение змейки
    speed_count += 1
    if not speed_count % snake_speed:
        x += dx * SIZE
        y += dy * SIZE
        snake.append((x, y))
        snake = snake[-length:]

    # Обработка поедания яблока
    if snake[-1] == apple:
        apple = randrange(SIZE, RES - SIZE, SIZE), randrange(SIZE, RES - SIZE, SIZE)
        length += 1
        score += 1
        snake_speed -= 1
        snake_speed = max(snake_speed, 4)

    # Обработка условий завершения игры (столкновение с границами или самой собой)
    if x < 0 or x > RES - SIZE or y < 0 or y > RES - SIZE or len(snake) != len(set(snake)):
        while True:
            render_end = font_end.render('GAME OVER', 1, pygame.Color('orange'))
            surface.blit(render_end, (RES // 2 - 200, RES // 3))
            pygame.display.flip()
            close_game()

    pygame.display.flip()  # Обновление экрана
    clock.tick(fps)  # Управление частотой кадров
    close_game()  # Проверка события закрытия окна

    # Обработка управления
    key = pygame.key.get_pressed()
    if key[pygame.K_w]:
        if dirs['W']:
            dx, dy = 0, -1
            dirs = {'W': True, 'S': False, 'A': True, 'D': True, }
    elif key[pygame.K_s]:
        if dirs['S']:
            dx, dy = 0, 1
            dirs = {'W': False, 'S': True, 'A': True, 'D': True, }
    elif key[pygame.K_a]:
        if dirs['A']:
            dx, dy = -1, 0
            dirs = {'W': True, 'S': True, 'A': True, 'D': False, }
    elif key[pygame.K_d]:
        if dirs['D']:
            dx, dy = 1, 0
            dirs = {'W': True, 'S': True, 'A': False, 'D': True, }




