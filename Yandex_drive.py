import requests

class YaUploader:
    def __init__(self, token: str):
        self.token = token

    def get_headers(self):
        return {
            'Authorization': 'OAuth' + ' ' + self.token,
            'Content-Type': 'application/json'
        }
    
    def _get_upload_link(self, path_to_file):
        upload_url = 'https://cloud-api.yandex.net/v1/disk/resources/upload'
        self.path_to_file = path_to_file
        params = {'path': self.path_to_file, 'overwrite': 'true'}
        headers = self.get_headers()
        response = requests.get(url=upload_url, params=params, headers=headers)
        return response.json()

    def reading_file(self, file_name):
        with open(file_name, 'rb') as file:
            data = file.read()
        return data

    def upload(self, file_path: str):
        url = self._get_upload_link(path_to_file).get('href')
        response = requests.put(url=url, data=self.reading_file(filename))
        response.raise_for_status()
        if response.status_code == 201:
            print('Загрузка прошла успешно')
        

if __name__ == '__main__':
    filename = 'test.txt'
    path_to_file = '/Netology/' + filename
    token = ''
    uploader = YaUploader(token)
    uploader.upload(path_to_file)