from .payload_generator import PayloadGenerator
from .request_handler import RequestHandler
from .response_analyzer import ResponseAnalyzer
from .logger import Logger

class SQLInjectionScanner:
    def __init__(self, url):
        self.url = url
        self.payload_generator = PayloadGenerator()
        self.request_handler = RequestHandler(url)
        self.response_analyzer = ResponseAnalyzer()
        self.logger = Logger()

    def scan(self):
        payloads = self.payload_generator.get_all_payloads()
        for payload in payloads:
            response = self.request_handler.send_payload(payload)
            if self.response_analyzer.is_vulnerable(response.text):
                self.logger.log_info(f"Vulnerable: {payload}")
                print(f"Possible SQL Injection with payload: {payload}")
    def scan_get(self, url):
        """
        Scans a URL using GET requests.
        """
        payloads = self.payload_generator.generate_basic_payloads()
        for payload in payloads:
            response = self.request_handler.send_get_request(url, payload)
            if self.response_analyzer.analyze_response(response):
                self.logger.log_success(url, payload)
            else:
                self.logger.log_failure(url, payload)

    def scan_post(self, url, post_data):
        """
        Scans a URL using POST requests.
        """
        payloads = self.payload_generator.generate_basic_payloads()
        for payload in payloads:
            post_data["input"] = payload  # Assumes 'input' is a POST parameter
            response = self.request_handler.send_post_request(url, post_data)
            if self.response_analyzer.analyze_response(response):
                self.logger.log_success(url, payload)
            else:
                self.logger.log_failure(url, payload)

    def scan_with_blind_payloads(self, url):
        """
        Scans a URL using blind SQL injection payloads.
        """
        payloads = self.payload_generator.generate_blind_payloads()
        for payload in payloads:
            response = self.request_handler.send_get_request(url, payload)
            if self.response_analyzer.analyze_response(response):
                self.logger.log_success(url, payload)
            else:
                self.logger.log_failure(url, payload)

    def add_custom_payload_and_scan(self, url, payload):
        """
        Adds a custom payload and scans the URL.
        """
        self.payload_generator.add_custom_payload(payload)
        response = self.request_handler.send_get_request(url, payload)
        if self.response_analyzer.analyze_response(response):
            self.logger.log_success(url, payload)
        else:
            self.logger.log_failure(url, payload)

    def show_logs(self):
        """
        Displays all logs from the scanning process.
        """
        self.logger.print_logs()
