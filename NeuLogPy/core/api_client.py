import requests

class NeuLogAPIClient:
    def __init__(self, host, port):
        self.base_url = f"http://{host}:{port}/NeuLogAPI"

    def send_request(self, command, params=""):
        url = f"{self.base_url}?{command}:{params}"
        try:
            response = requests.get(url)
            response.raise_for_status()
            return response.json()
        except requests.exceptions.RequestException as e:
            print(f"Error: {e}")
            return None
