import cv2
import numpy as np
import transliterate
import movis as mv


def create_video_opencv(message: str):
    """
    :param message: текст бегущей строки
    :return: mp4 видео
    """

    # создание названия для видео
    if len(message) > 50:
        title = message[:50]
    elif len(message) == 0:
        title = 'empty-video'
    else:
        title = message
    # Транслит кодировок
    transliterated_message = transliterate.translit(message, 'ru', reversed=True)
    title = f"video_{transliterated_message}"
    # Размеры видео (ширина x высота)
    width, height = 100, 100
    # Задаём параметры - видеопоток с частотой 10 кадров в секунду
    out = cv2.VideoWriter(f"media/videos/{title}.mp4", cv2.VideoWriter_fourcc(*'XVID'), 10, (width, height))
    # Создаем кадр с черным фоном
    frame = np.zeros((height, width, 3), dtype=np.uint8)

    # Устанавливаем параметры шрифта
    font = cv2.FONT_HERSHEY_COMPLEX
    font_scale = 0.5  # размер шрифта
    font_thickness = 1  # толщина шрифта
    font_color = (255, 255, 255)  # цвет текста - БЕЛЫЙ

    # получение размеров текста в пикселях
    message_size = cv2.getTextSize(message, font, font_scale, font_thickness)
    # Рассчитываем скорость перемещения текста для достижения 3 секунд видео
    speed = (width + message_size[0][0]) / (3 * 10)  # 3 секунды, 10 кадров в секунду
    # Начальные координаты для бегущей строки: x - ширина видео, y - середина высоты видео
    x, y = width, height // 2

    while True:
        # Очистка кадра
        frame.fill(0)
        # Новые координаты для бегущей строки
        x -= speed  # Скорость бегущей строки
        # Вот тут добавим текст
        cv2.putText(frame, message, (int(x), y), font, font_scale, font_color, font_thickness)
        # Тут запишем кадр
        out.write(frame)
        # завершение видео при достижении текста левой части экрана
        if x + message_size[0][0] < 0:
            break

    # Закрываем видеопоток
    out.release()

    return {'title': title, 'path': f"videos/{title}.mp4"}


def convert_to_h264(file):
    intro = mv.layer.Video(file)
    scene = mv.layer.Composition(size=(100, 100), duration=0.1)
    masdin = mv.concatenate([intro, scene])
    masdin.write_video(file)
