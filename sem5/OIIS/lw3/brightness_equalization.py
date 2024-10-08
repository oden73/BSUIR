import cv2
import numpy as np


def equalize_histogram(image):
    ycrcb = cv2.cvtColor(image, cv2.COLOR_BGR2YCrCb)
    channels = list(cv2.split(ycrcb))
    channels[0] = cv2.equalizeHist(channels[0])
    ycrcb = cv2.merge(channels)
    return cv2.cvtColor(ycrcb, cv2.COLOR_YCrCb2BGR)


def match_brightness(dark_image, light_image):
    dark_image_eq = equalize_histogram(dark_image)
    light_image_eq = equalize_histogram(light_image)

    mean1 = np.mean(dark_image_eq)
    mean2 = np.mean(light_image_eq)

    if mean2 != 0:
        correction_factor = mean1 / mean2
        light_image_corrected = cv2.convertScaleAbs(light_image_eq, alpha=correction_factor)
    else:
        light_image_corrected = light_image_eq

    return dark_image_eq, light_image_corrected


dark_image = cv2.imread('dark_image.jpg')
light_image = cv2.imread('light_image.jpg')

if dark_image is None:
    print("Ошибка: не удалось загрузить dark_image")
if light_image is None:
    print("Ошибка: не удалось загрузить light_image")

if dark_image is not None and light_image is not None:
    dark_image_eq, light_image_corrected = match_brightness(dark_image, light_image)

    cv2.imwrite('dark_image_equalized.jpg', dark_image_eq)
    cv2.imwrite('light_image_corrected.jpg', light_image_corrected)

    cv2.imshow('Image 1 Equalized', dark_image_eq)
    cv2.imshow('Image 2 Corrected', light_image_corrected)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
