import tensorflow as tf
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense

def train_simple_model():
    """
    Создает и обучает простую модель нейронной сети с использованием TensorFlow.

    Создает модель с одним слоем, компилирует ее и обучает на случайных данных.
    """
    model = Sequential([
        Dense(10, activation='relu', input_shape=(10,)),
        Dense(1)
    ])

    model.compile(optimizer='adam', loss='mse')

    import numpy as np
    x_train = np.random.rand(100, 10)
    y_train = np.random.rand(100, 1)

    model.fit(x_train, y_train, epochs=10)

    print("Обучение завершено!")

if __name__ == "__main__":
    train_simple_model()
