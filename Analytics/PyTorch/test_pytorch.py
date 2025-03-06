import torch
import torch.nn as nn
import torch.optim as optim

class SimpleNet(nn.Module):
    """
    Простая нейронная сеть с одним линейным слоем.

    Атрибуты:
        fc (nn.Linear): Линейный слой с 10 входами и 1 выходом.
    """
    def __init__(self):
        super(SimpleNet, self).__init__()
        self.fc = nn.Linear(10, 1)

    def forward(self, x):
        """
        Прямой проход через сеть.

        Аргументы:
            x (torch.Tensor): Входной тензор.

        Возвращает:
            torch.Tensor: Выходной тензор после линейного слоя.
        """
        return self.fc(x)

def train_model():
    """
    Обучает простую нейронную сеть на случайных данных.

    Создает модель SimpleNet, функцию потерь и оптимизатор.
    Генерирует случайные входные и целевые данные, затем обучает модель.
    """
    model = SimpleNet()
    criterion = nn.MSELoss()
    optimizer = optim.SGD(model.parameters(), lr=0.01)

    inputs = torch.randn(5, 10)
    targets = torch.randn(5, 1)

    for epoch in range(100):
        optimizer.zero_grad()
        outputs = model(inputs)
        loss = criterion(outputs, targets)
        loss.backward()
        optimizer.step()

    print("Обучение завершено!")

if __name__ == "__main__":
    train_model()
