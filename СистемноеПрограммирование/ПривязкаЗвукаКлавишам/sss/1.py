import pyaudio as pa
import pygame

# ... место для предыдущего кода ...

# наши клавиши
key_names = ['a', 's', 'd', 'f', 'g', 'h', 'j']
# коды клавиш
key_list = list(map(lambda x: ord(x), key_names))
# состояние клавиш (нажато/не нажато)
key_dict = dict([(key, False) for key in key_list])

if __name__ == '__main__':
    # инициализируем
    p = pa.PyAudio()
    # создаём поток для вывода
    stream = p.open(format=p.get_format_from_width(width=2),
                    channels=2, rate=SAMPLE_RATE, output=True)
    # размер окна pygame
    window_size = 320, 240
    # настраиваем экран
    screen = pygame.display.set_mode(window_size)
    pygame.display.flip()
    running = True
    while running:
        # обрабатываем события
        for event in pygame.event.get():
            # событие закрытия окна
            if event.type == pygame.QUIT:
                running = False
            # нажатия клавиш
            if event.type == pygame.KEYDOWN:
                if event.key == ord('q'):
                    running = False
                # обрабатываем нажатые клавиши по списку key_list
                for (index, key) in enumerate(key_list):
                    if event.key == key:
                        # зажимаем клавишу
                        key_dict[key] = True
            # отпускание клавиш
            if event.type == pygame.KEYUP:
                for (index, key) in enumerate(key_list):
                    if event.key == key:
                        # отпускаем клавишу
                        key_dict[key] = False
        # обрабатываем нажатые клавиши
        for (index, key) in enumerate(key_list):
            # если клавиша нажата
            if key_dict[key] == True:
                # то выводим звук на устройство
                stream.write(tones[index])
    # закрываем окно
    pygame.quit()
    # останавливаем устройство
    stream.stop_stream()
    # завершаем работу PyAudio
    stream.close()
    p.terminate()
