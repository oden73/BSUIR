import cv2
import numpy as np


def median_filter(image, kernel_size = 3):
    if kernel_size % 2 == 0:
        raise ValueError("Размер ядра должен быть нечетным.")

    height, width, channels = image.shape
    pad = kernel_size // 2

    filtered_image = np.zeros((height, width, channels), dtype=image.dtype)
    padded_image = np.pad(image, ((pad, pad), (pad, pad), (0, 0)), mode='reflect')

    for i in range(height):
        for j in range(width):
            for c in range(channels):
                region = padded_image[i:i + kernel_size, j:j + kernel_size, c]
                filtered_image[i, j, c] = np.median(region)

    return filtered_image


def salt_and_pepper_noise(image, salt_prob, pepper_prob):
    noisy = np.copy(image)
    total_pixels = image.size

    num_salt = np.ceil(salt_prob * total_pixels)
    coords = [np.random.randint(0, i - 1, int(num_salt)) for i in image.shape]
    noisy[coords[0], coords[1], :] = 1

    num_pepper = np.ceil(pepper_prob * total_pixels)
    coords = [np.random.randint(0, i - 1, int(num_pepper)) for i in image.shape]
    noisy[coords[0], coords[1], :] = 0

    return noisy


if __name__ == "__main__":
    image_path = './minion.jpg'
    image = cv2.imread(image_path, cv2.IMREAD_COLOR)

    if image is None:
        print("Ошибка: не удалось загрузить изображение.")
        exit()

    kernel_size = 3
    noisy_image = salt_and_pepper_noise(image, salt_prob=0.02, pepper_prob=0.02)
    filtered_image = median_filter(noisy_image, kernel_size)

    cv2.imshow('Original Image', image)
    cv2.imshow('Filtered Image', filtered_image)
    cv2.imshow('Noisy Image', noisy_image)

    cv2.waitKey(0)
    cv2.destroyAllWindows()
