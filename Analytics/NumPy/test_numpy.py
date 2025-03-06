import numpy as np

def numpy_operations():
    """
    Выполняет базовые операции с массивами NumPy.

    Создает массив, вычисляет среднее значение, сумму и возводит элементы в квадрат.
    """
    arr = np.array([1, 2, 3, 4, 5])

    print("Среднее значение:", np.mean(arr))
    print("Сумма:", np.sum(arr))
    print("Массив в квадрате:", arr ** 2)

if __name__ == "__main__":
    numpy_operations()
