class ResponseAnalyzer:
    def __init__(self):
        self.sql_errors = [
            "You have an error in your SQL syntax",
            "Warning: mysql_fetch_assoc()",
            "SQLSTATE[HY000]",
            "unclosed quotation mark",
            "Microsoft OLE DB Provider"
        ]

    def check_for_errors(self, response_text):
        return any(error in response_text for error in self.sql_errors)

    def is_vulnerable(self, response_text):
        return self.check_for_errors(response_text) or "error" in response_text.lower()

    def compare_response_length(self, normal_response, injected_response):
        return abs(len(normal_response) - len(injected_response))

    def analyze_bulk_responses(self, responses):
        return {payload: self.is_vulnerable(resp.text) for payload, resp in responses.items()}
