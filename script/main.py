import cv2
import numpy as np
import transliterate


def create_video_opencv(message: str):
    """
    :param message: текст бегущей строки
    :return: mp4 видео
    """

    # создание названия для видео
    if len(message) > 50:
        title = message[:50]
    elif len(message) == 0:
        title = 'empty-videos'
    else:
        title = message
    # ъ использован для работы и с латинскими символами
    title = transliterate.slugify('ъ' + title)
    # Размеры видео (ширина x высота)
    width, height = 1920, 1080
    # Задаём параметры - видеопоток с частотой 24 кадра в секунду
    fourcc = cv2.VideoWriter_fourcc(*'xvid')  # Use 'XVID' for H .264 codec
    out = cv2.VideoWriter(f"{title}.mp4", fourcc, 24, (width, height))
    # Создаем кадр с черным фоном
    frame = np.zeros((height, width, 3), dtype=np.uint8)

    # Устанавливаем параметры шрифта
    font = cv2.FONT_HERSHEY_COMPLEX
    font_scale = 10
    font_thickness = 10
    font_color = (255, 255, 255)  # цвет текста - БЕЛЫЙ

    # получение размеров текста в пикселях
    message_size = cv2.getTextSize(message, font, font_scale, font_thickness)
    # Начальные координаты для бегущей строки: x - ширина видео, y - середина высоты видео
    x, y = width, height // 2

    while True:
        # Очистка кадра
        frame.fill(0)
        # Новые координаты для бегущей строки
        x -= 30  # Скорость бегущей строки
        # Вот тут добавим текст
        cv2.putText(frame, message, (x, y), font, font_scale, font_color, font_thickness)
        # Тут запишем кадр
        out.write(frame)
        # завершение видео при достижении текста левой части экрана
        if x + message_size[0][0] < 0:
            break

    # Закрываем видеопоток
    out.release()
    return {'name': 'lol'}


def main():
    message = input('Введите текст бегущей строки: ')
    create_video_opencv(message)


if __name__ == '__main__':
    main()
