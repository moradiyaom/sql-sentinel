import logging


class logger:
    """
    Handles logging of scan results.
    """
    def __init__(self, log_file="scanner.log"):
        self.logs = []
        logging.basicConfig(filename=log_file, level=logging.INFO, format="%(asctime)s - %(message)s")
        self.logger = logging.getLogger()

    def log_success(self, url, payload):
        self.logs.append(f"[SUCCESS] SQL Injection found at {url} with payload: {payload}")

    def log_failure(self, url, payload):
        self.logs.append(f"[FAILURE] No SQL Injection found at {url} with payload: {payload}")

    def print_logs(self):
        for log in self.logs:
            print(log)

    def log_info(self, message):
        self.logger.info(message)

    def log_warning(self, message):
        self.logger.warning(message)

    def log_error(self, message):
        self.logger.error(message)

    def read_logs(self):
        with open("scanner.log", "r") as f:
            return f.readlines()

    def clear_logs(self):
        open("scanner.log", "w").close()