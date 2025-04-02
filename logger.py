class logger:
    """
    Handles logging of scan results.
    """
    def __init__(self):
        self.logs = []

    def log_success(self, url, payload):
        self.logs.append(f"[SUCCESS] SQL Injection found at {url} with payload: {payload}")

    def log_failure(self, url, payload):
        self.logs.append(f"[FAILURE] No SQL Injection found at {url} with payload: {payload}")

    def print_logs(self):
        for log in self.logs:
            print(log)
