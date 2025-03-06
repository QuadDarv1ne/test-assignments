import requests
import json

class GrafanaClient:
    """
    Клиент для взаимодействия с Grafana API.

    Атрибуты:
        base_url (str): Базовый URL Grafana сервера.
        api_key (str): API ключ для аутентификации.
    """

    def __init__(self, base_url, api_key):
        self.base_url = base_url
        self.api_key = api_key
        self.headers = {
            'Authorization': f'Bearer {self.api_key}',
            'Content-Type': 'application/json'
        }

    def create_dashboard(self, dashboard_data):
        """
        Создает новый дашборд в Grafana.

        Аргументы:
            dashboard_data (dict): Данные дашборда в формате JSON.

        Возвращает:
            response (dict): Ответ от API.
        """
        url = f"{self.base_url}/api/dashboards/db"
        response = requests.post(url, headers=self.headers, data=json.dumps(dashboard_data))
        return response.json()

    def get_dashboard(self, dashboard_uid):
        """
        Получает данные дашборда по его UID.

        Аргументы:
            dashboard_uid (str): UID дашборда.

        Возвращает:
            response (dict): Ответ от API.
        """
        url = f"{self.base_url}/api/dashboards/uid/{dashboard_uid}"
        response = requests.get(url, headers=self.headers)
        return response.json()

def main():
    """
    Основная функция для демонстрации работы с Grafana API.

    Создает клиент Grafana, создает новый дашборд и получает его данные.
    """
    grafana_client = GrafanaClient(base_url='http://your-grafana-url', api_key='your-api-key')

    # Пример данных для создания дашборда
    dashboard_data = {
        "dashboard": {
            "id": None,
            "uid": None,
            "title": "Sample Dashboard",
            "panels": [
                {
                    "id": 1,
                    "title": "Sample Panel",
                    "type": "graph",
                    "targets": [{"refId": "A"}]
                }
            ]
        },
        "overwrite": False
    }

    # Создаем дашборд
    created_dashboard = grafana_client.create_dashboard(dashboard_data)
    print("Созданный дашборд:", created_dashboard)

    # Получаем данные дашборда
    dashboard_uid = created_dashboard['uid']
    retrieved_dashboard = grafana_client.get_dashboard(dashboard_uid)
    print("Полученный дашборд:", retrieved_dashboard)

if __name__ == "__main__":
    main()
