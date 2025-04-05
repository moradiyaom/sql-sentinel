class response_analyzer:
    """
    Analyzes HTTP responses for SQL injection indicators.
    """
    def __init__(self):
        self.error_keywords = [
            "database error",
            "you have an error in your SQL",
            "unclosed quotation mark",
            "ORA-",
            "unexpected end of SQL command",
            "You have an error in your SQL syntax",
            "Warning: mysql_fetch_assoc()",
            "SQLSTATE[HY000]",
            "unclosed quotation mark",
            "Microsoft OLE DB Provider"
        ]

    def analyze_response(self, response_text):
        for keyword in self.error_keywords:
            if keyword in response_text:
                return True
        return False
    def check_for_errors(self, response_text):
        return any(error in response_text for error in self.sql_errors)

    def is_vulnerable(self, response_text):
        return self.check_for_errors(response_text) or "error" in response_text.lower()

    def compare_response_length(self, normal_response, injected_response):
        return abs(len(normal_response) - len(injected_response))

    def analyze_bulk_responses(self, responses):
        return {payload: self.is_vulnerable(resp.text) for payload, resp in responses.items()}
