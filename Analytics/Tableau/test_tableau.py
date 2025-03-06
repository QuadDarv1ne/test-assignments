from tableau_api_lib import TableauServerConnection

def connect_to_tableau():
    """
    Подключается к Tableau Server и выводит список проектов.

    Использует библиотеку tableau-api-lib для подключения к Tableau Server
    и извлечения информации о проектах.
    """
    tableau_server_config = {
        'my_env': {
            'server': 'http://your-server-url',
            'api_version': '3.10',
            'username': 'your-username',
            'password': 'your-password',
            'site_id': '',
            'site_name': ''
        }
    }

    conn = TableauServerConnection(config_json=tableau_server_config, env='my_env')
    conn.sign_in()

    projects = conn.query_projects()
    print(projects)

if __name__ == "__main__":
    connect_to_tableau()
