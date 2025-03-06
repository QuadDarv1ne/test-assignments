from mrjob.job import MRJob

class MRWordCount(MRJob):
    """
    Класс для подсчета слов с использованием Hadoop Streaming API.

    Атрибуты:
        mapper (function): Функция для разбиения строки на слова.
        reducer (function): Функция для подсчета количества каждого слова.
    """
    def mapper(self, _, line):
        """
        Разбивает строку на слова и выдает каждое слово с единицей.

        Аргументы:
            _ (None): Ключ (не используется).
            line (str): Строка текста.

        Выход:
            (word, 1): Каждое слово с единицей.
        """
        for word in line.split():
            yield word, 1

    def reducer(self, word, counts):
        """
        Суммирует количество каждого слова.

        Аргументы:
            word (str): Слово.
            counts (list): Список единиц для данного слова.

        Выход:
            (word, sum(counts)): Слово и его количество.
        """
        yield word, sum(counts)

if __name__ == '__main__':
    MRWordCount.run()
