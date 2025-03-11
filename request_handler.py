import requests

class RequestHandler:
    def __init__(self, url):
        self.url = url

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
