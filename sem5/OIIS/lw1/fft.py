import numpy as np
import matplotlib.pyplot as plt


def fft(x):
    N = len(x)

    if N <= 1:
        return x

    even = fft(x[0::2])
    odd = fft(x[1::2])

    W = [np.exp(-2j * np.pi * k / N) * odd[k] for k in range(N // 2)]

    return [complex(val) for val in [even[k] + W[k] for k in range(N // 2)] + \
            [even[k] - W[k] for k in range(N // 2)]]


def generate_cosine_signal(frequency, length):
    t = np.linspace(0, 1, length, endpoint=False)
    signal = np.cos(2 * np.pi * frequency * t)
    return signal.tolist()


def generate_sine_signal(frequency, length):
    t = np.linspace(0, 1, length, endpoint=False)
    signal = np.sin(2 * np.pi * frequency * t)
    return signal.tolist()

def plot_signal(signal, title):
    plt.figure(figsize=(12, 6))
    plt.plot(signal)
    plt.title(title)
    plt.xlabel('Sample Number')
    plt.ylabel('Amplitude')
    plt.grid()
    plt.show()


def plot_spectrum(spectrum, title):
    plt.figure(figsize=(12, 6))
    plt.plot(np.abs(spectrum))
    plt.title(title)
    plt.xlabel('Frequency Bin')
    plt.ylabel('Magnitude')
    plt.grid()
    plt.show()


if __name__ == "__main__":
    frequency = float(input("Введите частоту сигнала: "))
    length = int(input("Введите количество точек сигнала: "))
    func = int(input("Введите функцию(1 - sin, 2 - cos): "))

    signal = generate_sine_signal(frequency, length) if func == 1 else generate_cosine_signal(frequency, length)

    N = len(signal)
    next_pow_of_2 = 1 << (N - 1).bit_length()
    signal = list(signal)
    signal += [0] * (next_pow_of_2 - N)
    result_builtin_fft = np.fft.fft(signal)
    result_custom_fft = fft(signal)
    print("\nИсходный сигнал:", signal)
    print("Результат ручного БПФ:")
    print(result_custom_fft)
    print("\nРезультат встроенной функции np.fft.fft:")
    print(result_builtin_fft)
    difference = np.abs(np.array(result_custom_fft) - result_builtin_fft)
    print("\nРазница между результатами:")
    print(difference)

    are_close = np.all(np.isclose(result_custom_fft, result_builtin_fft))
    print("Результаты близки:", are_close)

    half_N = len(result_builtin_fft) // 2
    plot_spectrum(result_builtin_fft[:half_N], 'Спектр с использованием np.fft.fft')
    plot_spectrum(result_custom_fft[:half_N], 'Спектр с использованием пользовательского FFT')
