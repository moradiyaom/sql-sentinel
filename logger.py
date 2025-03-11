import logging

class Logger:
    def __init__(self, log_file="scanner.log"):
        logging.basicConfig(filename=log_file, level=logging.INFO, format="%(asctime)s - %(message)s")
        self.logger = logging.getLogger()

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
