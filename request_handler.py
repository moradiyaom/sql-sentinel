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
    
    def send_get(self, params=None):
        return requests.get(self.url, params=params)

    def send_post(self, data=None):
        return requests.post(self.url, data=data)

    def send_payload(self, payload, param="q"):
        return self.send_get({param: payload})

    def get_status_code(self, response):
        return response.status_code

    def get_response_text(self, response):
        return response.text

    def get_headers(self, response):
        return response.headers

    def send_bulk_payloads(self, payloads, param="q"):
        return {payload: self.send_payload(payload, param) for payload in payloads}