from pymongo import MongoClient

def test_mongodb_connection():
    """
    Подключается к MongoDB, добавляет документ в коллекцию и выполняет запрос.

    Создает подключение к MongoDB, добавляет документ в коллекцию 'test_collection'
    и выполняет запрос для получения документа с именем 'Test'.
    """
    client = MongoClient('mongodb://localhost:27017/')
    db = client['test_database']
    collection = db['test_collection']

    collection.insert_one({"name": "Test", "value": 42})

    result = collection.find_one({"name": "Test"})
    print(result)

if __name__ == "__main__":
    test_mongodb_connection()
