import requests


class request_handler:
    """
    Handles sending HTTP requests for scanning.
    """
    @staticmethod
    def send_get_request(url, payload):
        try:
            response = requests.get(url + payload)
            return response.text
        except requests.RequestException as e:
            return f"Error: {str(e)}"

    @staticmethod
    def send_post_request(url, data):
        try:
            response = requests.post(url, data=data)
            return response.text
        except requests.RequestException as e:
            return f"Error: {str(e)}"
