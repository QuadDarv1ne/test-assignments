import dask.array as da

def dask_operations():
    """
    Выполняет операции с большими массивами с использованием Dask.

    Создает большой массив и вычисляет его среднее значение.
    """
    x = da.random.random((10000, 10000), chunks=(1000, 1000))

    mean = x.mean().compute()
    print("Среднее значение:", mean)

if __name__ == "__main__":
    dask_operations()
